<template>
  <header class="bg-light fixed-top header">
    <div class="container d-flex justify-content-between align-items-center" style="max-width: 1200px">
      <router-link to="/">
        <img src="@/assets/img/colorfour_text.png" alt="colorfour" class="nav-text mx-auto" />
      </router-link>
      <button class="btn" @click="toggleSidebar">
        <img src="@/assets/img/menu_button_icon.png" class="zoom" style="width: 45px; height: 50px" />
      </button>
    </div>
    <aside class="sidebar bg-light p-3" :class="{ show: isSidebarVisible }">
      <img src="https://picsum.photos/100/100?random=1" alt="會員照片" class="member-photo mx-auto d-block mb-3" />
      <hr class="sidebar-divider" />
      <div class="page-links">
        <router-link v-for="link in sidebarLinks" :key="link.text" class="d-block mb-2 text-dark" :to="link.path">
          {{ link.text }}
        </router-link>
      </div>
    </aside>
  </header>
</template>

<script>
  export default {
    data() {
      return {
        isSidebarVisible: false,
        sidebarLinks: [
          { text: "我的氣色", path: "/color_index" },
          { text: "線上衣櫃", path: "/closet_index" },
          { text: "穿搭建議師", path: "/suggest_index" },
          { text: "採購建議師", path: "/buy_index" },
          { text: "社群互動", path: "/social_index" },
          { text: "穿搭日程", path: "/todo_index" },
          { text: "會員管理", path: "/user_profile" },
          { text: "設定", path: "/user_setting" },
          { text: "登入", path: "/login" },
          { text: "關於我們", path: "/about" },
          { text: "聯繫客服", path: "/contact" },
        ],
      };
    },
    methods: {
      toggleSidebar() {
        this.isSidebarVisible = !this.isSidebarVisible;
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
