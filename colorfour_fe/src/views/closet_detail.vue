<template>
  <div>
    <main>
      <div class="item-info-wrap">
        <!-- 根據 isInTrash 狀態決定顯示的按鈕 -->
        <button class="btn btn-outline-secondary edit-button" @click="toggleEdit" v-if="item && !item.is_in_trash">編輯</button>
        <button class="btn btn-outline-secondary" @click="moveToTrash" v-if="item && !item.is_in_trash">移置垃圾桶</button>

        <!-- 如果項目在垃圾桶中，顯示復原和永久刪除按鈕 -->
        <button class="btn btn-outline-secondary edit-button" @click="restoreItem" v-if="item && item.is_in_trash">復原</button>
        <button class="btn btn-outline-danger" @click="deleteItem" v-if="item && item.is_in_trash">永久刪除</button>
      </div>
      <section class="container" v-if="item">
        <div class="favorite-icon" @click="toggleFavorite">
          <transition name="zoom" mode="out-in">
            <img v-if="isFavorite" :src="require('@/assets/img/愛了.png')" alt="已加入最愛" key="liked" />
            <img v-else :src="require('@/assets/img/未愛.png')" alt="未加入最愛" key="unliked" />
          </transition>
        </div>
        <!-- 檢查 item 是否存在 -->
        <div class="item-img">
          <img :src="item.photo_url" alt="服飾圖片" />
        </div>
        <div class="item-info" v-if="!isEditing">
          <h1>{{ item.item_name }}</h1>
          <p>品牌: {{ getBrandName(item.brand) }}</p>
          <p>價格: ${{ item.price }}</p>

          <!-- 判斷顯示服飾種類 -->
          <template v-if="isClothing">
            <p class="hashtag">服飾主要分類：{{ getCategoryName(item.main_category) }}</p>
            <p class="hashtag">服飾次要分類：{{ getSubCategoryName(item.sub_category) }}</p>
          </template>

          <!-- 判斷顯示鞋子種類 -->
          <template v-if="isShoe">
            <p class="hashtag">鞋子主要分類：{{ getShoeCategoryName(item.shoe_category) }}</p>
            <p class="hashtag">鞋子次要分類：{{ getShoeSubCategoryName(item.shoe_sub_category) }}</p>
          </template>

          <p class="hashtag">
            場合標籤：
            <span v-for="(occasion, index) in item.occasions" :key="occasion">
              #{{ getOccasionName(occasion) }}<span v-if="index < item.occasions.length - 1">, </span>
            </span>
          </p>
          <p class="hashtag">顏色：{{ getColorName(item.color) }}</p>
          <p class="added-date">加入日期: {{ formatDate(item.add_date) }}</p>
          <p class="edit-date">編輯時間: {{ formatDate(item.edit_date) }}</p>
        </div>

        <!-- 編輯模式 -->
        <div class="edit-form" v-else>
          <label>名稱:</label>
          <input v-model="editForm.item_name" />

          <label>品牌:</label>
          <select v-model="editForm.brand">
            <option v-for="brand in brands" :key="brand.id" :value="brand.id">
              {{ brand.name }}
            </option>
          </select>

          <label>價格:</label>
          <input v-model="editForm.price" type="number" />

          <label>主要分類:</label>
          <select v-model="editForm.main_category">
            <option v-for="category in categories" :key="category.id" :value="category.id">
              {{ category.name }}
            </option>
          </select>

          <label>次要分類:</label>
          <select v-model="editForm.sub_category">
            <option v-for="subCategory in subCategories" :key="subCategory.id" :value="subCategory.id">
              {{ subCategory.name }}
            </option>
          </select>

          <label>鞋子主要分類:</label>
          <select v-model="editForm.shoe_category">
            <option v-for="shoeCategory in shoeCategories" :key="shoeCategory.id" :value="shoeCategory.id">
              {{ shoeCategory.name }}
            </option>
          </select>

          <label>鞋子次要分類:</label>
          <select v-model="editForm.shoe_sub_category">
            <option v-for="shoeSubCategory in shoeSubCategories" :key="shoeSubCategory.id" :value="shoeSubCategory.id">
              {{ shoeSubCategory.name }}
            </option>
          </select>

          <label>顏色:</label>
          <select v-model="editForm.color">
            <option v-for="color in colors" :key="color.id" :value="color.id">
              {{ color.name }}
            </option>
          </select>

          <!-- 場合標籤編輯 -->
          <label>場合標籤:</label>
          <div>
            <div v-for="(selectedOccasion, index) in editForm.occasions" :key="selectedOccasion">
              <span class="badge bg-primary m-1">{{ getOccasionName(selectedOccasion) }}</span>
              <button @click="removeOccasion(index)" class="btn btn-sm btn-danger">移除</button>
            </div>
          </div>
          <div>
            <select v-model="newOccasion">
              <option v-for="occasion in occasions" :key="occasion.id" :value="occasion.id">
                {{ occasion.occasion_name }}
              </option>
            </select>
            <button @click="addOccasion" class="btn btn-sm btn-primary">新增場合</button>
          </div>

          <button class="btn btn-outline-secondary" @click="saveEdit">儲存</button>
        </div>
      </section>
      <button class="btn btn-outline-secondary" @click="goBack">返回</button>
    </main>
  </div>
