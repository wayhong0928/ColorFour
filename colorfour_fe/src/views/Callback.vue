<template>
  <div>
    <p v-if="loading">正在處理登入，請稍候...</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      loading: true,
      errorMessage: null,
    };
  },
  methods: {
    ...mapActions("auth", ["login"]),
    async handleCallback() {
      try {
        const code = new URL(window.location.href).searchParams.get("code");
        const state = new URL(window.location.href).searchParams.get("state");

        console.log("OAuth Code:", code);
        console.log("OAuth State:", state);

        if (!code) {
          throw new Error("缺少授權碼，請重新登入");
        }

        if (state === "google" || state === "line") {
          const token = await this.login({ code, provider: state });

          if (token) {
            sessionStorage.setItem("token", token);
            console.log("Token stored in sessionStorage:", token);
            this.$router.push('/color_index');
          } else {
            throw new Error("無法取得 Token，請重新嘗試");
          }
        } else {
          throw new Error("無效的登入提供者");
        }
      } catch (error) {
        console.error("登入失敗:", error);

        if (error.message.includes("登入提供者")) {
          this.errorMessage = "無效的登入提供者，請重新嘗試。";
        } else if (error.response && error.response.status === 500) {
          this.errorMessage = "服務器內部錯誤，請稍後再試。";
        } else {
          this.errorMessage = "登入失敗，請重新嘗試。";
        }

        if (error.response) {
          console.error("服務器回應:", error.response.data);
        }
      } finally {
        this.loading = false;
      }
    },
  },
  mounted() {
    const token = sessionStorage.getItem('token');
    console.log('Token in Callback.vue:', token);

    if (!token) {
      console.log('未取得 Token，處理 OAuth 回應');
      this.handleCallback(); // 僅在無 Token 時呼叫 OAuth 回應處理函數
    } else {
      console.log('已有 Token，跳轉至 color_index');
      this.$router.push('/color_index');
    }
  },
};
</script>

<style scoped>
.error {
  color: red;
  font-weight: bold;
}
</style>
