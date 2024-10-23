<template>
  <div>
    <div id="header"></div>
    <main class="container">
      <div v-if="loading">
        <p>Loading...</p>
      </div>
      <div v-else-if="error">
        <p>{{ error }}</p>
      </div>
      <div v-else>
        <div class="row my-4">
          <!-- Profile information section -->
          <div class="col-6 d-flex justify-content-between align-items-center">
            <div>
              <img
                :src="user.photo_url || defaultProfileImage"
                alt="user profile image"
                class="rounded-circle"
                width="100"
                height="100"
              />
              <div>
                <h2>{{ user.nickname || "ColorFour User" }}</h2>
                <p>@{{ user.username || "ColorFourUser" }}</p>
                <p>{{ user.bio || "讓你的專屬穿搭造型師，給你點顏色瞧瞧！" }}</p>
              </div>
            </div>
          </div>
          <div class="col-6">
            <!-- Stats section -->
            <div class="row my-4">
              <div class="col-12">
                <div class="d-flex flex-column align-items-start position-relative">
                  <p>{{ user.gender || "男性/女性" }}</p>
                  <p @click="goToSocialFollowList" style="cursor: pointer">
                    {{ user.posts_count || 0 }} 貼文 | {{ user.followers_count || 0 }} 粉絲 |
                    {{ user.following_count || 0 }} 追蹤中
                  </p>
                  <img
                    src="@/assets/img/bell_icon.png"
                    alt="gender icon"
                    class="corner-icon"
                    @click="goToUserNotice"
                    style="cursor: pointer"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Buttons section -->
        <div class="buttons d-flex justify-content-center">
          <button
            class="btn btn-outline-secondary d-flex justify-content-center"
            style="width: 45%; margin: 0 2%; border-radius: 20px"
            @click="shareProfile"
          >
            分享個人檔案
          </button>
          <router-link
            :to="{ name: 'user_setting' }"
            class="btn btn-outline-secondary d-flex justify-content-center"
            style="width: 45%; margin: 0 2%; border-radius: 20px"
          >
            編輯個人簡介
          </router-link>
        </div>

        <!-- Navigation tabs section -->
        <div class="row my-4">
          <div class="col-12">
            <ul class="nav nav-tabs d-flex justify-content-center" style="border-radius: 10px">
              <li class="nav-item">
                <a
                  class="nav-link"
                  :class="{ active: activeTab === 'posts' }"
                  style="border-radius: 10px"
                  href="#"
                  @click="setActiveTab('posts')"
                  >我的貼文</a
                >
              </li>
              <li class="nav-item">
                <a
                  class="nav-link"
                  :class="{ active: activeTab === 'favorites' }"
                  style="border-radius: 10px"
                  href="#"
                  @click="setActiveTab('favorites')"
                  >收藏貼文</a
                >
              </li>
              <li class="nav-item">
                <a
                  class="nav-link"
                  :class="{ active: activeTab === 'likes' }"
                  style="border-radius: 10px"
                  href="#"
                  @click="setActiveTab('likes')"
                  >最愛單品</a
                >
              </li>
            </ul>
          </div>
        </div>

        <!-- Content based on active tab -->
        <div class="row my-4">
          <div class="col-12 text-center" v-if="activeTab === 'posts' && user.posts_count === 0">
            <p>尚未發布任何穿搭</p>
          </div>
          <div class="col-12 text-center" v-else-if="activeTab === 'favorites'">
            <!-- 收藏貼文區塊 -->
            <div id="saved-posts-container" class="content">
              <div class="row">
                <div v-for="post in savedPosts" :key="post.username" class="col-6">
                  <div class="post mb-5">
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
                          @click="toggleDropdown($event)"
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
                      <div>
                        <img :src="post.image" class="l_photo img-fluid" />
                      </div>
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
              </div>
            </div>
          </div>
          <!-- 最愛單品展示區 -->
          <div class="col-12" v-if="activeTab === 'likes' && favoriteItems.length > 0">
            <div class="row">
              <div class="col-md-4 mb-4" v-for="item in favoriteItems" :key="item.id">
                <div class="card custom-card">
                  <img :src="item.image" class="card-img-top" :alt="item.name" />
                  <div class="card-body">
                    <h5 class="card-title">{{ item.name }}</h5>
                    <p class="card-text">品牌: {{ item.brand }}</p>
                    <p class="card-text">價格: ${{ item.price }}</p>
                    <!-- router-link 跳轉到 closet_detail.vue -->
                    <router-link :to="{ name: 'closet_detail', params: { id: item.id } }" class="btn custom-button"
                      >查看詳細</router-link
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-12 text-center" v-else-if="activeTab === 'likes'">
            <p>這裡將顯示你最愛的單品</p>
          </div>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from "vuex";
  import defaultProfileImage from "@/assets/img/user_profile_default.jpg";

  export default {
    name: "user_profile",
    data() {
      return {
        loading: true,
        error: null,
        user: JSON.parse(sessionStorage.getItem("user")) || {},
        activeTab: "posts",
        favoriteItems: [], // 儲存最愛單品的陣列
        savedPosts: [
          {
            username: "嗡嗡嗡",
            description: "今日OOTD，鄰家妹妹vs帥氣姐姐，更喜歡哪個~~😍",
            hashtags: "#OOTD #帥氣 #甜美",
            location: "中原大學",
            time: "2024-04-18",
            image: require("@/assets/img/post_01.jpg"),
            likes: 12,
            comments: 3,
            newComment: "",
          },
          {
            username: "哇哈哈",
            description: "今天天氣真好，出門散步拍了些美照。",
            hashtags: "#散步 #美照 #好心情",
            location: "台北市",
            time: "2024-04-17",
            image: "https://picsum.photos/300/200?random=1",
            likes: 8,
            comments: 5,
            newComment: "",
          },
        ],
      };
    },
    computed: {
      ...mapGetters("auth", ["isAuthenticated", "user"]),
      defaultProfileImage() {
        return defaultProfileImage;
      },
    },
    methods: {
      ...mapActions("auth", ["fetchUserProfile"]),
      async loadUserProfile() {
        try {
          this.loading = true;
          this.error = null;
          await this.fetchUserProfile();
        } catch (error) {
          this.error = "無法載入用戶資料，請稍後再試。";
        } finally {
          this.loading = false;
        }
      },
      async loadFavoriteItems() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/favorites/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.favoriteItems = response.data;
        } catch (error) {
          console.error("Error fetching favorite items:", error);
        }
      },
      async fetchloveItems(endpoint) {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${endpoint}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          console.log("Items fetched successfully:", response.data);
          this.favoriteItems = response.data; // 確保將獲取到的資料賦值給 favoriteItems
        } catch (error) {
          console.error("Error fetching favorite items:", error);
        }
      },

      setActiveTab(tab) {
        this.activeTab = tab;
        if (tab === "likes") {
          this.loadFavoriteItems(); // 當點擊「最愛單品」頁籤時，載入最愛單品
        }
      },
      shareProfile() {
        alert("分享功能尚未實現");
      },
      goToUserNotice() {
        this.$router.push({ name: "user_notice" });
      },
      goToSocialFollowList() {
        this.$router.push({ name: "social_follow_list" });
      },
      toggleDropdown(event) {
        event.currentTarget.nextElementSibling.classList.toggle("show");
      },
      toggleCommentBox(event) {
        const commentBox = event.currentTarget.parentElement.nextElementSibling;
        commentBox.style.display = commentBox.style.display === "none" || !commentBox.style.display ? "block" : "none";
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
        this.savedPosts = this.savedPosts.filter((p) => p !== post);
      },
    },
    mounted() {
      if (this.isAuthenticated) {
        this.loadUserProfile();
        this.fetchloveItems("move_to_love"); // 要加載最愛項目
      } else {
        this.$router.push("/login");
      }
    },
    watch: {
      isAuthenticated(newValue) {
        if (newValue) {
          this.loadUserProfile();
        } else {
          this.$router.push("/login");
        }
      },
    },
  };
