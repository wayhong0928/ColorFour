import axios from "axios";

const BACKEND_URL = process.env.VUE_APP_BACKEND_URL;

export default {
  namespaced: true,
  state: {
    token: sessionStorage.getItem("my-app-auth") || "",
    refreshToken: sessionStorage.getItem("my-refresh-token") || "",
    user: null,
    loginProvider: null,
    isAuthenticated: !!sessionStorage.getItem("my-app-auth"),
    isGoogleLinked: false,
    isLineLinked: false,
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
      sessionStorage.setItem("isAuthenticated", true);
      sessionStorage.setItem("my-app-auth", token);
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
      sessionStorage.removeItem("my-app-auth");
      sessionStorage.removeItem("my-refresh-token");
      sessionStorage.removeItem("loginProvider");
      sessionStorage.removeItem("isAuthenticated");
      axios.defaults.headers.common["Authorization"] = '';
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
      const isAuthenticated = sessionStorage.getItem("isAuthenticated") === "true";
      if (token && isAuthenticated) {
        commit("setToken", token);
        axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
        try {
          await dispatch("fetchUserProfile");
        } catch (error) {
          console.error("Failed to fetch user info:", error);
          if (error.response && error.response.status === 401) {
            await dispatch("refreshToken");
          } else {
            commit("clearAuthData");
          }
        }
      } else {
        commit("clearAuthData");
      }
    },
    async login({ commit, dispatch }, { code, provider }) {
      let url;
      if (provider === "google") {
        url = `${BACKEND_URL}/member/login/google/`;
      } else if (provider === "line") {
        url = `${BACKEND_URL}/member/login/line/`;
      } else {
        throw new Error("Unknown provider");
      }
      try {
        const response = await axios.post(url, { code });
        console.log("API Response:", response.data);

        if (!response.data.access || !response.data.refresh) {
          throw new Error("Token not received");
        }

        commit("setToken", response.data.access);
        commit("setRefreshToken", response.data.refresh);
        commit("setLoginProvider", provider);
        sessionStorage.setItem("isAuthenticated", true);

        if (provider === "google") {
          commit("setIsGoogleLinked", true);
        } else if (provider === "line") {
          commit("setIsLineLinked", true);
        }

        if (provider === "line" && response.data.user) {
          const encodedName = encodeURIComponent(response.data.user.name);
          response.data.user.name = encodedName;
          console.log("Encoded Username:", encodedName);
        }

        axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`;

        await dispatch("fetchUserProfile");

        console.log("Token stored in sessionStorage:", sessionStorage.getItem("my-app-auth"));
        console.log("Refresh Token stored in sessionStorage:", sessionStorage.getItem("my-refresh-token"));
        console.log("Login Provider:", provider);
      } catch (error) {
        console.error("Login failed:", error);
        throw error;
      }
    },
    async refreshToken({ commit, state }) {
      if (!state.refreshToken) {
        commit("clearAuthData");
        return null;
      }

      try {
        const response = await axios.post(`${BACKEND_URL}/api/token/refresh/`, { refresh: state.refreshToken });
        const newToken = response.data.access;
        commit("setToken", newToken);
        sessionStorage.setItem("my-app-auth", newToken);
        axios.defaults.headers.common["Authorization"] = `Bearer ${newToken}`;
        return newToken;
      } catch (error) {
        commit("clearAuthData");
        console.error("Token refresh failed:", error);
        throw error;
      }
    },
    logout({ commit }) {
      commit("clearAuthData");
      axios.defaults.headers.common["Authorization"] = '';
    },
    async fetchUserProfile({ commit, state }) {
      try {
        const response = await axios.get(`${BACKEND_URL}/dj-rest-auth/user/`);
        commit("setUser", response.data);

        const isGoogleLinked =
          response.data.is_google_linked !== undefined ? response.data.is_google_linked : state.loginProvider === "google";
        const isLineLinked =
          response.data.is_line_linked !== undefined ? response.data.is_line_linked : state.loginProvider === "line";

        commit("setIsGoogleLinked", isGoogleLinked);
        commit("setIsLineLinked", isLineLinked);

        console.log("User profile fetched:", response.data);
        console.log("isGoogleLinked:", isGoogleLinked);
        console.log("isLineLinked:", isLineLinked);
        console.log("Current loginProvider:", state.loginProvider);
      } catch (error) {
        console.error("Failed to fetch user profile:", error);
        throw error;
      }
    },
    async updateUserProfile({ commit }, userData) {
      try {
        const response = await axios.patch(`${BACKEND_URL}/dj-rest-auth/user/`, userData);
        commit("setUser", response.data);
      } catch (error) {
        console.error("Failed to update user profile:", error);
        throw error;
      }
    },
    async linkSocialAccount({ dispatch }, provider) {
      console.log("開始連結帳號:", provider);
      try {
        const authWindow = window.open(
          `${process.env.VUE_APP_BACKEND_URL}/member/login/${provider}/`,
          "_blank",
          "width=600,height=600"
        );

        const messageHandler = async (event) => {
          if (event.origin !== process.env.VUE_APP_BACKEND_URL) return;

          if (event.data.type === "social_auth_success") {
            window.removeEventListener("message", messageHandler);
            authWindow.close();

            await axios.post(`${process.env.VUE_APP_BACKEND_URL}/member/auth-providers/`, {
              provider: provider,
              code: event.data.code,
            });

            await dispatch("fetchUserProfile");
            console.log("帳號連結成功");
          }
        };

        window.addEventListener("message", messageHandler);
      } catch (error) {
        console.error("連結帳號失敗:", error);
        throw error;
      }
    },
    async unlinkSocialAccount({ dispatch }, provider) {
      try {
        await axios.post(`${BACKEND_URL}/member/unlink-social-account/`, { provider });
        await dispatch("fetchUserProfile");
      } catch (error) {
        console.error("Failed to unlink social account:", error);
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
    loginProvider: (state) => state.loginProvider,
    isGoogleLinked: (state) => state.isGoogleLinked,
    isLineLinked: (state) => state.isLineLinked,
  },
};
