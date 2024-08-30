<template>
  <div>
    <main>
      <div class="item-info-wrap">
        <button class="btn btn-outline-secondary edit-button" @click="editItem">編輯單品</button>
        <button class="btn btn-outline-secondary" @click="deleteItem">刪除單品</button>
      </div>
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
      </section>
    </main>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        item: null,
      };
    },
    methods: {
      async fetchItem() {
        const itemId = this.$route.params.id;
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${itemId}/`);
          this.item = response.data;
        } catch (error) {
          console.error("Error fetching item details:", error);
        }
      },
      async deleteItem() {
        const itemId = this.$route.params.id;
        try {
          await axios.delete(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${itemId}/`);
          this.$router.push("/closet");
        } catch (error) {
          console.error("Error deleting item:", error);
        }
      },
      editItem() {
        this.$router.push({ name: "edit_item", params: { id: this.item.id } });
      },
    },
    created() {
      this.fetchItem();
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
