<template>
  <!-- 修改後code -->
  <div>
    <nav aria-label="breadcrumb">
      <ol class="bread">
        <li><router-link to="/">首頁</router-link></li>
        <li aria-current="page">衣櫃管理</li>
      </ol>
    </nav>
    <main>
      <div class="row">
        <aside class="col-lg-3 mb-4">
          <div class="mb-3">
            <label for="category" class="form-label">分類</label>
            <select v-model="selectedCategory" id="category" class="form-select">
              <option value="all">全部</option>
              <option value="typeA">類型A</option>
              <option value="typeB">類型B</option>
              <option value="typeC">類型C</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="brand" class="form-label">品牌</label>
            <select v-model="selectedBrand" id="brand" class="form-select">
              <option value="all">全部</option>
              <option value="品牌A">品牌A</option>
              <option value="品牌B">品牌B</option>
              <option value="品牌C">品牌C</option>
            </select>
          </div>
        </aside>

        <div class="col-lg-9">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <div>
              <label for="sort-by" class="form-label">排序方式:</label>
              <select v-model="sortBy" id="sort-by" class="form-select">
                <option value="newest">新增時間 (先到後)</option>
                <option value="oldest">新增時間 (後到先)</option>
                <option value="brand">品牌名稱</option>
                <option value="price-low-high">價格 (低到高)</option>
                <option value="price-high-low">價格 (高到低)</option>
              </select>
            </div>
            <div>
              <router-link to="/closet_new" class="btn btn-outline-secondary">新增單品</router-link>
              <router-link to="/closet_trash" class="btn btn-outline-secondary">回收區</router-link>
            </div>
          </div>

          <!-- 這裡是關鍵的資料顯示區域 -->
          <div class="row" id="wardrobe-list">
    <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" v-for="item in sortedAndFilteredItems" :key="item.id">
      <div class="card mb-3">
        <img :src="item.photo_url" class="card-img-top" :alt="item.item_name" />
        <div class="card-body">
          <h5 class="card-title">
            <router-link :to="{ name: 'closet_detail', params: { id: item.id } }">{{ item.item_name }}</router-link>
          </h5>
          <!-- Add the "穿搭組合推薦" button -->
          <router-link
            class="btn btn-outline-secondary"
            :to="{ name: 'suggest_detail', params: { id: item.id } }"
          >
            穿搭推薦
          </router-link>
        </div>
      </div>
    </div>
  </div>

          <section aria-label="Page navigation" style="margin-bottom: 100px">
            <ul class="pagination justify-content-center">
              <!-- 分頁項在此 -->
            </ul>
          </section>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        items: [],
        selectedCategory: "all",
        selectedBrand: "all",
        sortBy: "newest",
      };
    },
    computed: {
      filteredItems() {
        let filtered = this.items;

        // 過濾分類
        if (this.selectedCategory !== "all") {
          filtered = filtered.filter((item) => item.category === this.selectedCategory);
        }

        // 過濾品牌
        if (this.selectedBrand !== "all") {
          filtered = filtered.filter((item) => item.brand === this.selectedBrand);
        }

        return filtered;
      },
      sortedAndFilteredItems() {
        let sortedItems = [...this.filteredItems];

        switch (this.sortBy) {
          case "newest":
            sortedItems.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
            break;
          case "oldest":
            sortedItems.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
            break;
          case "brand":
            sortedItems.sort((a, b) => a.brand.localeCompare(b.brand));
            break;
          case "price-low-high":
            sortedItems.sort((a, b) => a.price - b.price);
            break;
          case "price-high-low":
            sortedItems.sort((a, b) => b.price - a.price);
            break;
        }

        return sortedItems;
      },
    },
    methods: {
      async fetchItems() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/`, {
            params: {
              trash: "false",
            },
          });
          this.items = response.data;
        } catch (error) {
          console.error("Error fetching wardrobe items:", error);
        }
      },
    },
    created() {
      this.fetchItems();
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
