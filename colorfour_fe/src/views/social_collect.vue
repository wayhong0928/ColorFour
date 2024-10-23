<template>
  <div>
    <div id="header"></div>
    <main class="main-content container">
      <div class="left-sidebar">
        <div class="icon-search">
          <img src="@/assets/img/search_icon.png" alt="Search Icon" />
          <input type="text" placeholder="search" />
        </div>

        <div class="icon-link">
          <router-link to="social_index">
            <img src="@/assets/img/social_home_icon.png" alt="Home Icon" />
            <span>社群平台首頁</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_collect">
            <img src="@/assets/img/like_icon.png" alt="Saved Posts Icon" />
            <span>收藏貼文</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_follow_list">
            <img src="@/assets/img/followers_icon.png" alt="Overview Icon" />
            <span>追蹤總覽</span>
          </router-link>
        </div>
      </div>

      <div id="saved-posts-container" class="content">
        <h2 class="collect">我的收藏</h2>
        <div v-if="collectedPosts.length">
          <div v-for="post in collectedPosts" :key="post.id" class="post mb-5">
            <div class="post-header d-flex justify-content-between align-items-center">
              <div class="post-userinfo d-flex align-items-center">
                <img src="https://picsum.photos/25" alt="User Avatar" class="post-avatar rounded-circle" />
                <span class="post-username ms-2">{{ post.username }}</span>
              </div>
              <button
                @click="handleToggleFollow(post)"
                :class="{ 'btn-primary': isFollowing(post.username), 'btn-outline-primary': !isFollowing(post.username) }"
              >
                {{ isFollowing(post.username) ? "已追蹤" : "追蹤" }}
              </button>
            </div>
          </div>
        </div>
        <p v-else class="collect-null">尚未收藏任何貼文</p>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        collectedPosts: [],
      };
    },
    mounted() {
      this.loadCollectedPosts();
    },
    methods: {
      async loadCollectedPosts() {
        try {
          const response = await this.$axios.get("/api/posts/bookmarked/");
          this.collectedPosts = response.data;
        } catch (error) {
          console.error("無法載入收藏的貼文：", error);
        }
      },
      async handleToggleFollow(post) {
        try {
          await this.$axios.post(`/api/followers/toggle/`, { user: post.user_id });
          alert("追蹤狀態已更新！");
        } catch (error) {
          console.error("無法更新追蹤狀態：", error);
        }
      },
      isFollowing(username) {
        // 判斷是否已追蹤的邏輯，可依據實際需求調整
        return this.collectedPosts.some((post) => post.username === username);
      },
    },
  };
</script>

