import axios from "axios";

const BACKEND_URL = process.env.VUE_APP_BACKEND_URL;

export default {
  namespaced: true,
  state: {
    token: sessionStorage.getItem("my-app-auth") || "",
    refreshToken: sessionStorage.getItem("my-refresh-token") || "",
    user: null,
    isAuthenticated: !!sessionStorage.getItem("my-app-auth"),
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
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
      sessionStorage.removeItem("my-app-auth");
      sessionStorage.removeItem("my-refresh-token");
    },
  },

  actions: {
    async initializeAuth({ commit }) {
      const token = sessionStorage.getItem("my-app-auth");
      if (token) {
        commit("setToken", token);
        try {
          const userInfo = await axios.get(`${BACKEND_URL}/dj-rest-auth/user/`);
          commit("setUser", userInfo.data);
        } catch (error) {
          console.error("Failed to fetch user info:", error);
          commit("clearAuthData");
        }
      } else {
        commit("clearAuthData");
      }
    },
    async login({ commit }, { code, provider }) {
      let url;
      if (provider === "google") {
        url = `${BACKEND_URL}/dj-rest-auth/google/`;
      } else if (provider === "line") {
        url = `${BACKEND_URL}/dj-rest-auth/line/`;
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

        axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`;

        const userInfo = await axios.get(`${BACKEND_URL}/dj-rest-auth/user/`);
        commit("setUser", userInfo.data);

        console.log("Token stored in sessionStorage:", sessionStorage.getItem("my-app-auth"));
        console.log("Refresh Token stored in sessionStorage:", sessionStorage.getItem("my-refresh-token"));
        console.log("User info:", userInfo.data);
      } catch (error) {
        console.error("Login failed:", error);
        // Consider adding user feedback here, e.g., via a notification system.
      }
    },
    async refreshToken({ commit, state }) {
      if (!state.refreshToken) {
        console.error("No refresh token available. Logging out.");
        commit("clearAuthData");
        return;
      }

      try {
        const response = await axios.post(`${BACKEND_URL}/api/token/refresh/`, {
          refresh: state.refreshToken,
        });
        commit("setToken", response.data.access);
        axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`;
        return response.data.access;
      } catch (error) {
        console.error("Token refresh failed:", error);

        if (error.response && error.response.status === 401) {
          console.error("Unauthorized - Refresh token is invalid. Logging out.");
          commit("clearAuthData");
        }

        throw error;
      }
    },

    logout({ commit }) {
      commit("clearAuthData");
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    user(state) {
      return state.user;
    },
  },
};
