import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Login from "@/views/Login.vue";
import Error404 from '@/views/Error404.vue';
import Callback from '@/views/Callback.vue';

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/Login",
    name: "Login",
    component: Login,
  },
  {
    path: '/:catchAll(.*)',
    name: 'Error404',
    component: Error404
  },
  {
    path: "/callback",
    name: "callback",
    component: Callback
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
