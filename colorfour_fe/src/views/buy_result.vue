<template>
  <div>
    <h1>建議結果</h1>
  
    <!-- 建議結果顯示 -->
    <div class="result-section">
      <div class="percentage">
        <div>
          <p>偏好程度</p>
          <p class="percentage-value">70%</p>
        </div>
        <div>
          <p>相似程度</p>
          <p class="percentage-value">40%</p>
        </div>
      </div>
      <div class="image-section">
        <img src="example.jpg" alt="Suggested item" />
      </div>
    </div>
    <div class="again">
      <button class="back-button" @click="again">重新上傳</button>
    </div>
  
    <!-- 推薦服飾區域 -->
    <div class="recommend-section">
      <h2>推薦服飾</h2>
      <div class="items">
        <!-- 重複元素 -->
        <div class="item" v-for="item in items" :key="item.id">
          <img :src="item.image" :alt="item.name" />
          <p>{{ item.name }}</p>
          <p>{{ item.price }}</p>
          <button class="btn btn-outline-secondary" @click="goToDetail(item.id)">詳細介紹</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name:"buy_result",
  data() {
    return {
      items: [
        // Example 
        { id: 1, name: 'T-Shirt', price: '$200', image: require("@/assets/img/Uniqlo_white_Tshirt.png"), },
        { id: 2, name: 'Dress', price: '$300', image: require("@/assets/img/closet_02.png"), },
        { id: 3, name: 'Shoes', price: '$550',image: require("@/assets/img/closet_05.png"), },
        { id: 4, name: 'Bottom', price: '$250', image: require("@/assets/img/closet_04.png"), }
      ]
    };
  },
  methods: {
    gotodetail() {
      this.$router.push('/buy_detail');  // 將跳轉至 buy_detail.vue
    },
    again() {
      this.$router.push(`/buy_suggest`);
    }
  }
};
</script>

<style scoped>
.result-section {
  text-align: center;
  margin: 40px 0;
}

.percentage {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.percentage-value {
  font-size: 24px;
  font-weight: bold;
  color: #d4b7a1;
}

.image-section img {
  max-width: 100%;
  height: auto;
}

.recommend-section {
  text-align: center;
  margin: 40px 0;
}

.items {
  display: flex;
  justify-content: space-around;
}

.item img {
  width: 100px;
  height: 100px;
}

.item {
  text-align: center;
}
.back-button {
  text-align: center;
  margin: 20px 0;
}

.again {
  text-align: center;
  margin: 20px 0;
}

button {
  padding: 10px 20px;
  background-color: #d4b7a1;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
