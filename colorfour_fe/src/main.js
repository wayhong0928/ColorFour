import { createApp } from 'vue'
import App from './App.vue'
<<<<<<< HEAD

createApp(App).mount('#app')
=======
import router from './router'
import store from './store'
import axios from 'axios'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'
import 'bootstrap/dist/css/bootstrap.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(store).use(router).use(bootstrap).mount('#app')
>>>>>>> upstream/main
