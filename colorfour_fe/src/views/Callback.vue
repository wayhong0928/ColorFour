<template>
  <div class="callback">
    <h1>Callback</h1>
    <p>Processing your login...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Callback",
  async created() {
    const code = new URLSearchParams(window.location.search).get('code');
    if (code) {
      try {
        const response = await axios.get(`${process.env.VUE_APP_API_URL}/accounts/google/login/callback?code=${code}`);
        const token = response.data.token;
        localStorage.setItem('token', token);
        this.$router.push('/'); // 跳轉回主頁面
      } catch (error) {
        console.error('Error fetching Google user info', error);
        this.$router.push('/login'); // 跳轉回登入頁面
      }
    }
  }
};
</script>

<style scoped>
.callback {
  padding: 20px;
}
</style>
