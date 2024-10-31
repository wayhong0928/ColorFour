<template>
  <div>
    <WardrobeFilterAndSort
      :brands="brands"
      :selectedCategory="selectedCategory"
      :selectedBrand="selectedBrand"
      :sortBy="sortBy"
      :favorites="favorites"
      @update:selectedCategory="updateSelectedCategory"
      @update:selectedBrand="updateSelectedBrand"
      @update:sortBy="updateSortBy"
      @update:favorites="updateFavorites"
    />
    <div class="d-flex justify-content-between align-items-center mb-3">
      <div class="item-info-wrap ms-auto">
        <router-link to="/closet_new" class="btn btn-outline-secondary me-2 mt-2">新增單品</router-link>
        <router-link to="/closet_new_outfit" class="btn btn-outline-secondary me-2 mt-2">新增穿搭組合</router-link>
        <router-link to="/closet_outfit_index" class="btn btn-outline-secondary me-2 mt-2">穿搭組合區</router-link>
        <button @click="moveItemsToTrash" class="btn btn-outline-danger me-2 mt-2">刪除單品</button>
        <router-link to="/closet_trash" class="btn btn-outline-danger me-2 mt-2">回收區</router-link>
      </div>
    </div>
    <WardrobeList :items="items" :selectedItems="selectedItems" @update:selectedItems="updateSelectedItems" />
  </div>
</template>

<script>
  import { closetApiMixin } from "../mixins/closet_ApiMixin.js";
  import { closet_filterSortMixin } from "../mixins/closet_filterSortMixin.js";
  import WardrobeFilterAndSort from "../components/Wardrobe_FilterAndSort.vue";
  import WardrobeList from "../components/Wardrobe_List.vue";
  import axios from "axios";

  export default {
    mixins: [closetApiMixin, closet_filterSortMixin],
    components: {
      WardrobeFilterAndSort,
      WardrobeList,
    },
    data() {
      return {
        items: [],
        selectedItems: [],
        favorites: "all",
      };
    },
    methods: {
      updateSelectedItems(newSelectedItems) {
        this.selectedItems = newSelectedItems;
      },
      updateSelectedCategory(newCategory) {
        this.selectedCategory = newCategory;
      },
      updateSelectedBrand(newBrand) {
        this.selectedBrand = newBrand;
      },
      updateSortBy(newSortBy) {
        this.sortBy = newSortBy;
      },
      updateFavorites(newFavorites) {
        this.favorites = newFavorites;
      },
      async moveItemsToTrash() {
      if (this.selectedItems.length === 0) {
        alert("請選擇要刪除的項目");
        return;
      }
      const confirmed = confirm("確定要將選中的單品移至回收區嗎？");
      if (!confirmed) return;
      try {
        await Promise.all(
          this.selectedItems.map((id) =>
            axios.post(`${process.env.VUE_APP_BACKEND_URL}/wardrobe/items/${id}/move_to_trash/`, {}, {
              headers: { Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}` },
            })
          )
        );
        // 刪除成功，更新頁面
        this.items = this.items.filter((item) => !this.selectedItems.includes(item.id));
        this.selectedItems = [];
        alert("選中單品已移至回收區");
      } catch (error) {
        console.error("移至垃圾桶失敗:", error);
        alert("移動失敗，請稍後再試。");
      }
    },
  },

    async mounted() {
      await this.fetchItems("overview"); // 獲取非垃圾桶中的項目
    },
  };
</script>

<style scoped>
  .container {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>
