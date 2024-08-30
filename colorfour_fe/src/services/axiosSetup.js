import axios from "axios";
import store from "../store";

export const setupInterceptors = () => {
  let isRefreshing = false;
  let failedQueue = [];

  const processQueue = (error, token = null) => {
    failedQueue.forEach((prom) => {
      if (token) {
        prom.resolve(token);
      } else {
        prom.reject(error);
      }
    });

    failedQueue = [];
  };

  axios.interceptors.request.use(
    (config) => {
      const token = store.getters["auth/token"];
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  axios.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      if (error.response && error.response.status === 401 && !originalRequest._retry) {
        if (isRefreshing) {
          return new Promise(function (resolve, reject) {
            failedQueue.push({ resolve, reject });
          })
            .then((token) => {
              originalRequest.headers["Authorization"] = "Bearer " + token;
              return axios(originalRequest);
            })
            .catch((err) => {
              return Promise.reject(err);
            });
        }

        originalRequest._retry = true;
        isRefreshing = true;

        try {
          const token = await store.dispatch("auth/refreshToken");
          processQueue(null, token);
          isRefreshing = false;

          originalRequest.headers.Authorization = `Bearer ${token}`;
          return axios(originalRequest);
        } catch (err) {
          processQueue(err, null);
          isRefreshing = false;
          await store.dispatch("auth/logout");
          router.push("/");
          return Promise.reject(err);
        }
      }

      return Promise.reject(error);
    }
  );
};
