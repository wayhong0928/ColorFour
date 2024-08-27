<template>
  <div class="detail-container">
    <h1 class="title">商品詳細介紹</h1>

    <!-- 商品資訊區域 -->
    <div class="item-detail">
      <img :src="item.image" alt="item.name" class="item-image" />
      <div class="item-info">
        <h2 class="item-name">{{ item.name }}</h2>
        <p class="item-price">價格: {{ item.price }}</p>
        <p class="item-description">商品描述: {{ item.description }}</p>
        <p class="item-brand">品牌: {{ item.brand }}</p>
        <button class="back-button" @click="goBack">返回上一頁</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "buy_detail",
  data() {
    return {
      item: {
        name: "商品名稱",
        price: "NT$ 1000",
        description: "這是一個非常棒的商品。",
        brand: "品牌名稱",
        image: "path_to_image.jpg",
      },
    };
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped>
.detail-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  margin-bottom: 30px;
  font-size: 2rem;
  color: #495057;
}

.item-detail {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.item-image {
  width: 250px;
  height: 250px;
  object-fit: cover;
  border-radius: 10px;
}

.item-info {
  flex: 1;
  margin-left: 20px;
}

.item-name {
  font-size: 1.8rem;
  color: #343a40;
  margin-bottom: 10px;
}

.item-price {
  font-size: 1.4rem;
  color: #d63384;
  margin-bottom: 20px;
}

.item-description, .item-stock {
  font-size: 1.2rem;
  color: #6c757d;
  margin-bottom: 10px;
}

.back-button {
  padding: 10px 20px;
  background-color: #d4b7a1;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.back-button:hover {
  background-color: #b3957e;
}
</style>

