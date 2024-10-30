<template>
  <div>
    <WardrobeFilterAndSort :brands="brands" />
    <div class="d-flex justify-content-between align-items-center mb-3">
    <div class="item-info-wrap ms-auto">
      <router-link to="/closet_index" class="btn btn-outline-secondary me-2 mt-2">回衣櫃</router-link>
      <button @click="restoreItems" class="btn btn-outline-secondary me-2 mt-2">復原</button>
      <button @click="deleteItems" class="btn btn-outline-danger mt-2">永久刪除</button>
      </div>
    </div>
    <!-- 清單元件 -->
    <WardrobeList :items="items" :selectedItems="selectedItems" @update:selectedItems="updateSelectedItems" />
  </div>
</template>

<script>
  import { closetApiMixin } from "../mixins/closet_ApiMixin.js";
  import { closet_filterSortMixin } from "../mixins/closet_filterSortMixin.js";
  import WardrobeFilterAndSort from "../components/Wardrobe_FilterAndSort.vue";
  import WardrobeList from "../components/Wardrobe_List.vue";

  export default {
    mixins: [closetApiMixin, closet_filterSortMixin],
    components: {
      WardrobeFilterAndSort,
      WardrobeList,
    },
    data() {
      return {
        items: [],
        selectedItems: [], // 用於存放使用者選中的項目
      };
    },
    methods: {
      updateSelectedItems(newSelectedItems) {
        this.selectedItems = newSelectedItems;
      },
      async restoreItems() {
        if (this.selectedItems.length === 0) {
          alert("請選擇要復原的項目！");
          return;
        }
        try {
          await this.modifyItem("restore", this.selectedItems);
          alert("已成功復原所選項目");
          this.fetchItems("trash");
        } catch (error) {
          console.error("復原失敗:", error);
          alert("復原失敗");
        }
      },
      async deleteItems() {
        if (this.selectedItems.length === 0) {
          alert("請選擇要刪除的項目！");
          return;
        }
        try {
          await this.modifyItem("delete", this.selectedItems);
          alert("已永久刪除所選項目");
          this.fetchItems("trash");
        } catch (error) {
          console.error("刪除失敗:", error);
          alert("刪除失敗");
        }
      },
      goBack() {
        this.$router.go(-1);
      },
    },
    mounted() {
      this.fetchItems("trash");
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
