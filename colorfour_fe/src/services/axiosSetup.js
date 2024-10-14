import axios from "axios";
import store from "../store";
import router from "../router";

export const setupInterceptors = () => {
  axios.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        try {
          const newToken = await store.dispatch("auth/refreshToken");
          if (newToken) {
            originalRequest.headers["Authorization"] = `Bearer ${newToken}`;
            return axios(originalRequest);
          }
        } catch (refreshError) {
          await store.dispatch("auth/logout");
          router.push("/login");
        }
      }
      return Promise.reject(error);
    }
  );
};
