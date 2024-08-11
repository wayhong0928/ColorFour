<template>
  <div>
    <button v-if="!isAuthenticated" class="btn-main google-button" @click="loginWithGoogle">
      <img src="../assets/img/web_light_rd_na@1x.png" alt="Google Logo" />
      使用 Google 登入
    </button>
    <button v-if="!isAuthenticated" class="btn-main line-button" @click="loginWithLine">
      <img src="../assets/img/line_44.png" alt="LINE Logo" />
      使用 LINE 登入
    </button>
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isAuthenticated: false, 
      errorMessage: null,
      googleLoginUrl: `${process.env.VUE_APP_NGROK_URL}/accounts/google/login`,
      lineLoginUrl: `${process.env.VUE_APP_NGROK_URL}/accounts/line/login`,
    };
  },
  methods: {
    loginWithGoogle() {
      window.location.href = this.googleLoginUrl;
    },
    loginWithLine() {
      window.location.href = this.lineLoginUrl;
    },
    checkAuthentication() {
      const token = localStorage.getItem('token');
      this.isAuthenticated = !!token;  // 若 token 存在，表示已登入
    },
  },
  mounted() {
    this.checkAuthentication(); 
  },
};
</script>


<!-- <script>
  import axios from "axios";

  export default {
    data() {
      return {
        errorMessage: "",
        state: Math.random().toString(36).substring(7),
      };
    },
    methods: {
      async handleLoginResponse(provider, code) {
        try {
          const response = await axios.post(`/auth/${provider}/callback/`, { code, state: this.state });
          if (response.data.success) {
            localStorage.setItem("authToken", response.data.access_token);
            this.$store.commit("setAuth", true);
            this.$store.commit("setUser", response.data.user);
            this.$router.push("/");
            alert("登入成功！");
          } else {
            this.errorMessage = "登入失敗，請重試。";
          }
        } catch (error) {
          this.errorMessage = "登入失敗，請重試。";
        }
      },
      loginWithGoogle() {
        const clientId = process.env.VUE_APP_GOOGLE_CLIENT_ID;
        const redirectUri = encodeURIComponent(process.env.VUE_APP_GOOGLE_LOGIN_CALLBACK);
        const scope = encodeURIComponent("email profile");
        const responseType = "code";
        const state = Math.random().toString(36).substring(7); // Generate random state
        sessionStorage.setItem("oauth_state", state); // Save state in session storage
        window.location.href = `https://accounts.google.com/o/oauth2/auth?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=${responseType}&scope=${scope}&state=${state}`;
      },
      loginWithLine() {
        const clientId = process.env.VUE_APP_LINE_LOGIN_CHANNEL_ID;
        const redirectUri = encodeURIComponent(process.env.VUE_APP_LINE_LOGIN_CALLBACK);
        const scope = encodeURIComponent("openid profile email");
        const responseType = "code";
        const state = Math.random().toString(36).substring(7); // Generate random state
        sessionStorage.setItem("oauth_state", state); // Save state in session storage
        window.location.href = `https://access.line.me/oauth2/v2.1/authorize?response_type=${responseType}&client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scope}&state=${state}`;
      },
    },
  };
</script> -->

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
