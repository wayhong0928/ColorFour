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
                :src="user.profile_image || 'https://picsum.photos/100/100?random=1'"
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
                  <p>{{ user.gender || "未設置" }}</p>
                  <p>
                    {{ user.posts_count || 0 }} 貼文 | {{ user.followers_count || 0 }} 粉絲 |
                    {{ user.following_count || 0 }} 追蹤中
                  </p>
                  <img src="@/assets/img/bell_icon.png" alt="gender icon" class="corner-icon" />
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
                <a class="nav-link active" style="border-radius: 10px" href="#" @click="setActiveTab('posts')">我的貼文</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" style="border-radius: 10px" href="#" @click="setActiveTab('favorites')">收藏穿搭</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" style="border-radius: 10px" href="#" @click="setActiveTab('likes')">最愛單品</a>
              </li>
            </ul>
          </div>
        </div>

        <!-- Content based on active tab -->
        <div class="row my-4">
          <div class="col-12 text-center" v-if="activeTab === 'posts' && user.posts_count === 0">
            <p>尚未發布任何穿搭</p>
          </div>
          <!-- Add content for other tabs here -->
        </div>

        <!-- Color analysis results -->
        <div class="row my-4">
          <div class="col-lg-6">
            <h3>個人色彩分析結果</h3>
            <div class="result-item" v-if="user.color_analysis">
              <span class="date">{{ user.color_analysis.date }}</span> {{ user.color_analysis.type }}
              <br />
              <div v-for="(feature, index) in user.color_analysis.features" :key="index">
                {{ feature }}
                <br />
              </div>
              <img src="@/assets/img/next_icon.png" class="icon" alt="next icon" />
            </div>
            <div v-else>
              <p>尚未進行個人色彩分析</p>
            </div>
          </div>

          <div class="col-lg-6">
            <div class="line-qr-code" v-if="user.line_qr_code">
              <h4>Line QR-code</h4>
              <img :src="user.line_qr_code" alt="Line QR-code" class="img-fluid" />
            </div>
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

  export default {
    name: "user_profile",
    data() {
      return {
        loading: true,
        error: null,
        activeTab: "posts",
      };
    },
    computed: {
      ...mapGetters("auth", ["isAuthenticated", "user"]),
    },
    methods: {
      ...mapActions("auth", ["fetchUserProfile"]),
      async loadUserProfile() {
        console.log("開始載入用戶資料");
        try {
          this.loading = true;
          this.error = null;
          await this.fetchUserProfile();
          console.log("用戶資料載入成功:", this.user);
        } catch (error) {
          console.error("載入用戶資料失敗:", error);
          this.error = "無法載入用戶資料，請稍後再試。";
        } finally {
          this.loading = false;
          console.log("用戶資料載入完成，loading 狀態:", this.loading);
        }
      },
      setActiveTab(tab) {
        this.activeTab = tab;
      },
      shareProfile() {
        // Implement share functionality
        alert("分享功能尚未實現");
      },
    },
    mounted() {
      console.log("user_profile 組件已掛載，認證狀態:", this.isAuthenticated);
      if (this.isAuthenticated) {
        this.loadUserProfile();
      } else {
        console.log("用戶未認證，重定向到登入頁面");
        this.$router.push("/login");
      }
    },
    watch: {
      isAuthenticated(newValue) {
        console.log("認證狀態變更:", newValue);
        if (newValue) {
          this.loadUserProfile();
        } else {
          console.log("用戶已登出，重定向到登入頁面");
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
</style>
