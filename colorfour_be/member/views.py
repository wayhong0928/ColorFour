import logging
import os
from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ImproperlyConfigured
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import UserAuthProvider
from .serializers import UserAuthProviderSerializer

logger = logging.getLogger(__name__)

class CustomSocialLoginView(SocialLoginView):
    def get_response(self):
        try:
            response = super().get_response()
            if self.user and hasattr(self, 'serializer'):
                provider = self.serializer.context.get('view').adapter_class.provider_id
                uid = self.serializer.validated_data.get('uid')
                
                if provider and uid:
                    auth_provider, created = UserAuthProvider.objects.get_or_create(
                        user=self.user,
                        provider=provider,
                        defaults={'provider_id': uid}
                    )
                    if not created:
                        auth_provider.last_login = timezone.now()
                        auth_provider.save()
                    if response.data is not None:
                        response.data['new_association'] = created
                else:
                    logger.warning(f"Provider or UID not found for user {self.user.id}")
            return response
        except Exception as e:
            logger.error(f"Error in CustomSocialLoginView: {str(e)}")
            return Response({"detail": "social login error"}, status=500)

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

    def get(self, request):
        providers = UserAuthProvider.objects.filter(user=request.user)
        serializer = UserAuthProviderSerializer(providers, many=True)
        return Response(serializer.data)

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
                existing_provider = UserAuthProvider.objects.filter(
                    user=request.user, provider=provider
                ).first()

                if existing_provider:
                    return Response(
                        {
                            "detail": f"A {provider} account is already bound to this user."
                        },
                        status=400,
                    )

                # 使用提供的 code 進行身份驗證
                auth_login = view.post(request._request)
                if auth_login.status_code != 200:
                    return Response({"detail": "Authentication failed."}, status=400)

                # 創建新的 UserAuthProvider
                UserAuthProvider.objects.create(
                    user=request.user,
                    provider=provider,
                    provider_id=auth_login.data.get("user", {}).get("id") if auth_login.data and "user" in auth_login.data else None,
                )

                provider_id = auth_login.data.get("user", {}).get("id") if auth_login.data and "user" in auth_login.data else None

                if provider_id:
                    return Response({"detail": f"{provider} 帳號綁定成功。"})
                else:
                    return Response({"detail": "無法獲取提供者ID。"}, status=400)
        except Exception as e:
            logger.error(f"Error in binding social account: {str(e)}")
            return Response(
                {"detail": "An error occurred while binding the account."}, status=500
            )
