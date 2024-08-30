<template>
  <footer v-if="isAuthenticated" class="footer bg-light">
    <div class="container footer-container">
      <div class="footer-col">
        <router-link to="/">
          <img src="@/assets/img/house_icon.png" class="zoom" style="width: 50px; height: 50px" />
        </router-link>
        <router-link to="/suggest_index">
          <img src="@/assets/img/clothing_icon.png" class="zoom" style="width: 45px; height: 50px" />
        </router-link>
        <router-link to="/post_new">
          <img src="@/assets/img/new_post_icon.png" class="zoom" style="width: 50px; height: 50px" />
        </router-link>
        <router-link to="/closet_index">
          <img src="@/assets/img/closet_icon.png" class="zoom" style="width: 50px; height: 50px" />
        </router-link>
        <router-link to="/user_profile">
          <img src="@/assets/img/user_icon.png" class="zoom" style="width: 45px; height: 50px" />
        </router-link>
      </div>
    </div>
  </footer>
</template>

<script>
  import { mapGetters } from "vuex";

  export default {
    computed: {
      ...mapGetters("auth", ["isAuthenticated"]),
    },
  };
</script>

<style scoped>
  .footer {
    height: 70px;
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: var(--header-footer-bg-color) !important;
    color: white;
    padding: 10px 0;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
    z-index: 100;
    text-align: center;
  }

  .footer-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: center;
  }

  .footer-col {
    display: flex;
    justify-content: space-around;
    width: 100%;
  }

  .footer-col a {
    color: white;
    margin: 0 10px;
    text-decoration: none;
  }

  .footer-col a img {
    vertical-align: middle;
  }
</style>
