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
      <h2 class="collect" >❤️ 我的收藏 ❤️</h2>
        <div v-if="collectedPosts.length">
          <div v-for="post in collectedPosts" :key="post.id" class="post mb-5">
            <div class="post-header d-flex justify-content-between align-items-center">
              <div class="post-userinfo d-flex align-items-center">
                <img src="https://picsum.photos/25" alt="User Avatar" class="post-avatar rounded-circle" />
                <span class="post-username ms-2">{{ post.username }}</span>
              </div>

              <div class="more-options position-relative">
                <svg
                  aria-label="更多選項"
                  class="change"
                  fill="currentColor"
                  height="24"
                  role="img"
                  viewBox="0 0 24 24"
                  width="24"
                  @click="toggleDropdown"
                >
                  <title>更多選項</title>
                  <circle cx="12" cy="12" r="1.5"></circle>
                  <circle cx="6" cy="12" r="1.5"></circle>
                  <circle cx="18" cy="12" r="1.5"></circle>
                </svg>
                <ul class="dropdown-menu position-absolute">
                  <li><a href="#" @click="removePost(post)">移除收藏</a></li>
                </ul>
              </div>
            </div>

            <div class="slider_container1 mt-3">
              <img :src="post.image" class="l_photo img-fluid" />
            </div>

            <ul class="prot mt-3">
              <li>{{ post.description }}</li>
              <li>{{ post.hashtags }}</li>
            </ul>

            <div class="post-time-location d-flex justify-content-left mt-2">
              <span class="post-location">地點：{{ post.location }}</span>
              <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
              <span class="post-time">時間：{{ post.time }}</span>
            </div>

            <div class="post-actions mt-3 d-flex justify-content-left">
              <button @click="likePost(post)" class="like-button btn btn-outline-primary">讚</button>
              <span>{{ post.likes }}</span>
              <button @click="toggleCommentBox" class="comment-button btn btn-outline-secondary">留言</button>
              <span>{{ post.comments }}</span>
            </div>

            <div class="comment-section mt-3">
              <textarea v-model="post.newComment" class="form-control mb-2" placeholder="請輸入留言..."></textarea>
              <button @click="submitComment(post)" class="btn btn-primary">提交留言</button>
            </div>
          </div>
        </div>
        <p v-else class="collect-null" >尚未收藏任何貼文</p>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters(['collectedPosts']),
  },
  methods: {
  ...mapActions(['removeFromCollection']),
  
  toggleDropdown(event) {
    const dropdownMenu = event.currentTarget.nextElementSibling;
    dropdownMenu.classList.toggle("show");
  },
  
  toggleCommentBox(event) {
    const commentBox = event.currentTarget.parentElement.nextElementSibling;
    commentBox.style.display =
      commentBox.style.display === "none" || !commentBox.style.display
        ? "block"
        : "none";
  },

  likePost(post) {
    post.likes++;
  },

  submitComment(post) {
    if (post.newComment.trim()) {
      post.comments++;
      post.newComment = "";
    }
  },

  removePost(post) {
    this.removeFromCollection(post); // 直接调用 Vuex 的 action
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
