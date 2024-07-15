<template>
  <button class="medium_button btn_p08_user_loginType" id="lineLoginBtn" @click="openLineLogin">
    <img src="./assets/btn_login_base.png" alt="LINE Logo">
  </button>
  <div>
    <!-- Toast 容器 -->
    <b-toaster name="b-toaster-top-center"></b-toaster>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { API_URL } from "@/config";
import qs from 'qs';
import { useToast } from 'vue-toastification';
import 'vue-toastification/dist/index.css';

// 為實際Channel ID 值
const client_id = ref('2005742580');

// 實際Line developer 設定的重新導向網址
const redirect_uri = ref('https://upward-gorgeous-bedbug.ngrok-free.app/line/login');

// 為實際Channel Secret 值
const client_secret = ref('d6358d95aafd5cef3ca2f5bca5e4244a');

// 使用 Vue Toastification
const toast = useToast();

// 使用者點擊登入按鈕觸發
function openLineLogin() {
  // 根據指定的 client_id、redirect_uri、scope 等參數組合出一個 LINE 登入的連結
  let link = `https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=${client_id.value}&redirect_uri=${redirect_uri.value}&state=login&scope=openid%20profile&bot_prompt=aggressive`;

  // 將頁面重新導向到該連結
  window.location.href = link;
}

// 顯示 toast 訊息的函數
function showHomeToast() {
  toast('登入成功', {
    position: 'top-center',
    timeout: 3000, // 3秒后自动消失
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: false,
    closeButton: 'button',
    icon: true,
    rtl: false
  });
}

// 检查 URL 中的登录结果标记
onMounted(() => {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const loginResult = urlParams.get('loginResult');

  if (loginResult === 'success') {
    showHomeToast();
  } else if (loginResult === 'failure') {
    toast.error('登入失敗，請重試', {
      position: 'top-center',
      timeout: 3000,
      closeOnClick: true,
      pauseOnFocusLoss: true,
      pauseOnHover: true,
      draggable: true,
      draggablePercent: 0.6,
      showCloseButtonOnHover: false,
      hideProgressBar: false,
      closeButton: 'button',
      icon: true,
      rtl: false
    });
  }
});
</script>

<style scoped>
.medium_button {
  margin: 0;
  padding: 0;
  border: none;
  background: none;
  cursor: pointer;
}
</style>