</template>

<script>
    import axios from "axios";
  import { closetApiMixin } from "../mixins/closet_ApiMixin.js";
  import { closet_filterSortMixin } from "../mixins/closet_filterSortMixin.js";

  export default {
    mixins: [closetApiMixin, closet_filterSortMixin],
    props: ["id"],
    data() {
      return {
        item: null,
        isFavorite: false,
        isEditing: false,
        editForm: {
          item_name: "",
          brand: "",
          price: 0,
          main_category: "",
          sub_category: "",
          shoe_category: "",
          shoe_sub_category: "",
          color: "",
          occasions: [], // 用於存放選中的場合標籤
        },
        brands: [],
        categories: [],
        subCategories: [],
        shoeCategories: [],
        shoeSubCategories: [],
        colors: [],
        occasions: [], // 所有場合標籤選項
        newOccasion: "", // 用於存放新增的場合標籤
      };
    },
    computed: {
      // 判斷是否為服飾類別
      isClothing() {
        return this.item && this.item.main_category != 1;
      },
      // 判斷是否為鞋子類別
      isShoe() {
        return this.item && this.item.shoe_category != 1;
      },
    },
    methods: {
      async fetchItem() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${this.id}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.item = response.data;
        } catch (error) {
          console.error("Error fetching item:", error);
        }
      },
      async fetchMetadata() {
        // 獲取品牌、分類、顏色、場合等資料
        try {
          const [
            brandsResponse,
            categoriesResponse,
            subCategoriesResponse,
            shoeCategoriesResponse,
            shoeSubCategoriesResponse,
            colorsResponse,
            occasionsResponse,
          ] = await Promise.all([
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/brands/`),
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/categories/`),
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/subcategories/`),
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/shoes_categories/`),
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/shoes_subcategories/`),
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/colors/`),
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/occasions/`),
          ]);
          this.brands = brandsResponse.data;
          this.categories = categoriesResponse.data;
          this.subCategories = subCategoriesResponse.data;
          this.shoeCategories = shoeCategoriesResponse.data;
          this.shoeSubCategories = shoeSubCategoriesResponse.data;
          this.colors = colorsResponse.data;
          this.occasions = occasionsResponse.data;
        } catch (error) {
          console.error("Error fetching metadata:", error);
        }
      },
      toggleEdit() {
        this.isEditing = !this.isEditing;
        if (this.isEditing) {
          this.populateEditForm(); // 進入編輯模式時，填充 editForm
        }
      },
      populateEditForm() {
        this.editForm = {
          item_name: this.item.item_name,
          brand: this.item.brand,
          price: this.item.price,
          main_category: this.item.main_category,
          sub_category: this.item.sub_category,
          shoe_category: this.item.shoe_category,
          shoe_sub_category: this.item.shoe_sub_category,
          color: this.item.color,
          occasions: [...this.item.occasions],
        };
      },
      addOccasion() {
        if (this.newOccasion && !this.editForm.occasions.includes(this.newOccasion)) {
          this.editForm.occasions.push(this.newOccasion);
          this.newOccasion = "";
        }
      },
      removeOccasion(index) {
        this.editForm.occasions.splice(index, 1);
      },
      async saveEdit() {
        try {
          await axios.put(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${this.id}/`, this.editForm, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          // 更新 item 資料
          this.item = { ...this.item, ...this.editForm };
          this.isEditing = false;
        } catch (error) {
          console.error("Error saving item:", error);
        }
      },
      async restoreItem() {
        try {
          await this.modifyItem("restore", this.id);
          alert("項目已成功復原！");
          this.$router.push("/closet_trash");
        } catch (error) {
          console.error("復原失敗:", error);
          alert("復原失敗，請稍後再試。");
        }
      },
      async deleteItem() {
        try {
          const confirmed = confirm("永久刪除無法復原，確定要刪除嗎？");
          if (confirmed) {
            await this.modifyItem("delete", this.id);
            alert("項目已成功永久刪除！");
            this.$router.push("/closet_trash");
          }
        } catch (error) {
          console.error("永久刪除失敗:", error);
          alert("永久刪除失敗，請稍後再試。");
        }
      },
      async moveToTrash() {
        try {
          await this.modifyItem("move_to_trash", this.id);
          alert(`成功將 ${this.item.item_name} 移至垃圾桶`);
          this.$router.push("/closet_trash");
        } catch (error) {
          console.error("移置垃圾桶失敗:", error);
        }
      },
      async toggleFavorite() {
        try {
          if (this.isFavorite) {
            await this.modifyItem("remove_from_favorites", this.id);
            this.isFavorite = false;
            alert(`成功移除 ${this.item.item_name} 的最愛`);
          } else {
            await this.modifyItem("add_to_favorites", this.id);
            this.isFavorite = true;
            alert(`成功將 ${this.item.item_name} 加入最愛`);
          }
        } catch (error) {
          console.error("操作最愛狀態失敗:", error);
        }
      },

      getBrandName(brandId) {
        const brand = this.brands.find((b) => b.id === brandId);
        return brand ? brand.name : "未知品牌";
      },
      getCategoryName(categoryId) {
        const category = this.categories.find((c) => c.id === categoryId);
        return category ? category.name : "未知分類";
      },
      getSubCategoryName(subCategoryId) {
        const subCategory = this.subCategories.find((sc) => sc.id === subCategoryId);
        return subCategory ? subCategory.name : "未知次分類";
      },
      getShoeCategoryName(shoeCategoryId) {
        const shoeCategory = this.shoeCategories.find((sc) => sc.id === shoeCategoryId);
        return shoeCategory ? shoeCategory.name : "未知鞋子分類";
      },
      getShoeSubCategoryName(shoeSubCategoryId) {
        const shoeSubCategory = this.shoeSubCategories.find((ssc) => ssc.id === shoeSubCategoryId);
        return shoeSubCategory ? shoeSubCategory.name : "未知鞋子次分類";
      },
      getOccasionName(occasionId) {
        const occasion = this.occasions.find((o) => o.id === occasionId);
        return occasion ? occasion.occasion_name : "未知場合";
      },
      getColorName(colorId) {
        const color = this.colors.find((c) => c.id === colorId);
        return color ? color.name : "未知顏色";
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString(); // 格式化為日期+時間
      },
      goBack() {
        this.$router.go(-1);
      },
    },
    async created() {
      await this.fetchMetadata(); // 先抓取品牌、分類、顏色、場合等資料
      this.fetchItem(); // 再獲取具體 item
      this.isFavorite = false;
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

  .item-info-wrap .edit-button {
    margin-right: 20px; /* 增加按鈕之間的距離 */
  }

  main button {
    width: auto; /* 讓按鈕的寬度自適應內容 */
    text-align: center; /* 讓按鈕內的字置中 */
    padding: 10px 20px; /* 添加適當的內邊距讓按鈕看起來更大 */
    display: inline-flex;
    align-items: center; /* 水平置中 */
    justify-content: center; /* 垂直置中 */
    margin-top: 20px;
  }

  .favorite-icon {
    cursor: pointer;
    width: 90px;
    height: 90px;
    margin-bottom: 10px;
    position: absolute;
    top: 20px;
    right: 20px;
  }

  .favorite-icon img {
    width: 100%;
    height: auto;
    transition: transform 0.2s ease-in-out;
  }

  .zoom-enter-active,
  .zoom-leave-active {
    transition: transform 0.3s ease;
  }

  .zoom-enter, .zoom-leave-to /* .zoom-leave-active in <2.1.8 */ {
    transform: scale(0.8);
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
    padding:40px;
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

  .edit-form label {
    display: block;
    margin-top: 10px;
  }

  .edit-form input {
    width: 100%;
    padding: 5px;
    margin-top: 5px;
    border-radius: 10px;
  }

  .edit-form select{
    border-radius: 10px; /* 加大圓角 */
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
