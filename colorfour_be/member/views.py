import logging
from django.db import transaction
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import UserAuthProvider



logger = logging.getLogger(__name__)
User = get_user_model()

class CustomSocialLoginView(SocialLoginView):
    def get_response(self):
        try:
            # 呼叫父類別的處理邏輯
            response = super().get_response()

            if self.user:
                # 如果用戶不存在，則自動創建
                user, created = User.objects.get_or_create(
                    email=self.user.email,
                    defaults={
                        "first_name": self.user.first_name,
                        "last_name": self.user.last_name,
                    },
                )
                if created:
                    logger.info(f"New user created: {user.email}")

                # 更新第三方登入紀錄
                self._update_auth_provider(user)
            else:
                raise ValueError("User is None")
            if created:
                logger.info(f"New user created: {user.email}")

            # 更新第三方登入紀錄
            self._update_auth_provider(user)

            return response

        except Exception as e:
            logger.error(f"Social login error: {str(e)}")
            return Response(
                {"detail": "Social login error"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def _update_auth_provider(self, user):
        """建立或更新第三方登入紀錄"""
        provider = self.serializer.context.get("view").adapter_class.provider_id
        provider_id = self.serializer.validated_data.get("id")

        if provider and provider_id:
            UserAuthProvider.objects.update_or_create(
                user=user,
                provider=provider,
                defaults={"provider_id": provider_id, "last_login": now()},
            )
            logger.info(f"Auth provider updated for user: {user.email}")


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
