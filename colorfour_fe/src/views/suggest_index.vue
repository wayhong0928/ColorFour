<template>
  <div>
    <nav aria-label="breadcrumb">
      <ol class="bread">
        <li><router-link to="/">首頁</router-link></li>
        <li aria-current="page">穿搭推薦總覽</li>
      </ol>
    </nav>
    <div id="header"></div>
    <main class="container">
      <div class="row my-4">
        <div class="col-12 d-flex justify-content-between align-items-center mb-3">
          <div class="item-info-wrap ms-auto">
            <router-link to="/suggest_recommend" class="btn btn-outline-secondary mx-2">新增推薦</router-link>
            <button @click="deleteItems" class="btn btn-outline-secondary mx-2">刪除推薦</button>
          </div>
        </div>
      </div>
      <div class="row" id="recommendation-list">
        <div v-for="rec in recommendations" :key="rec.id" class="card col-4 mb-3">
          <!-- <img :src="rec.image" class="card-img-top" :alt="rec.title" /> -->
          <!-- 此圖片暫時用 -->
          <img :src="rec.image || defaultImage" class="card-img-top" :alt="rec.title" @error="handleImageError($event, rec)" />
          <h5>{{ rec.recommendation_name }}</h5>
          <div class="card-body">
            <h5 class="card-title">{{ rec.title }}</h5>
            <p class="card-text">
              <small class="text-muted">推薦日期: {{ formatDate(rec.created_at) }}</small>
            </p>
            <router-link :to="`/suggest_detail/${rec.id}`" class="btn btn-outline-secondary">查看推薦詳情</router-link>
          </div>
          <div class="form-check check-box-top-right">
            <input type="checkbox" class="form-check-input" v-model="selectedItems" :value="rec.id" />
            <label class="form-check-label"></label>
          </div>
        </div>
      </div>
    </main>
    <div id="footer"></div>
  </div>
</template>

<script>
  import axios from "axios";
  import defaultProfileImage from "@/assets/img/user_profile_default.jpg";
  export default {
    name: "suggest_index",
    data() {
      return {
        selectedItems: [],
        recommendations: [],
      };
    },
    created() {
      this.fetchRecommendations();
    },
    methods: {
      async fetchRecommendations() {
        try {
          const response = await axios.get("http://localhost:8000/recommender/recommendations/", {
            headers: { Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}` },
          });
          this.recommendations = response.data;
          console.log("推薦清單：", this.recommendations);
        } catch (error) {
          console.error("無法獲取推薦", error);
          alert("載入推薦失敗，請稍後再試。");
        }
      },
      async deleteItems() {
        if (this.selectedItems.length === 0) {
          alert("請選擇至少一個推薦項目進行刪除");
          return;
        }

        try {
          await Promise.all(
            this.selectedItems.map((id) =>
              axios.delete(`http://localhost:8000/recommender/recommendations/${id}/`, {
                headers: { Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}` },
              })
            )
          );
          // 更新畫面中的推薦清單
          this.recommendations = this.recommendations.filter((rec) => !this.selectedItems.includes(rec.id));
          this.selectedItems = [];
          alert("選中的項目已成功刪除");
        } catch (error) {
          console.error("刪除失敗：", error);
          alert("刪除失敗，請稍後再試。");
        }
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString(); // 格式化為日期+時間
      },
    },

    computed: {
      defaultImage() {
        return defaultProfileImage;
      },
    },
  };
</script>

<style scoped>
  .bread {
    display: flex;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .bread li {
    padding: 0 20px;
  }

  .bread li + li {
    padding-left: 0;
  }

  .bread li + li:before {
    content: ">";
    color: #333;
    margin-right: 20px;
  }

  .bread a {
    text-decoration: none;
    color: #333;
  }
  .card-img-top {
    width: 60%;
    height: 60%;
    border-radius: 20px;
    margin: 20px auto;
  }

  .row .card {
    width: 45%;
    margin: 20px auto;
    display: flex;
  }

  .card-body {
    width: 100%;
    margin: 10px auto;
    display: flex;
    flex-direction: column;
  }

  /* 按鈕之間的間距 */
  .item-info-wrap .btn {
    margin-right: 10px;
  }

  /* 勾選框位置設定，放置於右上角 */
  .form-check {
    position: absolute;
    top: 10px;
    right: 10px;
  }

  /* 卡片容器在小螢幕的樣式 */
  @media (max-width: 768px) {
    .row .card {
      width: 90%;
      margin: 20px auto;
    }
  }
</style>
