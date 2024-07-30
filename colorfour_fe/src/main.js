import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import Toast from "vue-toastification";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.js";
import "vue-toastification/dist/index.css";

axios.defaults.baseURL = process.env.VUE_APP_NGROK_URL;

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const toastOptions = {};

const app = createApp(App);

app.use(store).use(router).use(Toast, toastOptions).mount("#app");
