import axios from "axios";

const BACKEND_URL = process.env.VUE_APP_BACKEND_URL;

async function retryRequest(requestFunc, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await requestFunc();
    } catch (error) {
      if (i === retries - 1) throw error;
      console.warn(`重試第 ${i + 1} 次請求...`);
    }
  }
}

export default {
  namespaced: true,
  state: {
    token: sessionStorage.getItem("my-app-auth") || "",
    refreshToken: sessionStorage.getItem("my-refresh-token") || "",
    user: null,
    loginProvider: sessionStorage.getItem("loginProvider") || null,
    isAuthenticated: !!sessionStorage.getItem("my-app-auth"),
    isGoogleLinked: false,
    isLineLinked: false,
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
      sessionStorage.setItem("my-app-auth", token);
      console.log("Token:", token);
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    },
    setRefreshToken(state, refreshToken) {
      state.refreshToken = refreshToken;
      sessionStorage.setItem("my-refresh-token", refreshToken);
    },
    setUser(state, user) {
      state.user = user;
    },
    clearAuthData(state) {
      state.token = "";
      state.refreshToken = "";
      state.user = null;
      state.isAuthenticated = false;
      state.loginProvider = null;
      state.isGoogleLinked = false;
      state.isLineLinked = false;
      sessionStorage.clear();
      axios.defaults.headers.common["Authorization"] = "";
    },
    setLoginProvider(state, provider) {
      state.loginProvider = provider;
      sessionStorage.setItem("loginProvider", provider);
    },
    setIsGoogleLinked(state, isLinked) {
      state.isGoogleLinked = isLinked;
    },
    setIsLineLinked(state, isLinked) {
      state.isLineLinked = isLinked;
    },
  },
  actions: {
    async initializeAuth({ commit, dispatch }) {
      const token = sessionStorage.getItem("my-app-auth");
      if (token) {
        commit("setToken", token);
        try {
          await dispatch("fetchUserProfile");
        } catch (error) {
          console.error("Failed to fetch user profile:", error);
          if (error.response?.status === 401) {
            const newToken = await dispatch("refreshToken");
            if (!newToken) {
              commit("clearAuthData");
            }
          } else {
            commit("clearAuthData");
          }
        }
      } else {
        commit("clearAuthData");
      }
    },

    async login({ commit }, { code, provider }) {
      try {
        sessionStorage.removeItem("my-app-auth");
        sessionStorage.removeItem("my-refresh-token");

        console.log(`開始使用 ${provider} 進行登入，授權碼: ${code}`);

        const response = await retryRequest(() =>
          axios.post(
            `${BACKEND_URL}/member/login/${provider}/`,
            { code },
            {
              headers: { "Content-Type": "application/json" },
            }
          )
        );

        const { access, refresh } = response.data;

        if (!access || !refresh) {
          throw new Error("未取得有效的 access 或 refresh token");
        }

        commit("setToken", access);
        commit("setRefreshToken", refresh);
      } catch (error) {
        console.error("登入失敗:", error.response ? error.response.data : error.message);
        throw error;
      }
    },
    async refreshToken({ commit, state, dispatch }) {
      if (!state.refreshToken) {
        commit("clearAuthData");
        return null;
      }
      try {
        const response = await retryRequest(() =>
          axios.post(`${BACKEND_URL}/api/token/refresh/`, {
            refresh: state.refreshToken,
          })
        );
        const newToken = response.data.access;
        commit("setToken", newToken);
        return newToken;
      } catch (error) {
        console.error("Token 刷新失敗:", error);
        commit("clearAuthData");
        dispatch("logout");
        return null;
      }
    },
    logout({ commit }) {
      commit("clearAuthData");
      sessionStorage.clear();
      axios.defaults.headers.common["Cache-Control"] = "no-store";
      axios.defaults.headers.common["Pragma"] = "no-cache";

      // 清除快取與 Cookies
      document.cookie.split(";").forEach((cookie) => {
        const eqPos = cookie.indexOf("=");
        const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
      });

      // 解除 Service Workers 註冊
      if ("serviceWorker" in navigator) {
        navigator.serviceWorker.getRegistrations().then((registrations) => {
          registrations.forEach((registration) => registration.unregister());
        });
      }

      // 強制刷新頁面
      window.location.reload(true);
    },
    async fetchUserProfile({ commit }) {
      try {
        const response = await retryRequest(() =>
          axios.get(`${BACKEND_URL}/dj-rest-auth/user/`, {
            headers: { Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}` },
          })
        );
        const userData = response.data;
        commit("setUser", userData);
        commit("setIsGoogleLinked", userData.is_google_linked || false);
        commit("setIsLineLinked", userData.is_line_linked || false);
      } catch (error) {
        console.error("Failed to fetch user profile:", error);
        throw error;
      }
    },
    async linkSocialAccount({ dispatch }, provider) {
      try {
        const authWindow = window.open(`${BACKEND_URL}/member/login/${provider}/`, "_blank", "width=600,height=600");

        const messageHandler = async (event) => {
          if (event.origin !== BACKEND_URL) return;

          if (event.data.type === "social_auth_success") {
            authWindow.close();
            await dispatch("fetchUserProfile");
          }
        };

        window.addEventListener("message", messageHandler);
      } catch (error) {
        console.error("連結帳號失敗:", error);
        throw error;
      }
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    user(state) {
      return state.user;
    },
    loginProvider(state) {
      return state.loginProvider;
    },
    isGoogleLinked(state) {
      return state.isGoogleLinked;
    },
    isLineLinked(state) {
      return state.isLineLinked;
    },
  },
};
