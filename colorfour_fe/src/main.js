import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import Toast from "vue-toastification";
import { setupInterceptors } from "./services/axiosSetup";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.js";
import "vue-toastification/dist/index.css";

axios.defaults.baseURL = process.env.VUE_APP_BACKEND_URL;
axios.defaults.headers.common["Content-Type"] = "application/json";

setupInterceptors();
store.dispatch("auth/initializeAuth");

const toastOptions = {};

const app = createApp(App);
app.use(store).use(router).use(Toast, toastOptions);

app.mount("#app");
