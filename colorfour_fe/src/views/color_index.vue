<template>
  <div>
    <header></header>
    <main>
      <section class="container my-5">
        <div class="row mb-4">
          <div
            class="col-md-6 order-md-2 d-flex flex-column justify-content-center mx-auto"
            style="order: 2"
          >
            <h2 class="mb-3 my-heading">我的氣色</h2>
            <p class="mb-4">
              透過使用者在上傳自己的臉部色彩圖片後，系統會依照照片中的膚色、髮色與瞳色進行判別，以提供個人化四季型色彩分析建議，讓使用者了解自己適合的服飾顏色穿搭。
              色彩分析結果為春、夏、秋、冬四個季節的色彩型。
            </p>
            <div class="d-flex justify-content-between align-items-center mb-3">
              <div>
                <label for="sort-by" class="form-label">排序方式：</label>
                <select id="sort-by" class="form-select" v-model="sortBy">
                  <option value="newest">新增時間 (先到後)</option>
                  <option value="oldest">新增時間 (後到先)</option>
                </select>
              </div>
              <div>
                <button class="btn btn-outline-secondary" @click="addItem">新增</button>
                <button class="btn btn-outline-secondary" @click="removeItem">刪除</button>
              </div>
            </div>
            <div class="scroll-container mt-4">
              <div
                class="result-item"
                v-for="(item, index) in sortedItems"
                :key="index"
              >
                <span class="date">{{ item.date }}</span>
                {{ item.type }}型人<br />
                ☆ 若搭配了適合的顏色<br />
                ✓ {{ item.benefit1 }}<br />
                ✓ {{ item.benefit2 }}<br />
                ✓ {{ item.benefit3 }}<br />
                <router-link to="/color_detail" class=""><img src="@/assets/img/next_icon.png" class="icon" /></router-link>
              </div>
            </div>
          </div>
          <div class="col-md-6 order-md-1 position-relative">
            <div class="image-container">
              <img src="@/assets/img/makeup.png" class="img-fluid rounded" alt="線上衣櫃" />
              <div class="overlay1"></div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <footer></footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sortBy: "newest",
      items: [
        {
          date: "2023/11/24",
          type: "春季",
          benefit1: "臉部變得明亮",
          benefit2: "可呈現出血色感",
          benefit3: "看起來彈力有光澤、生氣蓬勃",
        },
        {
          date: "2023/12/25",
          type: "夏季",
          benefit1: "顯白、肌膚看起來變明亮",
          benefit2: "呈現出透明感",
          benefit3: "肌膚看起來光滑",
        },
        {
          date: "2024/01/06",
          type: "秋季",
          benefit1: "讓血色感變好",
          benefit2: "肌膚看起來像陶器般平滑",
          benefit3: "輪廓看起來更俐落",
        },
        {
          date: "2024/05/17",
          type: "冬季",
          benefit1: "看起來洗練俐落",
          benefit2: "緊緻輪廓",
          benefit3: "肌膚看起來有光澤",
        },
      ],
    };
  },
  computed: {
    sortedItems() {
      if (this.sortBy === "newest") {
        return this.items.slice().sort((a, b) => new Date(b.date) - new Date(a.date));
      } else {
        return this.items.slice().sort((a, b) => new Date(a.date) - new Date(b.date));
      }
    },
  },
  methods: {
    addItem() {
      // Add item logic here
      console.log("Add item");
    },
    removeItem() {
      // Remove item logic here
      console.log("Remove item");
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;300;400;500;700;900&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&display=swap");

:root {
  --primary-bg-color: #ffffff;
  --header-footer-bg-color: #e7d8c9;
  --divider-color: #ccc;
  --primary-text-color: #b2967d;
  --button-bg-color: #e6b5ae;
  --button-hover-bg-color: #d9a68c;
  --search-icon-color: #888;
}

/* Reset and global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Noto Sans TC", "Noto Sans", sans-serif;
  font-weight: 500;
}

html {
  width: 100%;
  min-height: 100%;
}

body {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: var(--primary-bg-color);
}

/* Header and navigation bar */
header {
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  background-color: var(--header-footer-bg-color);
}

.nav {
  width: 100%;
  display: flex;
  color: white;
  padding: 10px 0;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  z-index: 50;
}

.nav button {
  width: 20%;
  display: flex;
  justify-content: start;
  background-color: transparent;
  border-style: none;
}

.nav .nav-text {
  width: 150px;
  height: 50px;
  margin: 0 auto;
}

/* Sidebar */
.sidebar {
  width: 200px;
  background-color: #f0f0f0;
  padding: 20px;
  display: none;
  position: fixed;
  top: 70px;
  right: 0;
  height: calc(100% - 120px);
  overflow-y: auto;
  z-index: 10;
}

.sidebar-divider {
  border: 0;
  height: 1px;
  margin: 20px 0;
  background-color: var(--divider-color);
}

.sidebar.show {
  display: block;
}

.member-photo {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin: 20px auto;
}

.page-links {
  margin-top: 20px;
}

.page-links a {
  display: block;
  margin-bottom: 10px;
  text-decoration: none;
  color: var(--primary-text-color);
}

.page-links a:hover {
  text-decoration: underline;
}

/* main */
main {
  width: 90%;
  margin: 100px auto;
  position: relative;
  flex: 1;
}

.btn-primary {
  background-color: #e6b5ae;
  border-color: #e6b5ae;
  border-radius: 20px;
  padding: 5px 10px;
  text-decoration: none;
  color: #fff;
  display: inline-block;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #f9d9ca; /* Change background color on hover */
  border: #f9d9ca;
}

/* Footer */
.footer {
  width: 100%;
  height: 70px;
  position: fixed;
  bottom: 0;
  left: 0;
  background-color: var(--header-footer-bg-color);
  color: white;
  padding: 10px 0;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
  z-index: 100;
  text-align: center;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
}

.footer-col {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

.footer-col a {
  color: white;
  margin: 0 10px;
  text-decoration: none;
}

.footer-col a img {
  vertical-align: middle;
}

/* 一般樣式 */
body {
  font-family: Arial, sans-serif;
}

.scroll-container {
  width: 90%;
  max-width: 500px;
  height: 400px;
  overflow-y: auto;
  background-color: #fafafa;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.scroll-container::-webkit-scrollbar {
  width: 8px;
}

.scroll-container::-webkit-scrollbar-thumb {
  background-color: #ccc;
  border-radius: 4px;
}

.scroll-container::-webkit-scrollbar-track {
  background-color: #f1f1f1;
}

.my-heading {
  color: #917b56; /* 替換為你想要的顏色 */
}

.result-item {
  display: flex;
  flex-direction: column; /* 改變成縱向排列 */
  margin-bottom: 10px;
  padding: 10px;
  font-size: 16px;
  background-color: #ffffff;
  border: 1px solid #ccc;
  border-radius: 5px;
  transition: background-color 0.3s, transform 0.3s;
  color: #333;
  
}

.result-item:hover {
  background-color: #f1f1f1;
  transform: translateY(-3px);
  cursor: pointer;
}

.result-item .date {
  background-color: #e6b5ae;
  color: white;
  padding: 2px 8px;
  border-radius: 5px;
  margin-right: 10px;
}

.result-item .icon {
  margin-left: 15px;
  width: 20px;
  height: 20px;
}

.btn-secondary {
  background-color: #e6b5ae;
  border-color: #e6b5ae;
  border-radius: 20px;
  padding: 5px 10px;
  text-decoration: none;
  color: #fff;
  display: inline-block;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-secondary:hover {
  background-color: #f9d9ca;
  border: #f9d9ca;
}

.image-container {
  position: relative;
  display: inline-block;
}

.image-container img {
  display: block;
  border-radius: 10px;
}

.image-container .overlay1 {
  position: absolute;
  z-index: -1;
  border-radius: 10px;
  top: 150px;
  left: -100px;
  width: 100%;
  height: 80%;
  background-color: #4f4845;
}

.image-container .overlay1::after {
  content: "";
  position: absolute;
  top: -200px;
  left: 50px;
  width: 60%;
  height: 100%;
  border: 3px solid #baa189;
  border-radius: 10px;
  z-index: -1;
}

/* 響應式樣式 */
@media (max-width: 425px) {

  .image-container .overlay1 {
    top: 140px;
  }

  .image-container .overlay1::after {
    top: -200px;
  }

  .col-md-6.order-md-2.d-flex.flex-column.justify-content-center.mx-auto {
    order: 2;
    margin-top: 95px;
    margin-bottom: 20px;
  }
}

</style>