<style scoped>
  .main-content {
    width: 90%;
    position: relative;
    display: flex;
    flex-direction: column;
  }

  .follow-button {
    margin-right: 20px;
  }

  .post {
    width: 100%;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    max-width: 600px;
    background-color: #fff;
    color: rgb(8, 8, 8);
    text-align: left;
  }

  .post-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }

  .post-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .post-username {
    font-size: 1.2em;
    padding: 10px;
  }

  .post-userinfo {
    display: flex;
    align-items: center;
  }

  .more-options {
    position: relative;
  }

  .more-options svg {
    cursor: pointer;
  }

  .dropdown-menu {
    display: none;
    position: absolute;
    right: 0;
    top: 30px;
    background: white;
    border: 1px solid #dbdbdb;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 3px;
    overflow: hidden;
    z-index: 1;
    white-space: nowrap;
  }

  .dropdown-menu.show {
    display: block;
  }

  .dropdown-menu li {
    list-style: none;
  }

  .dropdown-menu li a {
    display: block;
    padding: 10px 20px;
    text-decoration: none;
    color: black;
  }

  .dropdown-menu li a:hover {
    background-color: #f0f0f0;
  }

  .post img {
    display: block;
    margin: 0 auto;
  }

  .prot {
    list-style: none;
    padding: 0;
    text-align: left;
    margin-bottom: 20px;
    margin: 10px 0;
  }

  .prot li {
    margin: 10px 0;
  }

  .post-actions {
    display: flex;
    justify-content: flex-start;
    gap: 10px;
    margin-top: 20px;
    align-items: center;
  }

  .post-actions button {
    background-color: #f0a9a9;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    color: white;
  }

  .post-actions button:hover {
    background-color: #e09393;
  }

  .slider_container1 img {
    max-width: 100%;
    border-radius: 8px;
  }

  .comment-section {
    display: none;
    margin-top: 10px;
  }

  .comment-section textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
  }

  .comment-section button {
    margin-top: 10px;
  }

  .comment-section button {
    background-color: #f0a9a9;
    color: white; /* 白色文字 */
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .comment-section button:hover {
    background-color: #e09393; /* 當鼠標懸停時，顏色變深 */
  }

  .comment-avatar {
    width: 40px; /* 增加頭像大小 */
    height: 40px; /* 同樣增加高度來匹配寬度 */
    border-radius: 50%;
    margin-right: 10px; /* 調整頭像和文字之間的距離 */
  }

  .comment-content {
    display: flex;
    flex-direction: row; /* 確保是水平排列 */
    align-items: flex-start; /* 頭像和文字對齊 */
    justify-content: flex-start; /* 確保所有內容靠左 */
    text-align: left; /* 留言內容靠左對齊 */
    margin-bottom: 10px; /* 調整上下間距 */
    width: 100%; /* 確保內容不溢出 */
  }

  .comment-content div {
    flex: 1; /* 讓留言內容占據剩餘空間 */
  }

  .comment-text {
    text-align: left; /* 留言文字靠左對齊 */
    margin: 0; /* 去掉多餘的上下間距 */
    white-space: pre-wrap; /* 保持換行格式 */
  }

  .left-sidebar {
    width: 200px;
    padding: 20px;
    position: fixed;
    top: 70px;
    left: 0;
    height: calc(100% - 120px);
    background-color: #f0f0f0;
    overflow-y: auto;
  }

  .collect {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    background-color: var(--primary-bg-color);
    color: #917b56;
    margin-bottom: 30px;
  }

  .collect-null {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    background-color: var(--primary-bg-color);
    font-size: 20px;
    color: var(--primary-text-color);
  }

  @media screen and (max-width: 800px) {
    .slider {
      margin: 20px auto;
    }

    .slide img {
      border-radius: 20px;
    }

    .post {
      padding: 10px;
      margin: 10px 0;
      border-radius: 20px;
    }

    .post-actions button {
      padding: 5px 10px;
    }
  }

  /* 确保左侧边栏在大屏幕时显示 */
  .left-sidebar {
    width: 200px;
    background-color: #f0f0f0;
    padding: 20px;
    position: fixed;
    top: 70px;
    left: 0;
    height: calc(100% - 120px);
    overflow-y: auto;
    z-index: 10;
    transition: all 0.3s ease;
  }

  .left-sidebar .icon-search,
  .left-sidebar .icon-link {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
  }

  .left-sidebar .icon-search img,
  .left-sidebar .icon-link img {
    margin-right: 10px;
    width: 30px;
    height: 30px;
    transition: all 0.3s ease;
  }

  .left-sidebar .icon-search input {
    flex: 1;
  }

  .left-sidebar .icon-link a {
    text-decoration: none;
    color: var(--primary-text-color);
    font-weight: 600;
    transition: all 0.3s ease;
  }

  /* 小屏幕样式 */
  @media (max-width: 768px) {
    .left-sidebar {
      width: 100%;
      position: fixed;
      top: 60px;
      left: 0;
      height: 60px;
      display: flex;
      justify-content: space-around;
      padding: 15px;
      background-color: var(--header-footer-bg-color);
    }

    .main-content {
      margin-top: 90px;
    }

    .left-sidebar .icon-search {
      display: none; /* 隐藏搜索栏位 */
    }

    .left-sidebar .icon-link {
      flex-direction: column;
      align-items: center;
      margin-bottom: 0;
    }

    .left-sidebar .icon-link span {
      display: none; /* 隐藏文字 */
    }

    .left-sidebar .icon-link img {
      margin-right: 0;
      width: 40px;
      height: 40px;
    }
  }

  .left-sidebar .icon-search input {
    width: 100px; /* 设置搜索框的宽度 */
    height: 30px; /* 设置搜索框的高度 */
    padding: 5px; /* 调整内边距 */
    font-size: 14px; /* 调整字体大小 */
    border-radius: 10px; /* 调整圆角 */
    border: 1px solid #ccc; /* 设置边框 */
  }

  /* 在小屏幕时也可以相应调整搜索框大小 */
  @media (max-width: 768px) {
    .left-sidebar .icon-search input {
      width: 100px; /* 调整小屏幕时的宽度 */
      height: 25px; /* 调整小屏幕时的高度 */
      font-size: 12px; /* 调整小屏幕时的字体大小 */
    }
  }
</style>
