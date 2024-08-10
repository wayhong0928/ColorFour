import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Login from "@/views/Login.vue";
import Error404 from '@/views/Error404.vue';
import color_index from "@/views/color_index.vue";
import color_detail from "@/views/color_detail_1.vue";
import color_detail_2 from "@/views/color_detail_2.vue";
import color_detail_3 from "@/views/color_detail_3.vue";
import color_detail_4 from "@/views/color_detail_4.vue";
import color_test from "@/views/color_test.vue";
import closet_index from "../views/closet_index.vue";
import closet_detail from "../views/closet_detail.vue";
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
    path: "/color_index",
    name: "color_index",
    component: color_index,
  },
  {
    path: "/color_detail_1",
    name: "color_detail",
    component: color_detail,
  },
  {
    path: "/color_detail_2",
    name: "color_detail_2",
    component: color_detail_2,
  },
  {
    path: "/color_detail_3",
    name: "color_detail_3",
    component: color_detail_3,
  },
  {
    path: "/color_detail_4",
    name: "color_detail_4",
    component: color_detail_4,
  },
  {
    path: "/color_test",
    name: "color_test",
    component: color_test,
  },
  {
    path: "/closet_index",
    name: "closet_index",
    component: () => import("../views/closet_index.vue"),
  },
  {
    path: "/closet_detail/:id",
    name: "closet_detail",
    component: () => import("../views/closet_detail.vue"),
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
