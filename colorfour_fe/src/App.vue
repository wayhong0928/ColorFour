<template>
  <div id="app">
    <Header />
    <main>
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import { mapActions } from "vuex";

export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
  created() {
    this.initializeAuth();
  },
  methods: {
    ...mapActions("auth", ["initializeAuth"]),
  },
};
</script>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap");
  @import url("https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800&display=swap");

  :root {
    --primary-bg-color: #ffffff;
    --header-footer-bg-color: #e7d8c9;
    --divider-color: #ccc;
    --primary-text-color: #b2967d;
    --button-bg-color: #e6b5ae;
    --button-hover-bg-color: #d9a68c;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Noto Sans TC", "Noto Sans", sans-serif;
    font-weight: 500;
  }

  html,
  body {
    width: 100%;
    min-height: 100%;
  }

  body {
    display: flex;
    flex-direction: column;
    background-color: var(--primary-bg-color);
    padding-top: 70px;
    padding-bottom: 70px;
  }

  main {
    width: 90%;
    margin: 50px auto;
    position: relative;
    flex: 1;
  }

  .btn-main {
    background-color: var(--button-bg-color) !important;
    border-color: var(--button-bg-color);
    border-radius: 20px;
    padding: 5px 10px;
    text-decoration: none;
    color: #fff;
    display: inline-block;
    font-size: 16px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.3s, border-color 0.3s;
  }

  .btn-main:hover {
    background-color: var(--button-hover-bg-color);
    border-color: var(--button-hover-bg-color);
  }
</style>
