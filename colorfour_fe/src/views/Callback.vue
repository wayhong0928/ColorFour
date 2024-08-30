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
      ...mapActions("auth", ["login", "refreshToken", "logout"]),
      async handleCallback() {
        const code = new URL(window.location.href).searchParams.get("code");
        const state = new URL(window.location.href).searchParams.get("state");

        console.log("OAuth Code:", code);
        console.log("OAuth State:", state);

        if (!code) {
          this.errorMessage = "未找到授權碼，請重新嘗試登入。";
          this.loading = false;
          return;
        }

        try {
          if (state === "google") {
            await this.login({ code, provider: 'google' });
            this.$router.push({ name: "home" });
          } else if (state === "line") {
            await this.login({ code, provider: 'line' });
            this.$router.push({ name: "home" });
          } else {
            throw new Error("未知的登入提供者");
          }
        } catch (error) {
          console.error("登入失敗:", error);
          this.errorMessage = "登入失敗，請重新嘗試。";
          if (error.response) {
            console.error("服務器回應:", error.response.data);
          }
        } finally {
          this.loading = false;
        }
      },
    },

    mounted() {
      this.handleCallback();
    },
  };
</script>
