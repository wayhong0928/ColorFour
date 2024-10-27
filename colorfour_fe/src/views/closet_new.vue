<template>
  <div>
    <header id="header"></header>
    <div class="container mt-5">
      <h1>新增單品</h1>
      <form @submit.prevent="handleSubmit">
        <div class="mb-3">
          <label for="itemName" class="form-label">商品名稱</label>
          <input type="text" class="form-control" v-model="item.item_name" id="itemName" placeholder="輸入商品名稱" required />
        </div>

        <!-- 新增選擇服飾或鞋子的區域 -->
        <div>
          <label for="itemType" class="form-label">選擇類型:</label>
          <select v-model="item.type" @change="onTypeChange" required>
            <option value="" disabled>請選擇</option>
            <option value="服飾">服飾</option>
            <option value="鞋子">鞋子</option>
          </select>
        </div>

        <!-- 服飾主要類別 -->
        <div v-if="item.type === '服飾'">
          <label for="main_category" class="form-label">服飾主要類別:</label>
          <select v-model="item.main_category" @change="fetchSubCategories" required>
            <option v-for="category in mainCategories" :key="category.id" :value="category.id">
              {{ category.name }}
            </option>
          </select>
        </div>

        <!-- 服飾次要類別 -->
        <div v-if="item.type === '服飾' && subCategories.length > 0">
          <label for="sub_category" class="form-label">服飾次要類別:</label>
          <select v-model="item.sub_category" required>
            <option v-for="subCategory in subCategories" :key="subCategory.id" :value="subCategory.id">
              {{ subCategory.name }}
            </option>
          </select>
        </div>

        <!-- 鞋子主要類別 -->
        <div v-if="item.type === '鞋子'">
          <label for="shoe_category" class="form-label">鞋子主要類別:</label>
          <select v-model="item.shoe_category" @change="fetchShoeSubCategories" required>
            <option v-for="shoeCategory in shoeCategories" :key="shoeCategory.id" :value="shoeCategory.id">
              {{ shoeCategory.name }}
            </option>
          </select>
        </div>

        <!-- 鞋子次要類別 -->
        <div v-if="item.type === '鞋子' && shoeSubCategories.length > 0">
          <label for="shoe_sub_category" class="form-label">鞋子次要類別:</label>
          <select v-model="item.shoe_sub_category" required>
            <option v-for="shoeSubCategory in shoeSubCategories" :key="shoeSubCategory.id" :value="shoeSubCategory.id">
              {{ shoeSubCategory.name }}
            </option>
          </select>
        </div>

        <!-- 品牌下拉清單 -->
        <div class="mb-3">
          <label for="itemBrand" class="form-label">品牌</label>
          <select v-model="item.brand" id="itemBrand" class="form-control" required>
            <option v-for="brand in brands" :key="brand.id" :value="brand.id">
              {{ brand.name }}
            </option>
          </select>
        </div>

        <!-- 顏色下拉清單 -->
        <div class="mb-3">
          <label for="itemColor" class="form-label">顏色</label>
          <select v-model="item.color" id="itemColor" class="form-control" required>
            <option v-for="color in colors" :key="color.id" :value="color.id">
              {{ color.name }}
            </option>
          </select>
        </div>

        <div class="mb-3">
          <label for="itemPrice" class="form-label">價格</label>
          <input type="number" class="form-control" v-model="item.price" id="itemPrice" placeholder="輸入價格" required />
        </div>
        <div class="mb-3">
          <label>內容:</label>
          <input type="text" class="form-control" v-model="item.content" placeholder="請輸入內容" />
        </div>

        <!-- 場合選項 -->
        <div class="mb-3">
          <label for="occasion" class="form-label">場合/目的</label>
          <div id="occasion-tags" class="border p-3 mb-3">
            <span v-for="(tag, index) in item.selectedOccasions" :key="index" class="badge bg-secondary m-1">
              {{ tag.name }} <button type="button" class="btn-close btn-close-white" @click="removeOccasion(index)"></button>
            </span>
          </div>
          <div id="occasion" class="btn-group flex-wrap" role="group">
            <button
              type="button"
              class="btn btn-outline-secondary m-1"
              v-for="occasion in occasions"
              :key="occasion.id"
              @click="addOccasion(occasion)"
            >
              {{ occasion.occasion_name }}
            </button>
          </div>
        </div>

        <div class="mb-3">
          <label>購買日期</label>
          <input type="date" class="from-control" v-model="item.purchase_date" placeholder="請輸入購買日期" />
        </div>
        <div class="mb-3">
          <label>購買地點:</label>
          <input type="text" class="form-control" v-model="item.purchase_link" placeholder="請輸入購買地點" />
        </div>
        <div class="mb-3">
          <label for="photo_url" class="form-label">上傳圖片</label>
          <input type="file" class="form-control" id="photo_url" accept="image/*" @change="handleImageUpload" required />
          <button type="button" class="btn btn-outline-primary mt-2" @click="openCamera">開啟相機</button>
        </div>
        <div class="submit-section">
          <button type="submit" class="btn btn-primary mb-1" :disabled="submitting">新增單品</button>
          <button class="back-button" @click="goBack">返回</button>
        </div>
      </form>
    </div>

    <div class="zone"></div>
    <footer id="footer"></footer>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        item: {
          item_name: "",
          brand: "",
          price: 0,
          type: "",
          main_category: 1,
          sub_category: 1,
          shoe_category: 1,
          shoe_sub_category: 1,
          color: "",
          tags: "",
          content: "",
          purchase_link: "",
          photo_url: null,
        },
        submitting: false,
        selectedOccasions: [],
        mainCategories: [], // 服飾主要類別
        subCategories: [], // 服飾次要類別
        shoeCategories: [], // 鞋子主要類別
        shoeSubCategories: [], // 鞋子次要類別
        brands: [], // 品牌列表
        colors: [], // 顏色列表
        occasions: [], // 場合列表
      };
    },
    async mounted() {
      await this.fetchCategories(); // 讀取類別
      await this.fetchBrands(); // 讀取品牌
      await this.fetchColors(); // 讀取顏色
      await this.fetchOccasions(); // 讀取場合
    },
    methods: {
      async fetchCategories() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/categories/`);
          this.mainCategories = response.data; // 服飾主要類別
          console.log("服飾主要類別:", this.mainCategories);
          const shoeResponse = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/shoes_categories/`);
          this.shoeCategories = shoeResponse.data; // 鞋子主要類別
          console.log("鞋子主要類別:", this.shoeCategories);
        } catch (error) {
          console.error("無法讀取類別:", error);
        }
      },
      async fetchBrands() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/brands/`);
          this.brands = response.data; // 品牌列表
          console.log("品牌列表:", this.brands);
        } catch (error) {
          console.error("無法讀取品牌列表:", error);
        }
      },
      async fetchColors() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/colors/`);
          this.colors = response.data; // 顏色列表
          console.log("顏色列表:", this.colors);
        } catch (error) {
          console.error("無法讀取顏色列表:", error);
        }
      },
      async fetchSubCategories() {
        if (this.item.main_category) {
          try {
            const response = await axios.get(
              `${process.env.VUE_APP_BACKEND_URL}/wardrobe/subcategories/?main_category=${this.item.main_category}`
            );
            this.subCategories = response.data;
            console.log("次要類別:", this.subCategories);
          } catch (error) {
            console.error("無法讀取次要類別:", error);
          }
        } else {
          this.subCategories = [];
        }
      },
      async fetchShoeSubCategories() {
        if (this.item.shoe_category) {
          try {
            const response = await axios.get(
              `${process.env.VUE_APP_BACKEND_URL}/wardrobe/shoes_types/?shoe_category=${this.item.shoe_category}`
            );
            this.shoeSubCategories = response.data;
            console.log("鞋子次要類別:", this.shoeSubCategories);
          } catch (error) {
            console.error("無法讀取鞋子次要類別:", error);
          }
        } else {
          this.shoeSubCategories = [];
        }
      },
      async fetchOccasions() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/occasions/`);
          this.occasions = response.data; // 場合選項
          console.log("場合列表:", this.occasions);
        } catch (error) {
          console.error("無法讀取場合列表:", error);
        }
      },
      addOccasion(occasion) {
        if (!this.item.selectedOccasions) {
          this.item.selectedOccasions = [];
        }
        // 確認 occasion 尚未被選擇，然後將 occasion（包含id和name）加入
        if (!this.item.selectedOccasions.find((o) => o.id === occasion.id)) {
          this.item.selectedOccasions.push({
            id: occasion.id,
            name: occasion.occasion_name,
          });
          console.log("已選擇場合:", this.item.selectedOccasions);
        }
      },
      removeOccasion(index) {
        this.item.selectedOccasions.splice(index, 1);
      },
      async handleSubmit() {
        this.submitting = true;
        const occasionIds = this.item.selectedOccasions.map((occasion) => occasion.id);
        if (this.item.type === "服飾") {
          if (!this.item.main_category || !this.item.sub_category) {
            alert("請選擇服飾的主要類別和次要類別！");
            return;
          }
        } else if (this.item.type === "鞋子") {
          if (!this.item.shoe_category || !this.item.shoe_sub_category) {
            alert("請選擇鞋子的主要類別和次要類別！");
            return;
          }
        } else {
          alert("請選擇類型！");
          return;
        }

        const formData = new FormData();
        formData.append("item_name", this.item.item_name);
        formData.append("brand",  this.item.brand);
        formData.append("price", this.item.price);
        formData.append("content", this.item.content);
        formData.append("photo_url", this.item.photo_url);
        formData.append("color", this.item.color);
        formData.append("purchase_date", this.item.purchase_date);
        formData.append("purchase_link", this.item.purchase_link);
        formData.append("main_category", this.item.main_category ? this.item.main_category : 1);
        formData.append("sub_category", this.item.sub_category ? this.item.sub_category : 1);
        formData.append("shoe_category", this.item.shoe_category ? this.item.shoe_category : 1);
        formData.append("shoe_sub_category", this.item.shoe_sub_category ? this.item.shoe_sub_category : 1);
        occasionIds.forEach((id) => formData.append("occasions", id));

        for (let pair of formData.entries()) {
          console.log(`${pair[0]}, ${pair[1]}`);
        }

        try {
          const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/`, formData, {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          alert("Item successfully created!");
          this.$router.push({ path: "/closet_index" });
        } catch (error) {
          console.error("錯誤回應:", error.response);
          alert(error.response.data.message || "新增失敗！");
        }
        this.submitting = false;
      },
      handleImageUpload(event) {
        this.item.photo_url = event.target.files[0];
      },
      openCamera() {
        const cameraInput = document.createElement("input");
        cameraInput.type = "file";
        cameraInput.accept = "image/*";
        cameraInput.capture = "camera";
        cameraInput.click();

        cameraInput.onchange = (event) => {
          const file = event.target.files[0];
          if (file) {
            this.item.image = file;
            alert("照片已拍攝並選擇");
          }
        };
      },
      goBack() {
        this.$router.go(-1);
      },
      // 選擇服飾或鞋子時清空次要類別
      onTypeChange() {
        if (this.item.type === "服飾") {
          this.item.shoe_category = null;
          this.item.shoe_sub_category = null;
          this.shoeSubCategories = [];
        } else if (this.item.type === "鞋子") {
          this.item.main_category = null;
          this.item.sub_category = null;
          this.subCategories = [];
        }
      },
    },
  };
</script>

<style scoped>
  h1 {
    margin-bottom: 30px;
  }

  .submit-section {
    text-align: center;
    margin: 20px 0;
  }

  .submit-section button {
    padding: 10px 20px;
    background-color: #d4b7a1;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    margin: 0 10px;
  }
</style>
