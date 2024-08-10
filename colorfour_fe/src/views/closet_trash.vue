<template>
  <div>
    <main class="container">
      <div class="row">
        <aside class="col-lg-3 mb-4">
          <h2>篩選</h2>
          <div class="mb-3">
            <label for="category" class="form-label">分類:</label>
            <select v-model="selectedCategory" id="category" class="form-select">
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
              <a href="closet_new.html" class="btn btn-outline-secondary">新增單品</a>
              <a href="closet_trash.html" class="btn btn-outline-secondary">回收區</a>
            </div>
          </div>
          <div class="row" id="wardrobe-list">
            <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" v-for="item in filteredItems" :key="item.id">
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
  </div>
</template>

<script>
export default {
  name: "closet_trash",
  data() {
    return {
      selectedCategory: "all",
      selectedBrand: "all",
      sortBy: "newest",
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
          link: "closet_detail.html?id=1",
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
          link: "closet_detail.html?id=2",
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
          link: "closet_detail.html?id=3",
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
          link: "closet_detail.html?id=4",
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
          link: "closet_detail.html?id=5",
        },
        {
          id: 6,
          name: "西裝外套",
          category: "coat",
          brand: "GU",
          price: 120,
          addedDate: "2024/06/06",
          image: require("@/assets/img/closet_06.png"),
          tags: ["春天", "秋天"],
          link: "closet_detail.html?id=6",
        },
        {
          id: 7,
          name: "墨鏡",
          category: "accessories",
          brand: "品牌C",
          price: 50,
          addedDate: "2024/06/07",
          image: "https://picsum.photos/300/200?random=6",
          tags: ["春天", "夏天"],
          link: "closet_detail.html?id=7",
        },
        {
          id: 8,
          name: "手錶",
          category: "accessories",
          brand: "品牌A",
          price: 200,
          addedDate: "2024/06/08",
          image: "https://picsum.photos/300/200?random=7",
          tags: ["全年"],
          link: "closet_detail.html?id=8",
        },
        {
          id: 9,
          name: "風衣",
          category: "coat",
          brand: "品牌B",
          price: 180,
          addedDate: "2024/06/09",
          image: "https://picsum.photos/300/200?random=8",
          tags: ["秋天", "冬天"],
          link: "closet_detail.html?id=9",
        },
        {
          id: 10,
          name: "連帽衫",
          category: "top",
          brand: "品牌C",
          price: 130,
          addedDate: "2024/06/10",
          image: "https://picsum.photos/300/200?random=9",
          tags: ["秋天", "冬天"],
          link: "closet_detail.html?id=10",
        },
        {
          id: 11,
          name: "T恤",
          category: "top",
          brand: "品牌E",
          price: 50,
          addedDate: "2024/06/11",
          image: "https://picsum.photos/300/200?random=12",
          tags: ["春天", "夏天"],
          link: "closet_detail.html?id=11",
        },
        {
          id: 12,
          name: "針織衫",
          category: "top",
          brand: "GU",
          price: 90,
          addedDate: "2024/06/12",
          image: "https://picsum.photos/300/200?random=1",
          tags: ["秋天"],
          link: "closet_detail.html?id=12",
        },
        {
          id: 13,
          name: "皮帶",
          category: "accessories",
          brand: "品牌F",
          price: 40,
          addedDate: "2024/06/13",
          image: "https://picsum.photos/300/200?random=13",
          tags: ["全年"],
          link: "closet_detail.html?id=13",
        },
        {
          id: 14,
          name: "運動褲",
          category: "bottom",
          brand: "品牌G",
          price: 60,
          addedDate: "2024/06/14",
          image: "https://picsum.photos/300/200?random=14",
          tags: ["春天", "夏天"],
          link: "closet_detail.html?id=14",
        },
        {
          id: 15,
          name: "棒球帽",
          category: "accessories",
          brand: "品牌H",
          price: 30,
          addedDate: "2024/06/15",
          image: "https://picsum.photos/300/200?random=15",
          tags: ["春天", "夏天"],
          link: "closet_detail.html?id=15",
        },
        {
          id: 16,
          name: "羽絨服",
          category: "coat",
          brand: "品牌I",
          price: 250,
          addedDate: "2024/06/16",
          image: "https://picsum.photos/300/200?random=16",
          tags: ["冬天"],
          link: "closet_detail.html?id=16",
        },
        {
          id: 17,
          name: "連身裙",
          category: "dress",
          brand: "品牌J",
          price: 110,
          addedDate: "2024/06/17",
          image: "https://picsum.photos/300/200?random=17",
          tags: ["春天", "夏天"],
          link: "closet_detail.html?id=17",
        },
        {
          id: 18,
          name: "短靴",
          category: "shoes",
          brand: "品牌K",
          price: 140,
          addedDate: "2024/06/18",
          image: "https://picsum.photos/300/200?random=18",
          tags: ["秋天", "冬天"],
          link: "closet_detail.html?id=18",
        },
        {
          id: 19,
          name: "牛仔外套",
          category: "coat",
          brand: "品牌L",
          price: 160,
          addedDate: "2024/06/19",
          image: "https://picsum.photos/300/200?random=19",
          tags: ["秋天", "冬天"],
          link: "closet_detail.html?id=19",
        },
        {
          id: 20,
          name: "手提包",
          category: "accessories",
          brand: "品牌M",
          price: 90,
          addedDate: "2024/06/20",
          image: "https://picsum.photos/300/200?random=20",
          tags: ["全年"],
          link: "closet_detail.html?id=20",
        },
      ],
    };
  },
  computed: {
    filteredItems() {
      let filteredItems = this.items.filter((item) => {
        const categoryMatch = this.selectedCategory === "all" || item.category === this.selectedCategory;
        const brandMatch = this.selectedBrand === "all" || item.brand === this.selectedBrand;
        return categoryMatch && brandMatch;
      });

      switch (this.sortBy) {
        case "newest":
          filteredItems.sort((a, b) => new Date(b.addedDate) - new Date(a.addedDate));
          break;
        case "oldest":
          filteredItems.sort((a, b) => new Date(a.addedDate) - new Date(b.addedDate));
          break;
        case "brand":
          filteredItems.sort((a, b) => a.brand.localeCompare(b.brand));
          break;
        case "price-low-high":
          filteredItems.sort((a, b) => a.price - b.price);
          break;
        case "price-high-low":
          filteredItems.sort((a, b) => b.price - a.price);
          break;
      }

      return filteredItems;
    },
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

/* 全局字體顏色，例如深灰色 */
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
