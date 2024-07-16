<template>
  <div class="error-container">
    <h1>404 - 找不到頁面</h1>
    <p>您所尋找的頁面不存在。</p>
    <router-link to="/" class="btn-main">回到首頁</router-link>
  </div>
</template>

<script>
  export default {
    name: "Error404",
  };
</script>

<style scoped>
  .error-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    background-color: var(--primary-bg-color);
  }

  .error-container h1 {
    font-size: 2.5rem;
    color: var(--primary-text-color);
    margin-bottom: 1rem;
  }

  .error-container p {
    font-size: 1.5rem;
    color: var(--primary-text-color);
    margin-bottom: 2rem;
  }

  .btn-main {
    background-color: var(--button-bg-color) !important;
    border-color: var(--button-bg-color);
    border-radius: 20px;
    padding: 10px 20px;
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
