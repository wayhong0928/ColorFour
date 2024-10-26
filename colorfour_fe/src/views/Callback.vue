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
        const code = new URLSearchParams(window.location.search).get("code");
        const state = new URLSearchParams(window.location.search).get("state");
        console.log("code:", code, "state:", state);

        if (!code) {
          this.errorMessage = "無法取得驗證資訊，請重新嘗試。";
          this.loading = false;
          return;
        }

        try {
          await this.login({ code, provider: state });
          this.$router.push({ name: "home" });
        } catch (error) {
          console.error("登入失敗:", error);
          if (error.response && error.response.status === 500) {
            this.errorMessage = "服務器內部錯誤，請稍後再試。";
          } else if (error.message === "unknown login provider") {
            this.errorMessage = "無效的登入提供者，請重新嘗試。";
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
      this.handleCallback();
    },
  };
</script>

<style scoped>
  .error {
    color: red;
    font-weight: bold;
  }
</style>
