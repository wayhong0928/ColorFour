import logging
from django.db import transaction
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import UserAuthProvider


logger = logging.getLogger(__name__)


class CustomSocialLoginView(SocialLoginView):
    def get_response(self):
        try:
            # 調用父類別的回應
            response = super().get_response()

            # 檢查用戶是否正確綁定
            if self.user and hasattr(self, "serializer"):
                provider = self.serializer.context.get("view").adapter_class.provider_id
                provider_id = self.serializer.validated_data.get("id")

                # 建立或更新 UserAuthProvider 紀錄
                if provider and provider_id:
                    auth_provider, created = UserAuthProvider.objects.get_or_create(
                        user=self.user,
                        provider=provider,
                        defaults={"provider_id": provider_id},
                    )
                    if not created:
                        auth_provider.last_login = now()
                        auth_provider.save()

                # 生成新的 JWT Token 並回傳
                tokens = self.generate_tokens(self.user)

                # 回應包含完整的使用者資料與 token
                return Response(
                    {
                        "access": tokens["access"],
                        "refresh": tokens["refresh"],
                        "user": {
                            "pk": self.user.pk,
                            "email": self.user.email,
                            "first_name": self.user.first_name,
                            "last_name": self.user.last_name,
                            "role": (
                                self.user.role.role_name if self.user.role else "user"
                            ),
                        },
                    }
                )
        except Exception as e:
            logger.error(f"Error in CustomSocialLoginView: {str(e)}")
            return Response({"detail": "social login error"}, status=500)

    def generate_tokens(self, user):
        """生成新的 access 和 refresh token"""
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(access),
        }


class CustomGoogleLogin(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8080/callback"
    client_class = OAuth2Client


class CustomLineLogin(CustomSocialLoginView):
    adapter_class = LineOAuth2Adapter
    callback_url = "http://localhost:8080/callback"
    client_class = OAuth2Client

class UserAuthProviderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        provider = request.data.get("provider")
        code = request.data.get("code")

        if not provider or not code:
            return Response({"detail": "Provider and code are required."}, status=400)

        if provider not in ["google", "line"]:
            return Response({"detail": "Invalid provider."}, status=400)

        view_class = CustomGoogleLogin if provider == "google" else CustomLineLogin
        view = view_class()
        view.request = request

        try:
            with transaction.atomic():
                # 檢查是否已存在綁定
                existing_provider = UserAuthProvider.objects.filter(
                    user=request.user, provider=provider
                ).first()

                if existing_provider:
                    return Response(
                        {"detail": f"{provider} 已綁定此帳號。"},
                        status=400,
                    )

                # 調用登入邏輯，進行身份驗證
                auth_login = view.post(request._request)

                if auth_login.status_code != 200:
                    return Response({"detail": "Authentication failed."}, status=400)

                provider_id = auth_login.data.get("user", {}).get("id")
                if not provider_id:
                    return Response({"detail": "無法獲取提供者ID。"}, status=400)

                # 建立新的 UserAuthProvider
                UserAuthProvider.objects.create(
                    user=request.user,
                    provider=provider,
                    provider_id=provider_id,
                    created_at=now(),
                    last_login=now(),
                )

                return Response({"detail": f"{provider} 帳號綁定成功。"})

        except Exception as e:
            logger.error(f"Error in binding social account: {str(e)}")
            return Response(
                {"detail": "An error occurred while binding the account."}, status=500
            )
