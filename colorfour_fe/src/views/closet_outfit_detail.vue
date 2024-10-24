<template>
  <div>
    <main>
      <nav aria-label="breadcrumb">
        <ol class="bread">
          <li><router-link to="/">首頁</router-link></li>
          <li><router-link to="/closet_index">穿搭組合總覽</router-link></li>
          <li aria-current="page">穿搭組合詳情</li>
        </ol>
      </nav>

      <div class="item-info-wrap">
        <button class="btn btn-outline-secondary edit-button" @click="toggleEdit">編輯穿搭</button>
        <button class="btn btn-outline-danger" @click="deleteOutfit">刪除穿搭</button>
      </div>

      <section class="container" v-if="outfit">
        <div class="item-img">
          <!-- 找一張預設的圖片擺上去 -->
          <img :src="outfit.outfit_image || 'https://picsum.photos/300/200?random=1'" alt="穿搭圖片" />
        </div>
        <div class="item-info" v-if="!isEditing">
          <h1>{{ outfit.outfit_name }}</h1>
          <p>{{ outfit.description }}</p>
          <p class="added-date">建立日期: {{ formatDate(outfit.created_at) }}</p>

          <h5>包含的物品：</h5>
          <ul>
            <li v-for="item in outfit.items" :key="item.id">
              {{ item.item_name }} - {{ getBrandName(item.brand) }} - {{ getColorName(item.color) }}
            </li>
          </ul>
        </div>

        <!-- 編輯模式 -->
        <div class="edit-form" v-else>
          <label>名稱:</label>
          <input v-model="editForm.outfit_name" />

          <label>描述:</label>
          <input v-model="editForm.description" />

          <button class="btn btn-outline-secondary" @click="saveEdit">儲存</button>
        </div>
      </section>

      <button class="btn btn-outline-secondary" @click="goBack">返回上一頁</button>
    </main>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    props: ["id"],
    data() {
      return {
        outfit: null, // 存放穿搭資料
        brands: [], // 儲存品牌資料
        colors: [], // 儲存顏色資料
        isEditing: false, // 編輯模式切換
        editForm: {
          outfit_name: "",
          description: "",
        },
      };
    },
    methods: {
      async fetchOutfit() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/outfits/${this.id}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.outfit = response.data;
          console.log("Outfit fetched successfully:", this.outfit);
          this.editForm = { ...this.outfit };
        } catch (error) {
          console.error("Error fetching outfit:", error);
        }
      },
      async fetchMetadata() {
        try {
          const [brandsResponse, colorsResponse] = await Promise.all([
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/brands/`),
            axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/colors/`),
          ]);
          this.brands = brandsResponse.data;
          this.colors = colorsResponse.data;
        } catch (error) {
          console.error("Error fetching metadata:", error);
        }
      },
      getBrandName(brandId) {
        const brand = this.brands.find((b) => b.id === brandId);
        return brand ? brand.name : "未知品牌";
      },
      getColorName(colorId) {
        const color = this.colors.find((c) => c.id === colorId);
        return color ? color.name : "未知顏色";
      },
      toggleEdit() {
        this.isEditing = !this.isEditing;
      },
      async saveEdit() {
        try {
          const response = await axios.put(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/outfits/${this.id}/`, this.editForm, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.outfit = response.data;
          this.isEditing = false;
          alert("更新成功");
        } catch (error) {
          console.error("Error saving outfit:", error);
          alert("更新失敗");
        }
      },
      async deleteOutfit() {
        const confirmed = confirm("確定要刪除嗎？");
        if (!confirmed) return;

        try {
          await axios.delete(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/outfits/${this.id}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          alert("穿搭已刪除");
          this.$router.push("/closet_index");
        } catch (error) {
          console.error("Error deleting outfit:", error);
        }
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString();
      },
      goBack() {
        this.$router.go(-1);
      },
    },
    async mounted() {
      await this.fetchMetadata(); // 先抓取品牌和顏色資料
      await this.fetchOutfit(); // 再載入穿搭詳細資料
    },
  };
</script>

<style scoped>
  /* 保持樣式一致 */
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

  .item-info-wrap {
    width: 90%;
    display: flex;
    align-items: end;
    justify-content: end;
    margin-bottom: 20px;
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

  .container {
    min-height: 400px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    background-color: #e9e8e8;
    padding: 20px;
    border-radius: 20px;
  }

  .item-img {
    width: 45%;
    height: 45%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .item-img img {
    max-width: 100%;
    max-height: 100%;
    border-radius: 20px;
  }

  .item-info {
    width: 50%;
    margin-left: 20px;
  }

  .edit-form label {
    display: block;
    margin-top: 10px;
  }

  .edit-form input {
    width: 100%;
    padding: 5px;
    margin-top: 5px;
  }
</style>
