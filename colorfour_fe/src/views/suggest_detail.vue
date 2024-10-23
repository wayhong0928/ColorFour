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
        <button class="btn btn-outline-secondary edit-button" @click="toggleEdit">編輯推薦</button>
      </div>
      <section class="container">
        <div class="item-img">
          <img :src="item.image" alt="推薦圖片" id="itemImage" />
        </div>
        <div class="item-info" v-if="!isEditing">
          <h1 id="itemName">{{ item.title }}</h1>
          <p id="itemDescription">{{ item.description }}</p>
          <p class="added-date" id="itemDate">推薦日期: {{ item.date }}</p>
        </div>
        <!-- 編輯模式 -->
        <div class="edit-form" v-else>
          <label>名稱:</label>
          <input v-model="editForm.title" />

          <label>標籤:</label>
          <input v-model="editForm.description" placeholder="用逗號分隔" />

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
  export default {
    name: "suggest_detail",
    data() {
      return {
        isEditing: false, // 是否進入編輯模式
        editForm: {
          // 編輯表單資料
          title: "",
          description: "",
        },
        item: {
          image: "https://via.placeholder.com/150",
          title: "查無資料",
          description: "查無資料",
          date: "查無資料",
        },
        recommendations: [
          {
            id: 1,
            title: "表演服",
            image: require("@/assets/img/suggest_01.png"),
            link: "/suggest_detail/1",
            description: "夏天、百搭、休閒、全妝",
            date: "2023-06-01",
          },
          {
            id: 2,
            title: "期末報告穿搭",
            image: require("@/assets/img/suggest_03.png"),
            link: "/suggest_detail/2",
            description: "夏天、正式、報告",
            date: "2023-06-02",
          },
          {
            id: 3,
            title: "推薦穿搭3",
            image: "https://picsum.photos/300/200?random=3",
            link: "/suggest_detail/3",
            description: "這是推薦穿搭3的描述。",
            date: "2023-06-03",
          },
        ],
      };
    },
    created() {
      this.fetchItemDetails();
    },
    methods: {
      toggleEdit() {
        this.isEditing = !this.isEditing;
        if (this.isEditing) {
          // 將原始資料填入編輯表單中
          this.editForm = { ...this.item };
        }
      },
      saveEdit() {
        // 儲存編輯後的資料
        this.item.title = this.editForm.title;
        this.item.description = this.editForm.description;
        this.isEditing = false; // 結束編輯模式
      },
      fetchItemDetails() {
        const itemId = this.$route.params.id;
        const item = this.recommendations.find((i) => i.id === Number(itemId));
        if (item) {
          this.item = item;
        }
      },
      editRecommendation() {
        // 執行編輯推薦的邏輯
      },
      goBack() {
        this.$router.go(-1); // 返回上一頁
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
