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
            <textarea v-model="newPost.description" id="postDescription" class="form-control" placeholder="輸入貼文內容"></textarea>
          </div>

          <div class="form-group mt-3">
            <label for="postHashtags">標籤</label>
            <input v-model="newPost.hashtags" id="postHashtags" type="text" class="form-control" placeholder="#標籤1 #標籤2">
          </div>

          <div class="form-group mt-3">
            <label for="postLocation">地點</label>
            <input v-model="newPost.location" id="postLocation" type="text" class="form-control" placeholder="輸入地點">
          </div>

          <div class="form-group mt-3">
            <label for="postImage">上傳圖片</label>
            <input type="file" id="postImage" @change="handleFileUpload" class="form-control">
          </div>

          <div class="form-group mt-3">
            <label for="postTime">時間</label>
            <input v-model="newPost.time" id="postTime" type="datetime-local" class="form-control">
          </div>

          <div class="form-group mt-4">
            <button type="submit" class="btn btn-primary">提交貼文</button>
          </div>
        </form>
      </div>
    </main>
    <div id="footer"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newPost: {
        description: '',
        hashtags: '',
        location: '',
        image: null,
        time: '',
      },
    };
  },
  methods: {
    handleFileUpload(event) {
      this.newPost.image = event.target.files[0];
    },
    submitPost() {
      // 提交新貼文的邏輯
      console.log('提交貼文:', this.newPost);
      // 此處可以將貼文數據發送到後端或存儲在 Vuex 中
      this.$router.push({ name: 'social_index' }); // 提交後導航回社群平台首頁
    },
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
    top: 90px;
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
