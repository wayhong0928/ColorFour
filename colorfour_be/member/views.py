from http import client
import logging
from pydoc import cli
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


logger = logging.getLogger(__name__)
User = get_user_model()


class CustomSocialLoginView(SocialLoginView):
    def get_response(self):
        response = super().get_response()
        user = self.user

        # 若使用者不存在則自動創建
        if user and user.is_active:
            self._create_or_update_user(user)

        return response

    def _create_or_update_user(self, user):
        """
        將第三方登入的使用者資料存入 User 資料庫中。
        """
        try:
            if self.user:
                user_data = {
                    "first_name": self.user.first_name,
                    "last_name": self.user.last_name,
                    "email": self.user.email,
                }
            else:
                logger.error("無法創建或更新使用者: self.user 為 None")
                return
            User.objects.update_or_create(email=user.email, defaults=user_data)
            logger.info(f"使用者 {user.email} 已成功登入或創建。")
        except Exception as e:
            logger.error(f"無法創建或更新使用者: {str(e)}")


class CustomGoogleLogin(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8080/callback"
    client_class = OAuth2Client

    def get_response(self):
        try:
            response = super().get_response()
        except Exception as e:
            logger.error(f"Google 登入失敗: {str(e)}")
            return Response(
                {"detail": "無法完成 Google 登入"}, status=status.HTTP_400_BAD_REQUEST
            )
        return response


class CustomLineLogin(CustomSocialLoginView):
    adapter_class = LineOAuth2Adapter
    callback_url = "http://localhost:8080/callback"
    client_class = OAuth2Client
