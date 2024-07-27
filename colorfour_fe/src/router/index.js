import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Login from "@/views/Login.vue";
import Error404 from "@/views/Error404.vue";
import closet_index from "../views/closet_index.vue";
import closet_detail from "../views/closet_detail.vue";

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
    path: "/:catchAll(.*)",
    name: "Error404",
    component: Error404,
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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
