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
      <div class="content">
        <h2>新增貼文</h2>
        <form @submit.prevent="submitPost">
          <div class="form-group">
            <label for="postDescription">貼文內容</label>
            <textarea v-model="post.description" id="postDescription" class="form-control" placeholder="輸入貼文內容"></textarea>
          </div>

          <div class="form-group mt-3">
            <label for="tags" class="form-label">選擇標籤</label>
            <div class="tag-options">
              <button
                v-for="tag in availableTags"
                :key="tag.id"
                type="button"
                class="btn btn-outline-secondary m-1"
                :class="{ selected: selectedTags.includes(tag.id) }"
                @click="toggleTag(tag.id)"
              >
                {{ tag.tag_name }}
              </button>
              <input v-model="newTag" placeholder="新增其他標籤" class="form-control mt-2" @keyup.enter="addNewTag" />
            </div>
          </div>

          <div class="form-group mt-3">
            <label for="postLocation">地點</label>
            <input v-model="post.location" id="postLocation" type="text" class="form-control" placeholder="輸入地點" />
          </div>

          <div class="form-group mt-3">
            <label for="postImage">上傳圖片</label>
            <input type="file" id="postImage" @change="handleImageUpload" class="form-control" />
          </div>

          <button type="submit" class="btn-main" :disabled="submitting">送出貼文</button>
        </form>
      </div>
    </main>
    <div id="footer"></div>
  </div>
</template>

<script>
  import axios from "axios";
  export default {
    data() {
      return {
        post: {
          description: "",
          location: "",
          image: null,
        },
        availableTags: [],
        selectedTags: [],
        newTag: "",
        submitting: false,
      };
    },
    methods: {
      async fetchTags() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/social/tags/`);
          this.availableTags = response.data;
          console.log("標籤列表：", this.availableTags);
        } catch (error) {
          console.error("無法取得標籤:", error);
        }
      },
      toggleTag(tagId) {
        const index = this.selectedTags.indexOf(tagId);
        if (index > -1) {
          this.selectedTags.splice(index, 1);
        } else {
          this.selectedTags.push(tagId);
        }
      },
      async addNewTag() {
        if (this.newTag.trim() === "") return;

        try {
          const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/social/tags/`, {
            tag_name: this.newTag,
          });
          this.availableTags.push(response.data);
          this.selectedTags.push(response.data.id);
          this.newTag = "";
        } catch (error) {
          console.error("無法新增標籤:", error);
        }
      },
      handleImageUpload(event) {
        const file = event.target.files[0];
        if (file) {
          this.post.image = file;
        }
      },
      async submitPost() {
        if (this.submitting) return;
        this.submitting = true;

        try {
          const formData = new FormData();
          formData.append("content", this.post.description);
          formData.append("location", this.post.location);

          if (this.post.image) {
            formData.append("media_url", this.post.image);
          }

          this.selectedTags.forEach((tagId) => {
            formData.append("tags", tagId);
          });

          console.log("提交的表單數據：", Array.from(formData.entries()));

          const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/social/posts/`, formData, {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });

          alert("貼文新增成功！");
          this.$router.push({ name: "social_index" });
        } catch (error) {
          console.error("新增失敗：", error);
          alert("提交失敗，請稍後再試。");
        } finally {
          this.submitting = false;
        }
      },
    },
    mounted() {
      this.fetchTags();
    },
  };
</script>

<style scoped>
  .main-content {
    width: 90%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
  }

  .content {
    margin: 0 auto; /* Center horizontally */
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    max-width: 600px;
  }

  .form-group {
    margin-bottom: 15px;
  }

  .form-control {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  h2 {
    font-size: 1.5em;
    margin-bottom: 20px;
  }

  .btn-primary {
    background-color: #f0a9a9;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    color: white;
    transition: background-color 0.3s ease;
  }

  .btn-primary:hover {
    background-color: #e09393;
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

  /* 確保左側邊欄在大屏幕時顯示 */
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

  /* 小屏幕樣式 */
  @media (max-width: 1020px) {
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
      display: none; /* 隱藏搜索欄位 */
    }

    .left-sidebar .icon-link {
      flex-direction: column;
      align-items: center;
      margin-bottom: 0;
    }

    .left-sidebar .icon-link span {
      display: none; /* 隱藏文字 */
    }

    .left-sidebar .icon-link img {
      margin-right: 0;
      width: 40px;
      height: 40px;
    }
  }

  .left-sidebar .icon-search input {
    width: 100px; /* 設置搜索框的寬度 */
    height: 30px; /* 設置搜索框的高度 */
    padding: 5px; /* 調整內邊距 */
    font-size: 14px; /* 調整字體大小 */
    border-radius: 10px; /* 調整圓角 */
    border: 1px solid #ccc; /* 設置邊框 */
  }

  /* 在小屏幕時也可以相應調整搜索框大小 */
  @media (max-width: 768px) {
    .left-sidebar .icon-search input {
      width: 100px; /* 調整小屏幕時的寬度 */
      height: 25px; /* 調整小屏幕時的高度 */
      font-size: 12px; /* 調整小屏幕時的字體大小 */
    }
  }
</style>
