<template>
  <div>Logging you in...</div>
</template>

<script>
  export default {
    async created() {
      console.log("Current URL:", window.location.href);

      const code = new URL(window.location.href).searchParams.get("code");

      if (code) {
        console.log("Authorization code found:", code);
        try {
          const provider = window.location.href.includes("google") ? "google" : "line";
          console.log("Using provider:", provider);

          const response = await this.$axios.post(`${process.env.VUE_APP_NGROK_URL}/accounts/${provider}/login/callback/`, {
            code: code,
            redirect_uri: process.env.VUE_APP_NGROK_URL + `/accounts/${provider}/login/callback/`,
          });

          console.log("Response received:", response.data);

          localStorage.setItem("token", response.data.access_token);
          console.log("Access token stored:", response.data.access_token);

          this.$router.push({ name: "home" });
        } catch (error) {
          console.error("Login failed:", error);
          console.error("Error details:", error.response ? error.response.data : "No response from server");
        }
      } else {
        console.error("Authorization code not found");
      }
    },
  };
</script>
