<template>
  <div>
    <div id="header"></div>
    <main class="container">
      <div class="row">
        <aside class="col-lg-3 mb-4">
          <h2>篩選</h2>
          <div class="mb-3">
            <label for="category" class="form-label">分類:</label>
            <select id="category" class="form-select" v-model="filters.category" @change="filterItems">
              <option value="all">全部</option>
              <option value="top">上衣</option>
              <option value="bottom">下身</option>
              <option value="coat">外套</option>
              <option value="shoes">鞋子</option>
              <option value="accessories">配件</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="brand" class="form-label">品牌:</label>
            <select id="brand" class="form-select" v-model="filters.brand" @change="filterItems">
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
              <select id="sort-by" class="form-select" v-model="filters.sortBy" @change="filterItems">
                <option value="newest">新增時間 (先到後)</option>
                <option value="oldest">新增時間 (後到先)</option>
                <option value="brand">品牌名稱</option>
                <option value="price-low-high">價格 (低到高)</option>
                <option value="price-high-low">價格 (高到低)</option>
              </select>
            </div>
            <div>
              <button class="btn btn-outline-secondary">新增單品</button>
              <button class="btn btn-outline-secondary">刪除單品</button>
            </div>
          </div>
          <div class="row" id="wardrobe-list">
            <div v-for="item in filteredItems" :key="item.name" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
              <div class="card mb-3">
                <img :src="item.image" class="card-img-top" :alt="item.name" />
                <div class="card-body">
                  <h5 class="card-title">
                    <a :href="item.link">{{ item.name }}</a>
                  </h5>
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
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
  export default {
    name: "closet_index",
    data() {
      return {
        filters: {
          category: "all",
          brand: "all",
          sortBy: "newest",
        },
        items: [
          {
            name: "白T萬歲",
            category: "top",
            brand: "UNIQLO",
            price: 150,
            image: require("@/assets/img/Uniqlo_white_Tshirt.png"),
            link: "closet_detail.html?item=t-shirt",
          },
          {
            name: "短褲",
            category: "bottom",
            brand: "GU",
            price: 70,
            image: require("@/assets/img/closet_04.png"),
            link: "closet_detail.html?item=bottom",
          },
          {
            name: "西裝外套",
            category: "coat",
            brand: "UNIQLO",
            price: 220,
            image: require("@/assets/img/closet_06.png"),
            link: "closet_detail.html?item=coat",
          },
          {
            name: "連身裙",
            category: "dress",
            brand: "GU",
            price: 100,
            image: require("@/assets/img/closet_02.png"),
            link: "closet_detail.html?item=dress",
          },
          {
            name: "小白鞋",
            category: "shoes",
            brand: "無印",
            price: 80,
            image: require("@/assets/img/closet_05.png"),
            link: "closet_detail.html?item=shoes",
          },
          {
            name: "牛仔褲",
            category: "bottom",
            brand: "GU",
            price: 120,
            image: require("@/assets/img/closet_03.png"),
            link: "closet_detail.html?item=bottom",
          },
          {
            name: "墨鏡",
            category: "accessories",
            brand: "品牌C",
            price: 50,
            image: "https://picsum.photos/300/200?random=6",
            link: "closet_detail.html?item=sunglasses",
          },
          {
            name: "手錶",
            category: "accessories",
            brand: "品牌A",
            price: 200,
            image: "https://picsum.photos/300/200?random=7",
            link: "closet_detail.html?item=watch",
          },
          {
            name: "風衣",
            category: "coat",
            brand: "品牌B",
            price: 180,
            image: "https://picsum.photos/300/200?random=8",
            link: "closet_detail.html?item=trench",
          },
          {
            name: "連帽衫",
            category: "top",
            brand: "品牌C",
            price: 130,
            image: "https://picsum.photos/300/200?random=9",
            link: "closet_detail.html?item=hoodie",
          },
          {
            name: "T恤",
            category: "top",
            brand: "品牌E",
            price: 50,
            image: "https://picsum.photos/300/200?random=12",
            link: "closet_detail.html?item=tshirt",
          },
          {
            name: "針織衫",
            category: "top",
            brand: "GU",
            price: 90,
            image: "https://picsum.photos/300/200?random=1",
            link: "closet_detail.html?item=sweater",
          },
          {
            name: "皮帶",
            category: "accessories",
            brand: "品牌F",
            price: 40,
            image: "https://picsum.photos/300/200?random=13",
            link: "closet_detail.html?item=belt",
          },
          {
            name: "運動褲",
            category: "bottom",
            brand: "品牌G",
            price: 60,
            image: "https://picsum.photos/300/200?random=14",
            link: "closet_detail.html?item=sportspants",
          },
          {
            name: "棒球帽",
            category: "accessories",
            brand: "品牌H",
            price: 30,
            image: "https://picsum.photos/300/200?random=15",
            link: "closet_detail.html?item=cap",
          },
          {
            name: "羽絨服",
            category: "coat",
            brand: "品牌I",
            price: 250,
            image: "https://picsum.photos/300/200?random=16",
            link: "closet_detail.html?item=downjacket",
          },
          {
            name: "連身裙",
            category: "top",
            brand: "品牌J",
            price: 110,
            image: "https://picsum.photos/300/200?random=17",
            link: "closet_detail.html?item=dress",
          },
          {
            name: "短靴",
            category: "shoes",
            brand: "品牌K",
            price: 140,
            image: "https://picsum.photos/300/200?random=18",
            link: "closet_detail.html?item=boots",
          },
          {
            name: "牛仔外套",
            category: "coat",
            brand: "品牌L",
            price: 160,
            image: "https://picsum.photos/300/200?random=19",
            link: "closet_detail.html?item=denimjacket",
          },
          {
            name: "手提包",
            category: "accessories",
            brand: "品牌M",
            price: 90,
            image: "https://picsum.photos/300/200?random=20",
            link: "closet_detail.html?item=bag",
          },
        ],
        filteredItems: [],
      };
    },
    methods: {
      filterItems() {
        let filtered = this.items.filter((item) => {
          const categoryMatch = this.filters.category === "all" || item.category === this.filters.category;
          const brandMatch = this.filters.brand === "all" || item.brand === this.filters.brand;
          return categoryMatch && brandMatch;
        });

        switch (this.filters.sortBy) {
          case "newest":
            filtered.sort((a, b) => new Date(b.addedDate) - new Date(a.addedDate));
            break;
          case "oldest":
            filtered.sort((a, b) => new Date(a.addedDate) - new Date(b.addedDate));
            break;
          case "brand":
            filtered.sort((a, b) => a.brand.localeCompare(b.brand));
            break;
          case "price-low-high":
            filtered.sort((a, b) => a.price - b.price);
            break;
          case "price-high-low":
            filtered.sort((a, b) => b.price - a.price);
            break;
        }

        this.filteredItems = filtered;
      },
    },
    mounted() {
      this.filteredItems = this.items;
    },
  };
</script>

<style scoped>
  #wardrobe-list .card {
    margin-bottom: 1.5em;
  }

  .card img {
    max-height: 200px;
    object-fit: cover;
  }

  .card-title {
    font-size: 1.25em;
    margin-bottom: 0.5em;
  }
  .card-title a {
    text-decoration: none;
    color: var(--primary-text-color);
  }

  .card-body {
    text-align: center;
  }

  @media (max-width: 576px) {
    #wardrobe-list .col-12 {
      flex: 0 0 auto;
      width: 33.333333%;
    }
  }

  @media (min-width: 576px) {
    #wardrobe-list .col-sm-6 {
      flex: 0 0 auto;
      width: 33.333333%;
    }
  }

  @media (min-width: 768px) {
    #wardrobe-list .col-md-4 {
      flex: 0 0 auto;
      width: 33.333333%;
    }
  }

  @media (min-width: 992px) {
    #wardrobe-list .col-lg-3 {
      flex: 0 0 auto;
      width: 25%;
    }
  }

  .container {
    color: #86797d;
  }

  .form-select {
    color: #8d8185;
  }

  .btn {
    color: #8d8185;
  }
</style>
