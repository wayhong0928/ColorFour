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
  import exampleImage from "@/assets/img/suggest_04.png";

  export default {
    data() {
      return {
        items: [],
        selectedItems: [],
        outfitForm: {
          outfit_name: "",
          description: "",
        },
        brands: [],
        colors: [],
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

        try {
          const imageBase64 = await this.convertImageToBase64(exampleImage);

          const payload = {
            outfit_name: this.outfitForm.outfit_name,
            description: this.outfitForm.description,
            selected_items: this.selectedItems,
            outfit_image: imageBase64,
          };
          console.log("Creating outfit with payload:", payload);

          const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/outfits/`, payload, {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });

          alert("穿搭組合新增成功！");
          this.$router.push("/closet_outfit_index");
        } catch (error) {
          console.error("Error creating outfit:", error);
          alert("穿搭組合新增失敗，請稍後再試。");
        }
      },
      convertImageToBase64(imageSrc) {
        return new Promise((resolve, reject) => {
          const img = new Image();
          img.src = imageSrc;
          img.onload = () => {
            const canvas = document.createElement("canvas");
            canvas.width = img.width;
            canvas.height = img.height;
            const ctx = canvas.getContext("2d");
            ctx.drawImage(img, 0, 0);
            const dataURL = canvas.toDataURL("image/png");
            resolve(dataURL.split(",")[1]);
          };
          img.onerror = reject;
        });
      },
      goBack() {
        this.$router.go(-1);
      },
    },
    async mounted() {
      await this.fetchItems();
      await this.fetchMetadata();
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
