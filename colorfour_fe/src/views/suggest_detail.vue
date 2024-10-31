<template>
  <div>
    <div id="header"></div>
    <main>
      <nav aria-label="breadcrumb">
        <ol class="bread">
          <li><router-link to="/">首頁</router-link></li>
          <li><router-link to="/suggest_index">推薦總覽</router-link></li>
          <li aria-current="page">推薦詳情</li>
        </ol>
      </nav>
      <div class="wrap">
        <router-link
          class="btn btn-outline-secondary edit-button"
          :to="{
            name: 'social_new',
            query: {
              description: item.recommendation_name,
              location: item.location,
              image: item.recommendation_image,
            },
          }"
        >
          新增貼文
        </router-link>
        <button class="btn btn-outline-secondary edit-button" @click="toggleEdit">編輯推薦</button>
        <button class="btn btn-outline-danger delete-button" @click="deleteRecommendation">刪除推薦</button>
      </div>
      <section class="container">
        <div class="item-img">
          <img :src="item.recommendation_image || defaultImage" alt="推薦圖片" id="itemImage" />
        </div>
        <div class="item-info" v-if="!isEditing">
          <h1>{{ item.recommendation_name }}</h1>
          <p>位置: {{ item.location }}</p>
          <p>場合: {{ item.occasion }}</p>
          <p>氣色: {{ item.skin_tone }}</p>
          <p>推薦日期: {{ formatDate(item.created_at) }}</p>
        </div>
        <!-- 編輯模式 -->
        <div class="edit-form" v-else>
          <label>名稱:</label>
          <input v-model="editForm.recommendation_name" />

          <label>位置:</label>
          <input v-model="editForm.location" />

          <label>場合:</label>
          <input v-model="editForm.occasion" />

          <label>氣色:</label>
          <input v-model="editForm.skin_tone" />

          <button class="btn btn-outline-secondary" @click="saveEdit">儲存</button>
        </div>
      </section>
      <button class="btn btn-outline-secondary" @click="goBack">返回上一頁</button>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
  import axios from "axios";
  import defaultProfileImage from "@/assets/img/user_profile_default.jpg";

  export default {
    name: "suggest_detail",
    data() {
      return {
        isEditing: false, // 是否進入編輯模式
        editForm: {
          title: "",
          description: "",
        },
        item: {
          image: "https://via.placeholder.com/150",
          title: "查無資料",
          description: "查無資料",
          date: "查無資料",
        },
      };
    },
    created() {
      this.fetchItemDetails();
    },
    methods: {
      toggleEdit() {
        this.isEditing = !this.isEditing;
        if (this.isEditing) {
          this.editForm = { ...this.item };
        }
      },
      async saveEdit() {
        const itemId = this.$route.params.id;
        try {
          const response = await axios.put(`http://localhost:8000/recommender/recommendations/${itemId}/`, this.editForm, {
            headers: { Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}` },
          });
          this.item = response.data;
          this.isEditing = false;
          alert("推薦已成功更新！");
        } catch (error) {
          console.error("更新失敗：", error.response ? error.response.data : error);
          alert("更新失敗，請稍後再試。");
        }
      },
      async fetchItemDetails() {
        const itemId = this.$route.params.id;
        try {
          const response = await axios.get(`http://localhost:8000/recommender/recommendations/${itemId}/`, {
            headers: { Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}` },
          });
          this.item = response.data;
        } catch (error) {
          console.error("無法取得推薦詳情：", error.response ? error.response.data : error);
          alert("無法取得推薦詳情，請稍後再試。");
        }
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString(); // 格式化為日期+時間
      },
      goBack() {
        this.$router.go(-1);
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

  .wrap {
    width: 100%;
    display: flex;
    justify-content: end;
    margin-bottom: 20px;
  }
  .wrap button {
    margin: 0 10px;
  }

  .wrap .btn {
    display: inline-flex;
    align-items: center; /* 垂直置中 */
    justify-content: center; /* 水平置中 */
    text-align: center; /* 文字居中 */
    padding: 10px 15px;
  }

  .container {
    min-height: 400px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    background-color: #e9e8e8;
    margin: 0 auto;
    padding: 20px;
    border-radius: 20px;
    position: relative;
  }

  .item-img {
    width: 45%;
    height: 45%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 0px;
  }

  .item-img img {
    width: 100%;
    height: 100%;
    margin: auto;
    position: relative;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 20px;
  }

  .item-info {
    width: 50%;
    margin-left: 20px;
    display: flex;
    flex-direction: column;
    text-align: center;
    align-items: start;
  }

  .item-info h1,
  .item-info p {
    margin: 5px 0;
  }

  .item-info h1 {
    font-size: 2rem;
    margin-bottom: 10px;
  }

  .item-info p {
    font-size: 1rem;
    margin-bottom: 10px;
  }

  .item-info .price {
    font-size: 1.5rem;
    color: #333;
  }

  .item-info .added-date {
    font-size: 1rem;
    color: #777;
  }

  main button {
    width: auto; /* 讓按鈕的寬度自適應內容 */
    text-align: center; /* 讓按鈕內的字置中 */
    padding: 10px 20px; /* 添加適當的內邊距讓按鈕看起來更大 */
    display: inline-flex;
    align-items: center; /* 水平置中 */
    justify-content: center; /* 垂直置中 */
    margin-top: 20px;
  }

  .back-button {
    padding: 10px 20px;
    background-color: #d4b7a1;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    margin-top: 30px;
  }

  .back-button:hover {
    background-color: #b3957e;
  }

  .edit-form label {
    display: block;
    margin-top: 10px;
  }

  .edit-form input {
    width: 100%;
    padding: 5px;
    margin-top: 5px;
  }

  @media screen and (max-width: 768px) {
    .item-img {
      width: 90%;
      flex-wrap: wrap;
      margin-bottom: 0;
    }

    .item-info {
      width: 90%;
      flex-wrap: wrap;
      align-items: flex-start;
    }
  }
</style>
