<template>
  <div>
    <main>
      <section class="container my-5">
        <div class="row mb-4">
          <!-- 內容區塊 -->
          <div class="col-md-6 order-md-2 d-flex flex-column justify-content-center mx-auto" style="order: 2">
            <h2 class="mb-3 my-heading">我的氣色</h2>
            <p class="mb-4">
              透過使用者在上傳自己的臉部色彩圖片後，系統會依照照片中的膚色、髮色與瞳色進行判別，
              以提供個人化四季型色彩分析建議，讓使用者了解自己適合的服飾顏色穿搭。色彩分析結果為春、夏、秋、冬四個季節的色彩型。
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
                  <button class="btn btn-outline-secondary">新增</button>
                </router-link>
                <button class="btn btn-outline-secondary" @click="removeSelectedItems">刪除</button>
              </div>
            </div>

            <!-- 資料列表 -->
            <div v-if="items.length > 0" class="scroll-container mt-4">
              <div class="result-item" v-for="(item, index) in sortedItems" :key="index">
                <div class="d-flex justify-content-between align-items-center">
                  <span class="date">{{ item.date }}</span>
                  <input type="checkbox" class="form-check-input" v-model="selectedItems" :value="index" />
                </div>
                {{ item.type }}型人<br />
                ☆ 若搭配了適合的顏色<br />
                ✓ {{ item.benefit1 }}<br />
                ✓ {{ item.benefit2 }}<br />
                ✓ {{ item.benefit3 }}<br />
                <router-link :to="item.link">
                  <img src="@/assets/img/next_icon.png" class="icon" />
                </router-link>
              </div>
            </div>

            <!-- 無資料提示 -->
            <div v-else class="no-data">
              尚無測驗資料，請進行測驗後再查看。
            </div>
          </div>

          <!-- 圖片展示區 -->
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
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  data() {
    return {
      sortBy: 'newest',
      selectedItems: [],
      items: [],
    };
  },
  computed: {
    sortedItems() {
      return this.sortBy === 'newest'
        ? this.items.slice().sort((a, b) => new Date(b.test_date) - new Date(a.test_date))
        : this.items.slice().sort((a, b) => new Date(a.test_date) - new Date(b.test_date));
    },
  },
  methods: {
async fetchItems() {
  try {
    const token = sessionStorage.getItem('token');
    if (!token) {
      throw new Error('無法取得 Token，請重新登入');
    }

    const response = await axios.get('http://127.0.0.1:8000/color/user-tests/', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    // 確保 response 存在且具有 data 和 status
    if (response && response.data && response.status === 200) {
      this.items = response.data.length > 0 ? response.data : [];
      console.log('資料取得成功', this.items);
    } else {
      console.warn('API 回應無資料或異常', response?.status);
      this.items = []; // 設為空，避免渲染錯誤
    }
  } catch (error) {
    const toast = useToast();
    if (error.response) {
      console.error('API 回應錯誤:', error.response);
      toast.error(`錯誤：${error.response.data.detail || '無法取得測驗紀錄'}`);
    } else if (error.request) {
      console.error('無法連接至 API:', error.request);
      toast.error('無法連接至伺服器，請稍後再試');
    } else {
      console.error('未知錯誤:', error.message);
      toast.error('發生未知錯誤，請重新登入');
    }
  }
},

    removeSelectedItems() {
      this.selectedItems.forEach(index => {
        this.items.splice(index, 1);
      });
      this.selectedItems = [];
    },
  },
  mounted() {
    const token = sessionStorage.getItem('token');
    console.log('Token in color_index.vue:', token);

    if (!token) {
      this.$router.push('/login');
    } else {
      this.fetchItems();
    }
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
    margin-right: 10px;
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
