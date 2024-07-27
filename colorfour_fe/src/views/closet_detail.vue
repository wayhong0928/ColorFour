<template>
  <div>
    <div id="header"></div>
    <main class="container">
      <div class="row">
        <div class="col-lg-9">
          <h1>{{ item.name }}</h1>
          <img :src="item.image" :alt="item.name" class="img-fluid mb-4" />
          <p>分類: {{ item.category }}</p>
          <p>品牌: {{ item.brand }}</p>
          <p>價格: {{ item.price }} 元</p>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
export default {
  name: "closet_detail",
  data() {
    return {
      items: [
        {
          name: "白T萬歲",
          category: "top",
          brand: "UNIQLO",
          price: 150,
          image: require("@/assets/img/Uniqlo_white_Tshirt.png"),
        },
        {
          name: "短褲",
          category: "bottom",
          brand: "GU",
          price: 70,
          image: require("@/assets/img/closet_04.png"),
        },
        {
          name: "西裝外套",
          category: "coat",
          brand: "UNIQLO",
          price: 220,
          image: require("@/assets/img/closet_06.png"),
        },
        {
          name: "連身裙",
          category: "dress",
          brand: "GU",
          price: 100,
          image: require("@/assets/img/closet_02.png"),
        },
        {
          name: "小白鞋",
          category: "shoes",
          brand: "無印",
          price: 80,
          image: require("@/assets/img/closet_05.png"),
        },
        {
          name: "牛仔褲",
          category: "bottom",
          brand: "GU",
          price: 120,
          image: require("@/assets/img/closet_03.png"),
        },
        {
          name: "墨鏡",
          category: "accessories",
          brand: "品牌C",
          price: 50,
          image: "https://picsum.photos/300/200?random=6",
        },
        {
          name: "手錶",
          category: "accessories",
          brand: "品牌A",
          price: 200,
          image: "https://picsum.photos/300/200?random=7",
        },
        {
          name: "風衣",
          category: "coat",
          brand: "品牌B",
          price: 180,
          image: "https://picsum.photos/300/200?random=8",
        },
        {
          name: "連帽衫",
          category: "top",
          brand: "品牌C",
          price: 130,
          image: "https://picsum.photos/300/200?random=9",
        },
        {
          name: "T恤",
          category: "top",
          brand: "品牌E",
          price: 50,
          image: "https://picsum.photos/300/200?random=12",
        },
        {
          name: "針織衫",
          category: "top",
          brand: "GU",
          price: 90,
          image: "https://picsum.photos/300/200?random=1",
        },
        {
          name: "皮帶",
          category: "accessories",
          brand: "品牌F",
          price: 40,
          image: "https://picsum.photos/300/200?random=13",
        },
        {
          name: "運動褲",
          category: "bottom",
          brand: "品牌G",
          price: 60,
          image: "https://picsum.photos/300/200?random=14",
        },
        {
          name: "棒球帽",
          category: "accessories",
          brand: "品牌H",
          price: 30,
          image: "https://picsum.photos/300/200?random=15",
        },
        {
          name: "羽絨服",
          category: "coat",
          brand: "品牌I",
          price: 250,
          image: "https://picsum.photos/300/200?random=16",
        },
        {
          name: "連身裙",
          category: "top",
          brand: "品牌J",
          price: 110,
          image: "https://picsum.photos/300/200?random=17",
        },
        {
          name: "短靴",
          category: "shoes",
          brand: "品牌K",
          price: 140,
          image: "https://picsum.photos/300/200?random=18",
        },
        {
          name: "牛仔外套",
          category: "coat",
          brand: "品牌L",
          price: 160,
          image: "https://picsum.photos/300/200?random=19",
        },
      ],
      item: {},
    };
  },
  created() {
    const itemName = this.$route.params.itemName;
    this.item = this.items.find((item) => item.name === itemName) || {};
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

main button {
  width: 20%;
  display: flex;
  align-items: end;
  justify-content: end;
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

@media screen and (max-width: 768px) {
  .item-img {
    width: 90%;
    margin-bottom: 20px;
  }

  .item-info {
    width: 90%;
    margin-left: 0;
  }
  .item-info h1 {
    align-items: center;
  }

  main button {
    width: 30%;
  }
}
</style>
