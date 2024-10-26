<template>
  <div>
    <button class="btn-main google-button" @click="loginWithGoogle">
      <img src="../assets/img/web_light_rd_na@1x.png" alt="Google Logo" />
      使用 Google 登入
    </button>
    <button class="btn-main line-button" @click="loginWithLine">
      <img src="../assets/img/line_44.png" alt="LINE Logo" />
      使用 LINE 登入
    </button>
    <p>登入後會取得用戶 Email 等個人資訊作為會員個人資訊使用。</p>
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
  </div>
</template>

<script>
  import { mapActions } from "vuex";

  export default {
    data() {
      return {
        errorMessage: null,
      };
    },
    computed: {
      googleLoginUrl() {
        return `${process.env.VUE_APP_BACKEND_URL}/member/login/google/`;
      },
      lineLoginUrl() {
        return `${process.env.VUE_APP_BACKEND_URL}/member/login/line/`;
      },
    },
    methods: {
      ...mapActions("auth", ["loginWithGoogleCode", "loginWithLineCode"]),
      loginWithGoogle() {
        const googleAuthUrl = "https://accounts.google.com/o/oauth2/v2/auth";
        const params = {
          response_type: "code",
          client_id: process.env.VUE_APP_GOOGLE_CLIENT_ID,
          redirect_uri: process.env.VUE_APP_LOGIN_CALLBACK,
          scope: "openid email profile",
          access_type: "offline",
          prompt: "consent",
          state: "google",
        };
        const urlParams = new URLSearchParams(params).toString();
        window.location.href = `${googleAuthUrl}?${urlParams}`;
      },
      loginWithLine() {
        const lineAuthUrl = "https://access.line.me/oauth2/v2.1/authorize";
        const params = {
          response_type: "code",
          client_id: process.env.VUE_APP_LINE_LOGIN_CHANNEL_ID,
          redirect_uri: process.env.VUE_APP_LOGIN_CALLBACK,
          scope: "profile openid email",
          state: "line",
        };
        const urlParams = new URLSearchParams(params).toString();
        window.location.href = `${lineAuthUrl}?${urlParams}`;
      },
    },
  };
</script>

<style scoped>
  .login-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    max-height: 100vh;
    background-color: var(--primary-bg-color);
  }

  .login-title {
    font-size: 2rem;
    color: var(--primary-text-color);
    margin-bottom: 2rem;
  }

  .btn-main {
    background-color: #06c755 !important;
    border-color: #06c755;
    border-radius: 20px;
    padding: 10px 20px;
    text-decoration: none;
    color: #fff;
    display: flex;
    align-items: center;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.3s, border-color 0.3s;
    margin-bottom: 1rem;
  }

  .btn-main:hover {
    background-color: var(--button-hover-bg-color);
    border-color: var(--button-hover-bg-color);
  }

  .btn-main img {
    vertical-align: middle;
    margin-right: 8px;
  }

  .google-button {
    background-color: #4285f4 !important;
    border-color: #4285f4;
  }

  .google-button:hover {
    background-color: #357ae8;
    border-color: #357ae8;
  }
</style>
