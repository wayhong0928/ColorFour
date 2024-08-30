import logging
from math import log
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import UserAuthProvider
from .serializers import UserAuthProviderSerializer


def handle_user_auth_provider(user, provider, provider_id=None, email=None):
    if provider_id:
        UserAuthProvider.objects.get_or_create(
            user=user, provider=provider, defaults={"provider_id": provider_id}
        )
    elif email:
        UserAuthProvider.objects.get_or_create(
            user=user, provider=provider, defaults={"provider_id": email}
        )
    else:
        raise ValueError("Either provider_id or email must be provided")


class CustomGoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8080/callback"
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.request.user
        provider = "google"
        provider_id = None

        # 檢查 response.data 是否包含 user 資訊
        if isinstance(response.data, dict) and "user" in response.data:
            user_info = response.data["user"]
            email = user_info.get("email", None)
        else:
            email = None

        if provider_id is None and email is None:
            return Response(
                {"detail": "Unable to retrieve user ID or email from Google response"},
                status=400,
            )

        # 使用 email 進行綁定
        handle_user_auth_provider(user, provider, provider_id, email)
        return response


class CustomLineLogin(SocialLoginView):
    adapter_class = LineOAuth2Adapter
    callback_url = "http://localhost:8080/callback"
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = self.request.user
        provider = "line"
        provider_id = None
        logging.info(response.data)
        # 檢查 response.data 是否包含 Line 的使用者資訊
        # if isinstance(response.data, dict) and "user" in response.data:
        #     user_info = response.data["user"]
        #     email = user_info.get("email", None)
        #     provider_id = user_info.get("user_id", None)
        # else:
        #     email = None

        # if provider_id is None and email is None:
        #     return Response(
        #         {"detail": "Unable to retrieve user ID or email from Line response"},
        #         status=400,
        #     )

        # # 使用 email 或 provider_id 進行綁定
        # handle_user_auth_provider(user, provider, provider_id, email)
        # return response


class UserAuthProviderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        providers = UserAuthProvider.objects.filter(user=request.user)
        serializer = UserAuthProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request):
        provider_name = request.data.get("provider")
        provider_id = request.data.get("provider_id")

        if UserAuthProvider.objects.filter(
            user=request.user, provider=provider_name
        ).exists():
            return Response({"detail": "此登入方式已綁定"}, status=400)

        UserAuthProvider.objects.create(
            user=request.user, provider=provider_name, provider_id=provider_id
        )
        return Response({"detail": "綁定成功"})

    def delete(self, request):
        provider_name = request.data.get("provider")

        provider = UserAuthProvider.objects.filter(
            user=request.user, provider=provider_name
        ).first()
        if provider:
            provider.delete()
            return Response({"detail": "取消綁定成功"})
        return Response({"detail": "找不到該綁定方式"}, status=400)


class BindAnotherLoginProvider(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        provider_name = request.data.get("provider_name")
        provider_user_id = request.data.get("provider_user_id")

        if UserAuthProvider.objects.filter(
            user=request.user, provider=provider_name
        ).exists():
            return Response({"detail": "此登入方式已綁定"}, status=400)

        UserAuthProvider.objects.create(
            user=request.user,
            provider=provider_name,
            provider_id=provider_user_id,
        )
        return Response({"detail": "綁定成功"})
