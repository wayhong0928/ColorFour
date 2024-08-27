<template>
  <div>
    <div id="header"></div>
    <main>
      <div class="wrap">
        <button class="btn btn-outline-secondary" @click="editRecommendation">編輯推薦</button>
        <router-link to="/suggest_index" class="btn btn-outline-secondary">回推薦總覽</router-link>
      </div>
      <section class="container">
        <div class="item-img">
          <img :src="item.image" alt="推薦圖片" id="itemImage" />
        </div>
        <div class="item-info">
          <h1 id="itemName">{{ item.title }}</h1>
          <p id="itemDescription">{{ item.description }}</p>
          <p class="added-date" id="itemDate">推薦日期: {{ item.date }}</p>
        </div>
      </section>
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
      item: {
        image: "https://via.placeholder.com/150",
        title: "查無資料",
        description: "查無資料",
        date: "查無資料"
      },
      recommendations: [
        { id: 1, title: "表演服", image: require('@/assets/img/suggest_01.png'), link:"/suggest_detail/1", description: "夏天、百搭、休閒、全妝", date: "2023-06-01" },
        { id: 2, title: "期末報告穿搭", image: require("@/assets/img/suggest_03.png"), link:"/suggest_detail/2", description: "夏天、正式、報告", date: "2023-06-02" },
        { id: 3, title: "推薦穿搭3", image: "https://picsum.photos/300/200?random=3", link:"/suggest_detail/3", description: "這是推薦穿搭3的描述。", date: "2023-06-03" },
      ]
    };
  },
  created() {
    this.fetchItemDetails();
  },
  methods: {
    fetchItemDetails() {
      const itemId = this.$route.params.id;
      const item = this.recommendations.find(i => i.id === Number(itemId));
      if (item) {
        this.item = item;
      }
    },
    editRecommendation() {
      // 執行編輯推薦的邏輯
    }
  }
};
</script>

<style scoped>
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
