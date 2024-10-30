<template>
  <div>
    <div class="d-flex justify-content-between align-items-center mb-3">
      <div class="item-info-wrap ms-auto">
        <router-link to="/closet_index" @click="goBack" class="btn btn-outline-secondary me-2 mt-2">回衣櫃</router-link>
        <router-link to="/closet_new_outfit" class="btn btn-outline-secondary me-2 mt-2"> 新增穿搭組合 </router-link>
        <button @click="deleteItems" class="btn btn-outline-danger mt-2">刪除穿搭組合</button>
      </div>
    </div>

    <div class="row" id="outfit-list">
      <div v-for="outfit in outfits" :key="outfit.id" class="card col-4 mb-3">
        <!-- 預設圖片 -->
        <img :src="outfit.outfit_image || defaultImage" class="card-img-top" :alt="outfit.outfit_name" />
        <div class="card-body">
          <h5 class="card-title">{{ outfit.outfit_name }}</h5>
          <p class="card-text">
            <small class="text-muted">建立日期: {{ formatDate(outfit.created_at) }}</small>
          </p>
          <router-link :to="{ name: 'closet_outfit_detail', params: { id: outfit.id } }" class="btn btn-outline-secondary">
            查看詳細
          </router-link>
        </div>
        <div class="form-check check-box-top-right">
          <input type="checkbox" class="form-check-input" v-model="selectedItems" :value="outfit.id" />
          <label class="form-check-label"></label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import { closet_filterSortMixin } from "../mixins/closet_filterSortMixin.js";
  import WardrobeFilterAndSort from "../components/Wardrobe_FilterAndSort.vue";
  import defaultImage from "@/assets/img/suggest_05.png";

  export default {
    mixins: [closet_filterSortMixin],
    components: {
      WardrobeFilterAndSort,
    },
    data() {
      return {
        outfits: [],
        selectedItems: [],
        defaultImage,
      };
    },
    methods: {
      async fetchOutfits() {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/outfits/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          console.log("Outfits fetched successfully:", response.data);
          this.outfits = response.data;
        } catch (error) {
          console.error("Error fetching outfits:", error);
        }
      },
      goBack() {
        this.$router.go(-1);
      },
      async deleteItems() {
        if (this.selectedItems.length === 0) {
          alert("請選擇要刪除的項目");
          return;
        }

        const confirmed = confirm("確定要刪除選中的穿搭組合嗎？");

        if (!confirmed) return;

        try {
          await Promise.all(
            this.selectedItems.map((id) =>
              axios.delete(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/outfits/${id}/`, {
                headers: {
                  Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
                },
              })
            )
          );

          alert("穿搭組合刪除成功");

          // 將已刪除的項目從畫面上移除
          this.outfits = this.outfits.filter((outfit) => !this.selectedItems.includes(outfit.id));

          // 清空選中的項目
          this.selectedItems = [];
        } catch (error) {
          console.error("Error deleting items:", error);
          alert("刪除失敗，請稍後再試。");
        }
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString();
      },
      defaultImage() {
        return defaultImage;
      },
    },
    async mounted() {
      await this.fetchOutfits();
    },
  };
</script>

<style scoped>
  .container {
    width: 90%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  .row .card {
    width: 45%;
    margin: 20px auto;
    display: flex;
  }

  .card-body {
    width: 100%;
    margin: 10px auto;
    display: flex;
    flex-direction: column;
  }

  .item-info-wrap .btn {
    margin-right: 10px;
  }

  .form-check {
    position: absolute;
    top: 10px;
    right: 10px;
  }

  @media (max-width: 768px) {
    .row .card {
      width: 90%;
      margin: 20px auto;
    }
  }
</style>
