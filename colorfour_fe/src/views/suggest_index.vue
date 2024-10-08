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
        <div class="col-12 d-flex justify-content-between align-items-center">
          <h2> </h2>
          <div class="item-info-wrap">
            <router-link to="/suggest_recommend" class="btn btn-outline-secondary mx-2">新增推薦</router-link>
            <button @click="deleteItems" class="btn btn-outline-secondary mx-2">刪除推薦</button>
          </div>
        </div>
      </div>
      <div class="row" id="recommendation-list">
        <div v-for="rec in recommendations" :key="rec.id" class="card col-4 mb-3">
          <img :src="rec.image" class="card-img-top" :alt="rec.title" />
          <div class="card-body">
            <h5 class="card-title">{{ rec.title }}</h5>
            <p class="card-text">
              <small class="text-muted">推薦日期: {{ rec.date }}</small>
            </p>
            <router-link :to="rec.link" class="btn btn-outline-secondary">查看推薦詳情</router-link>
          </div>
          <div class="form-check check-box-top-right">
            <input type="checkbox" class="form-check-input" v-model="selectedItems" :value="rec.id" />
            <label class="form-check-label"></label>
          </div>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
export default {
  name: "suggest_index",
  data() {
    return {
      selectedItems: [], // 用於儲存被選中的推薦項目
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
  methods: {
    deleteItems() {
      this.recommendations = this.recommendations.filter((rec) => !this.selectedItems.includes(rec.id));
      this.selectedItems = [];
      alert("選中的項目已永久刪除");
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
