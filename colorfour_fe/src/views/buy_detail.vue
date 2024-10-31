<template>
  <div class="detail-container">
    <h1 class="title">商品詳細介紹</h1>

    <!-- 商品資訊區域 -->
    <section class="container">
      <div class="item-img">
        <img :src="item.image" alt="服飾圖片" />
      </div>
      <div class="item-info">
        <h1>{{ item.name }}</h1>
        <p>品牌: {{ item.brand }}</p>
        <p>價格: ${{ item.price }}</p>
        <p class="hashtag">種類：#{{ item.category }}</p>
        <p class="hashtag">標籤：{{ item.tags.map((tag) => `#${tag}`).join(" ") }}</p>
        <p class="added-date">加入日期: {{ item.addedDate }}</p>
      </div>
      <button class="btn btn-outline-secondary" @click="goBack">返回</button>
    </section>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    props: ["id"],
    data() {
      return {
        item: null, // 儲存對應id的項目
        items: [
          {
            id: 1,
            name: "白T萬歲",
            category: "t-shirt",
            brand: "UNIQLO",
            price: 150,
            addedDate: "2024/06/01",
            image: require("@/assets/img/Uniqlo_white_Tshirt.png"),
            tags: ["春天", "夏天", "休閒", "百搭"],
          },
          {
            id: 2,
            name: "連身裙",
            category: "dress",
            brand: "GU",
            price: 100,
            addedDate: "2024/06/02",
            image: require("@/assets/img/closet_02.png"),
            tags: ["春天", "夏天"],
          },
          {
            id: 3,
            name: "牛仔褲",
            category: "bottom",
            brand: "GU",
            price: 70,
            addedDate: "2024/06/03",
            image: require("@/assets/img/closet_03.png"),
            tags: ["春天", "夏天"],
          },
          {
            id: 4,
            name: "短褲",
            category: "bottom",
            brand: "UNIQLO",
            price: 220,
            addedDate: "2024/06/04",
            image: require("@/assets/img/closet_04.png"),
            tags: ["秋天", "冬天"],
          },
          {
            id: 5,
            name: "小白鞋",
            category: "shoes",
            brand: "無印",
            price: 80,
            addedDate: "2024/06/05",
            image: require("@/assets/img/closet_05.png"),
            tags: ["春天", "夏天"],
          },
        ],
      };
    },
    created() {
      const itemId = this.$route.params.id; // 從路由獲取商品id
      this.item = this.items.find((item) => item.id == itemId); // 根據id查找商品
    },
    methods: {
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

  button {
    width: auto; /* 讓按鈕的寬度自適應內容 */
    text-align: center; /* 讓按鈕內的字置中 */
    padding: 10px 20px; /* 添加適當的內邊距讓按鈕看起來更大 */
    display: inline-flex;
    align-items: center; /* 水平置中 */
    justify-content: center; /* 垂直置中 */
  }

  .container {
    width: 90%;
    min-height: 400px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    background-color: #ffffff;
    border: #333333 1px solid;
    box-shadow: #999999 3px 3px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 20px;
    position: relative;
  }

  .item-info-wrap {
    width: 90%;
    display: flex;
    align-items: end;
    justify-content: end;
    margin-bottom: 20px;
  }

  .item-img {
    width: 45%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .item-img img {
    width: 100%;
    height: 100%;
    border-radius: 20px;
    object-fit: cover;
  }

  .item-info {
    width: 50%;
    margin-left: 20px;
    display: flex;
    flex-direction: column;
    text-align: start;
    align-items: flex-start;
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

  @media screen and (max-width: 768px) {
    .item-img {
      width: 90%;
      margin-bottom: 20px;
    }

    .item-info {
      width: 90%;
      margin-left: 0;
    }

    main button {
      width: 30%;
    }
  }
</style>
