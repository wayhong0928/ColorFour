<template>
  <div>
    <main>
      <section class="container my-5">
        <div class="row mb-4">
          <div class="col-md-6 order-md-2 d-flex flex-column justify-content-center mx-auto" style="order: 2">
            <h2 class="mb-3 my-heading">我的氣色</h2>
            <p class="mb-4">
              透過使用者在上傳自己的臉部色彩圖片後，系統會依照照片中的膚色、髮色與瞳色進行判別，
              提供個人化四季型色彩分析建議，讓使用者了解自己適合的服飾顏色穿搭。色彩分析結果為春、夏、秋、冬四個季節的色彩型。
            </p>
            <div class="d-flex justify-content-between align-items-center mb-3">
              <div>
                <label for="sort-by" class="form-label">排序方式：</label>
                <select id="sort-by" class="form-select" v-model="sortBy">
                  <option value="newest">新增時間 (先到後)</option>
                  <option value="oldest">新增時間 (後到先)</option>
                </select>
              </div>
              <div class="item-info-wrap">
                <router-link to="/color_test">
                  <button class="btn btn-outline-secondary">一般分析</button>
                </router-link>
                <router-link to="/color_test_auto">
                  <button class="btn btn-outline-secondary" @click="handleAutomatedAnalysis">自動分析</button>
                </router-link>
                <button class="btn btn-outline-secondary" @click="removeSelectedItems">刪除</button>
              </div>
            </div>

            <div v-if="items.length > 0" class="scroll-container mt-4">
              <div class="result-item" v-for="(item, index) in sortedItems" :key="item.id">
                <div class="d-flex justify-content-between align-items-center">
                  <span class="date"> {{ item.test_name }} 的測驗結果：{{ item.result_type }}</span>
                  <input type="checkbox" class="form-check-input" v-model="selectedItems" :value="item.id" />
                </div>
                測驗時間：{{ formatDate(item.test_date) }}
                <br />
                <router-link :to="{ path: `color_detail/${item.id}/` }">
                  <img src="@/assets/img/next_icon.png" class="icon" />
                </router-link>
              </div>
            </div>

            <div v-else class="no-data">尚無測驗資料，請進行測驗後再查看。</div>
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
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        items: [],
        selectedItems: [],
        sortBy: "newest",
      };
    },
    computed: {
      sortedItems() {
        return this.sortBy === "newest"
          ? this.items.slice().sort((a, b) => new Date(b.test_date) - new Date(a.test_date))
          : this.items.slice().sort((a, b) => new Date(a.test_date) - new Date(b.test_date));
      },
    },
    methods: {
      async fetchItems() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/color/user-tests/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.items = response.data;
          console.log("測驗結果載入成功:", this.items);
        } catch (error) {
          console.error("無法載入測驗結果:", error.response);
        }
      },
      async deleteTest(id) {
        try {
          await axios.delete(`${process.env.VUE_APP_BACKEND_URL}/color/user-tests/${id}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.fetchItems();
        } catch (error) {
          console.error("無法刪除測驗:", error.response);
        }
      },
      removeSelectedItems() {
        this.selectedItems.forEach((id) => this.deleteTest(id));
        this.selectedItems = [];
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString();
      },
    },
    mounted() {
      this.fetchItems();
    },
  };
</script>

<style scoped>
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
    color: #917b56;
  }

  .result-item {
    display: flex;
    flex-direction: column;
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
    flex: 1;
  }

  .result-item .icon {
    margin-left: 15px;
    width: 20px;
    height: 20px;
  }

  /* 按鈕之間的間距 */
  .item-info-wrap .btn {
    margin: 5px;
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