</script>

<style scoped>
  .container {
    width: 90%;
    display: flex;
    flex-direction: column;
    max-width: 1200px;
    margin: 100px auto 100px auto;
  }

  .img-fluid {
    border-radius: 10px;
  }

  .nav-tabs .nav-link {
    color: #333;
  }

  .nav-tabs .nav-link.active {
    color: #000;
    font-weight: bold;
  }

  .text-center p {
    font-size: 1.2rem;
    color: #777;
  }

  .rounded-circle {
    border-radius: 50%;
  }

  /* Two-column layout */
  .result-item {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
  }

  .result-item .date {
    font-weight: bold;
    display: block;
    margin-bottom: 10px;
  }

  .line-qr-code img {
    max-width: 50%;
    height: auto;
    border-radius: 10px;
  }

  .icon {
    width: 20px; /* Adjust the size as needed */
    height: 20px;
    margin-left: 5px; /* Add some margin if needed */
  }

  /* Position small icon in the top right corner */
  .corner-icon {
    width: 26px;
    height: 26px;
    position: absolute;
    top: 0;
    right: 0;
    transform: translate(50%, -50%); /* Adjust position to align with the corner */
  }

  @media (min-width: 992px) {
    .col-lg-6 {
      margin-bottom: 20px;
    }
  }

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

  .custom-card {
    height: 100%; /* 讓卡片撐滿父元素 */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .custom-img {
    height: 200px; /* 固定圖片高度 */
    object-fit: cover; /* 圖片自適應，保持比例 */
  }

  .card-body {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* 自定義按鈕樣式 */
  .custom-button {
    background-color: #e7d8c9; /* 更改按鈕顏色 */
    color: white; /* 按鈕文字顏色 */
    border: none;
    padding: 10px 20px;
    border-radius: 5px; /* 圓角 */
    cursor: pointer;
    text-align: center;
  }

  .custom-button:hover {
    background-color: #d6c2b0; /* 懸停時的按鈕顏色 */
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

  /* 小屏幕样式 */
  @media (max-width: 768px) {
    .main-content {
      margin-top: 90px;
    }
  }
</style>
