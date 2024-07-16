<template>
  <div class="login-container">
    <h1 class="login-title">登入</h1>
    <button class="btn-main" @click="openLineLogin">
      <img src="../assets/img/btn_login_base.png" alt="LINE Logo" />
      使用 LINE 登入
    </button>
    <!-- 尚未實作 Google 的第三方登入 -->
    <button class="btn-main google-button" @click="openGoogleLogin">
      <!-- <img src="../assets/google_logo.png" alt="Google Logo" /> -->
      使用 Google 登入
    </button>
  </div>
</template>

<script>
  import { ref, onMounted } from "vue";
  import { useToast } from "vue-toastification";
  import "vue-toastification/dist/index.css";

  export default {
    name: "Login",
    setup() {
      const client_id = ref("2005742580");
      const redirect_uri = ref("https://upward-gorgeous-bedbug.ngrok-free.app/line/login");
      const google_client_id = ref("YOUR_GOOGLE_CLIENT_ID");
      const google_redirect_uri = ref("https://upward-gorgeous-bedbug.ngrok-free.app/google/login");
      const toastOptions = {
        position: "top-center",
        timeout: 3000,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        showCloseButtonOnHover: false,
        hideProgressBar: false,
        closeButton: "button",
        icon: true,
        rtl: false,
      };

      const toast = useToast();

      // 使用者點擊 LINE 登入按鈕觸發
      const openLineLogin = () => {
        const link = `https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=${client_id.value}&redirect_uri=${redirect_uri.value}&state=login&scope=openid%20profile&bot_prompt=aggressive`;
        window.location.href = link;
      };

      // 使用者點擊 Google 登入按鈕觸發
      const openGoogleLogin = () => {
        const link = `https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=${google_client_id.value}&redirect_uri=${google_redirect_uri.value}&scope=openid%20email%20profile&state=login`;
        window.location.href = link;
      };

      const showHomeToast = () => toast("登入成功", toastOptions);

      const showErrorToast = () => toast.error("登入失敗，請重試", toastOptions);

      // 檢查 URL 中的登入結果標記
      const checkLoginResult = () => {
        const urlParams = new URLSearchParams(window.location.search);
        const loginResult = urlParams.get("loginResult");

        if (loginResult === "success") {
          showHomeToast();
        } else if (loginResult === "failure") {
          showErrorToast();
        }
      };

      onMounted(checkLoginResult);

      return {
        openLineLogin,
        openGoogleLogin,
      };
    },
  };
</script>

<style scoped>
  .login-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: var(--primary-bg-color);
  }

  .login-title {
    font-size: 2rem;
    color: var(--primary-text-color);
    margin-bottom: 2rem;
  }

  .btn-main {
    background-color: var(--button-bg-color) !important;
    border-color: var(--button-bg-color);
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
    background-color: var(--button-hover-bg-color); /* Change background color on hover */
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
    background-color: #357ae8; /* Change background color on hover */
    border-color: #357ae8;
  }
</style>
