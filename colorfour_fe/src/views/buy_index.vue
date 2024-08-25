<template>
  <div class="buy-index">
      <h1>採購建議總覽</h1>
    <!-- 上傳圖片按鈕 -->
    <div class="upload-section">
      <button @click="goToSuggest">前往上傳圖片</button>
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
  name:"buy_index",
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
    goToSuggest() {
      this.$router.push('/buy_suggest');
    },
    goToDetail(itemId) {
      this.$router.push('/buy_detail');
    }
  }
};
</script>

<style scoped>
.upload-section {
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

</style>

