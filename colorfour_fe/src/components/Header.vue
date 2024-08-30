<template>
  <header class="bg-light fixed-top header">
    <div class="container d-flex justify-content-between align-items-center" style="max-width: 1200px">
      <router-link to="/">
        <img :src="logo" alt="colorfour" class="nav-text mx-auto" />
      </router-link>
      <button class="btn" @click="toggleSidebar">
        <img :src="menuIcon" class="zoom" style="width: 45px; height: 50px" />
      </button>
    </div>
    <aside class="sidebar bg-light p-3" :class="{ show: isSidebarVisible }">
      <img :src="memberPhoto" alt="會員照片" class="member-photo mx-auto d-block mb-3" />
      <hr class="sidebar-divider" />
      <div class="page-links">
        <router-link
          v-for="link in sidebarLinks"
          :key="link.text"
          class="d-block mb-2 text-dark"
          :to="link.path"
          @click="link.action ? link.action() : null"
        >
          {{ link.text }}
        </router-link>
      </div>
    </aside>
  </header>
</template>

<script>
  import { mapGetters } from "vuex";

  export default {
    data() {
      return {
        isSidebarVisible: false,
      };
    },
    computed: {
      ...mapGetters("auth", ["isAuthenticated"]),
      sidebarLinks() {
        console.log("Current isAuthenticated:", this.isAuthenticated);

        return [
          { text: "我的氣色", path: "/color_index" },
          { text: "線上衣櫃", path: "/closet_index" },
          { text: "穿搭建議師", path: "/suggest_index" },
          { text: "採購建議師", path: "/buy_index" },
          { text: "社群互動", path: "/social_index" },
          { text: "穿搭日程", path: "/todo_index" },
          ...(this.isAuthenticated
            ? [
                { text: "會員管理", path: "/user_profile" },
                { text: "設定", path: "/user_setting" },
                { text: "登出", path: "#", action: this.logout },
              ]
            : [{ text: "登入", path: "/login" }]),
          { text: "關於我們", path: "/about" },
          { text: "聯繫客服", path: "/contact" },
        ];
      },
      filteredSidebarLinks() {
        return this.sidebarLinks.filter((link) => link.path);
      },
      logo() {
        return require("@/assets/img/colorfour_text.png");
      },
      menuIcon() {
        return require("@/assets/img/menu_button_icon.png");
      },
      memberPhoto() {
        return "https://picsum.photos/100/100?random=1";
      },
    },
    methods: {
      toggleSidebar() {
        this.isSidebarVisible = !this.isSidebarVisible;
      },
      logout() {
        this.$store.dispatch("auth/logout").then(() => {
          this.$router.push("/login");
          this.isSidebarVisible = false;
        });
      },
    },
  };
</script>

<style scoped>
  .header {
    height: 70px;
    background-color: var(--header-footer-bg-color) !important;
  }

  .nav-text {
    height: 50px;
    margin: 0 auto;
  }

  .member-photo {
    width: 100px;
    height: 100px;
    border-radius: 50%;
  }

  .sidebar-divider {
    border: 0;
    height: 1px;
    margin: 20px 0;
    background-color: var(--divider-color);
  }

  .sidebar.show {
    display: block;
  }

  .sidebar {
    display: none;
    position: fixed;
    top: 70px;
    right: 0;
    height: calc(100% - 70px);
    overflow-y: auto;
    z-index: 10;
  }
</style>
