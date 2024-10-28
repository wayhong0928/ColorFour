<template>
  <div class="container mt-5">
    <h2>新增穿搭組合</h2>
    <form @submit.prevent="createOutfit">
      <div class="mb-3">
        <label for="outfitName" class="form-label">穿搭名稱</label>
        <input v-model="outfitForm.outfit_name" id="outfitName" class="form-control" required />
      </div>

      <div class="mb-3">
        <label for="outfitDescription" class="form-label">描述</label>
        <textarea v-model="outfitForm.description" id="outfitDescription" class="form-control"></textarea>
      </div>

      <div class="mb-3">
        <label class="form-label">選擇單品</label>
        <ul class="list-group">
          <li v-for="item in items" :key="item.id" class="list-group-item d-flex justify-content-between align-items-center">
            {{ item.item_name }} - {{ getBrandName(item.brand) }} - {{ getColorName(item.color) }}
            <input type="checkbox" :value="item.id" v-model="selectedItems" />
          </li>
        </ul>
      </div>

      <button type="submit" class="btn btn-primary">新增穿搭組合</button>
      <button @click="goBack" class="btn btn-outline-secondary ms-3">返回</button>
    </form>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        items: [], // 儲存所有單品
        selectedItems: [], // 已選擇的單品ID
        outfitForm: {
          outfit_name: "",
          description: "",
        },
        brands: [], // 儲存品牌資料
        colors: [], // 儲存顏色資料
      };
    },
    methods: {
      async fetchItems() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/overview/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.items = response.data;
        } catch (error) {
          console.error("Error fetching items:", error);
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
      async createOutfit() {
        if (this.selectedItems.length < 2) {
          alert("請選擇至少兩個單品！");
          return;
        }
        // TODO 把腳本預設的圖片丟上去
        try {
          const response = await axios.post(
            `${process.env.VUE_APP_BACKEND_URL}/wardrobe/outfits/`,
            {
              outfit_name: this.outfitForm.outfit_name,
              description: this.outfitForm.description,
              selected_items: this.selectedItems,
            },
            {
              headers: {
                Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
              },
            }
          );

          alert("穿搭組合新增成功！");
          this.$router.push("/closet_outfit_index");
        } catch (error) {
          console.error("Error creating outfit:", error);
          alert("穿搭組合新增失敗，請稍後再試。");
        }
      },
      goBack() {
        this.$router.go(-1);
      },
    },
    async mounted() {
      await this.fetchItems(); // 載入所有單品資料
      await this.fetchMetadata(); // 載入品牌和顏色資料
    },
  };
</script>

<style scoped>
  .container {
    max-width: 600px;
    margin: 0 auto;
  }
  .list-group-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
</style>
