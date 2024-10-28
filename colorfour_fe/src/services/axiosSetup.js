import axios from "axios";
import store from "../store";
import router from "../router";

// 設定最大重試次數與間隔時間
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 1000; // 1 秒

// 延遲函數，用於重試間隔
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export const setupInterceptors = () => {
  axios.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      if (error.response.status === 401 && !originalRequest._retryCount) {
        originalRequest._retryCount = 0;
      }

      // 若是未授權錯誤 (401) 且未超過重試次數限制
      if (error.response.status === 401 && originalRequest._retryCount < MAX_RETRIES) {
        originalRequest._retryCount += 1;
        await delay(RETRY_DELAY_MS); // 等待一段時間再重試

        try {
          const newToken = await store.dispatch("auth/refreshToken");
          if (newToken) {
            originalRequest.headers["Authorization"] = `Bearer ${newToken}`;
            return axios(originalRequest); // 重試請求
          }
        } catch (refreshError) {
          console.error("Refresh token 失敗：", refreshError);
          await store.dispatch("auth/logout");
          router.push("/login");
          return Promise.reject(refreshError);
        }
      }

      // 若超過重試次數限制，登出並導向登入頁面
      if (originalRequest._retryCount >= MAX_RETRIES) {
        console.warn("重試次數達到上限，登出使用者。");
        await store.dispatch("auth/logout");
        router.push("/login");
      }

      return Promise.reject(error);
    }
  );
};
