import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Login from "@/views/Login.vue";
import Error404 from "@/views/Error404.vue";
import Callback from '@/views/Callback.vue';

// Color 
import color_index from "@/views/color_index.vue";
import color_detail_1 from "@/views/color_detail_1.vue";
import color_detail_2 from "@/views/color_detail_2.vue";
import color_detail_3 from "@/views/color_detail_3.vue";
import color_detail_4 from "@/views/color_detail_4.vue";
import color_test from "@/views/color_test.vue";

// Closet
import closet_index from "@/views/closet_index.vue";
import closet_detail from "@/views/closet_detail.vue";
import closet_new from "@/views/closet_new.vue";
import closet_trash from "@/views/closet_trash.vue";

//Social
import social_index from "@/views/social_index.vue";
import user_profile from "@/views/user_profile.vue"
import social_collect from "@/views/social_collect.vue"
import post_new from "@/views/post_new.vue"
import post_edit from "@/views/post_edit.vue"
import social_follow_list from "@/views/social_follow_list.vue"


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
    path: "/color_index",
    name: "color_index",
    component: color_index,
  },
  {
    path: "/color_detail_1",
    name: "color_detail_1",
    component: color_detail_1,
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
    component: closet_index,
  },
  {
    path: "/closet_detail/:id",
    name: "closet_detail",
    component: closet_detail,
    props: true,
  },
  {
    path: "/closet_new",
    name: "closet_new",
    component: closet_new,
  },
  {
    path: "/closet_trash",
    name: "closet_trash",
    component: closet_trash,
  },
  {
    path: "/callback",
    name: "Callback",
    component: Callback,
  },
  {
    path: "/social_index",
    name: "social_index",
    component: social_index,
  },
  {
    path: "/user_profile",
    name: "user_profile",
    component: user_profile,
  },
  {
    path: "/social_collect",
    name: "social_collect",
    component: social_collect,
  },
  {
    path: "/post_new",
    name: "post_new",
    component: post_new,
  },
  {
    path: "/post_edit",
    name: "post_edit",
    component: post_edit,
  },
  {
    path: "/social_follow_list",
    name: "social_follow_list",
    component: social_follow_list,
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
