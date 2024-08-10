import json
from django.http import HttpResponseRedirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.models import SocialAccount
from django.conf import settings
import requests
from .models import UserProfile
import logging

logger = logging.getLogger(__name__)


class GoogleLogin(SocialLoginView):
	adapter_class = GoogleOAuth2Adapter


class LineLogin(SocialLoginView):
	adapter_class = LineOAuth2Adapter


class LineLoginCallback(APIView):
	def get(self, request, *args, **kwargs):
		code = request.GET.get("code")
		state = request.GET.get("state")
		session_state = request.session.get("oauth_state")

		logger.debug(
			f"Received code: {code}, state: {state}, session state: {session_state}"
		)

		if not state or state != session_state:
			logger.error("Invalid state: Received state does not match session state")
			return HttpResponseRedirect(
				f"{settings.FRONTEND_URL}/?loginResult=failure&message=Invalid state"
			)

		if code:
			try:
				user_info = self.authenticate_with_line(
					code, settings.LINE_LOGIN_CALLBACK_URL
				)
				logger.debug(f"User info: {user_info}")
				user, created = self.create_or_get_user(user_info)
				if created:
					return HttpResponseRedirect(
						f"{settings.FRONTEND_URL}/profile-setup"
					)
				return HttpResponseRedirect(
					f"{settings.FRONTEND_URL}/?loginResult=success"
				)
			except Exception as e:
				logger.error(f"Error during Line login: {e}")
				return HttpResponseRedirect(
					f"{settings.FRONTEND_URL}/?loginResult=failure&message={str(e)}"
				)
		return HttpResponseRedirect(
			f"{settings.FRONTEND_URL}/?loginResult=failure&message=No code provided"
		)

	def authenticate_with_line(self, code, redirect_uri):
		client_id = settings.LINE_LOGIN_CHANNEL_ID
		client_secret = settings.LINE_LOGIN_CHANNEL_SECRET

		token_url = "https://api.line.me/oauth2/v2.1/token"
		headers = {"Content-Type": "application/x-www-form-urlencoded"}
		data = {
			"grant_type": "authorization_code",
			"code": code,
			"redirect_uri": redirect_uri,
			"client_id": client_id,
			"client_secret": client_secret,
		}

		response = requests.post(token_url, headers=headers, data=data)
		logger.debug(f"Line token response: {response.content}")
		if response.status_code != 200:
			logger.error(f"Failed to obtain access token from LINE: {response.content}")
			raise Exception(
				f"Failed to obtain access token from LINE: {response.content}"
			)

		access_token = response.json().get("access_token")
		if not access_token:
			logger.error(
				"Failed to obtain access token from LINE: No access token received"
			)
			raise Exception("Failed to obtain access token from LINE")

		return self.get_line_user_info(access_token)

	def get_line_user_info(self, access_token):
		user_info_url = "https://api.line.me/v2/profile"
		headers = {"Authorization": f"Bearer {access_token}"}

		response = requests.get(user_info_url, headers=headers)
		logger.debug(f"Line user info response: {response.content}")
		if response.status_code != 200:
			logger.error(f"Failed to obtain user info from LINE: {response.content}")
			raise Exception(f"Failed to obtain user info from LINE: {response.content}")

		return response.json()

	def create_or_get_user(self, user_info):
		user, created = User.objects.get_or_create(
			username=user_info["userId"],
			defaults={"first_name": user_info["displayName"]},
		)
		profile, created = UserProfile.objects.get_or_create(
			user=user, defaults={"line_id": user_info["userId"]}
		)
		if created:
			profile.is_new_user = True
			profile.save()
		return user, created


class GoogleLoginCallback(APIView):
	def get(self, request, *args, **kwargs):
		code = request.GET.get("code")
		state = request.GET.get("state")
		session_state = request.session.get("oauth_state")

		logger.debug(
			f"Received code: {code}, state: {state}, session state: {session_state}"
		)

		if not state or state != session_state:
			logger.error("Invalid state: Received state does not match session state")
			return HttpResponseRedirect(
				f"{settings.FRONTEND_URL}/?loginResult=failure&message=Invalid state"
			)

		if code:
			try:
				user_info = self.authenticate_with_google(
					code, settings.GOOGLE_LOGIN_CALLBACK_URL
				)
				logger.debug(f"User info: {user_info}")
				user, created = self.create_or_get_user(user_info)
				if created:
					return HttpResponseRedirect(
						f"{settings.FRONTEND_URL}/profile-setup"
					)
				return HttpResponseRedirect(
					f"{settings.FRONTEND_URL}/?loginResult=success"
				)
			except Exception as e:
				logger.error(f"Error during Google login: {e}")
				return HttpResponseRedirect(
					f"{settings.FRONTEND_URL}/?loginResult=failure&message={str(e)}"
				)
		return HttpResponseRedirect(
			f"{settings.FRONTEND_URL}/?loginResult=failure&message=No code provided"
		)

	def authenticate_with_google(self, code, redirect_uri):
		client_id = settings.GOOGLE_CLIENT_ID
		client_secret = settings.GOOGLE_CLIENT_SECRET

		token_url = "https://oauth2.googleapis.com/token"
		headers = {"Content-Type": "application/x-www-form-urlencoded"}
		data = {
			"grant_type": "authorization_code",
			"code": code,
			"redirect_uri": redirect_uri,
			"client_id": client_id,
			"client_secret": client_secret,
		}

		response = requests.post(token_url, headers=headers, data=data)
		logger.debug(f"Google token response: {response.content}")
		if response.status_code != 200:
			logger.error(
				f"Failed to obtain access token from Google: {response.content}"
			)
			raise Exception(
				f"Failed to obtain access token from Google: {response.content}"
			)

		access_token = response.json().get("access_token")
		if not access_token:
			logger.error(
				"Failed to obtain access token from Google: No access token received"
			)
			raise Exception("Failed to obtain access token from Google")

		return self.get_google_user_info(access_token)

	def get_google_user_info(self, access_token):
		user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
		headers = {"Authorization": f"Bearer {access_token}"}

		response = requests.get(user_info_url, headers=headers)
		logger.debug(f"Google user info response: {response.content}")
		if response.status_code != 200:
			logger.error(f"Failed to obtain user info from Google: {response.content}")
			raise Exception(
				f"Failed to obtain user info from Google: {response.content}"
			)

		return response.json()

	def create_or_get_user(self, user_info):
		user, created = User.objects.get_or_create(
			username=user_info["id"],
			defaults={
				"first_name": user_info["given_name"],
				"last_name": user_info["family_name"],
				"email": user_info["email"],
			},
		)
		profile, created = UserProfile.objects.get_or_create(
			user=user, defaults={"google_id": user_info["id"]}
		)
		if created:
			profile.is_new_user = True
			profile.save()
		return user, created
