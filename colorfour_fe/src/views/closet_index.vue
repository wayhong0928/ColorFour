<template>
  <div>
    <WardrobeFilterAndSort :brands="brands" />
    <div class="d-flex justify-content-between align-items-center mb-3">
      <div>
        <router-link to="/closet_new" class="btn btn-outline-secondary me-2">新增單品</router-link>
        <router-link to="/closet_trash" class="btn btn-outline-secondary">回收區</router-link>
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
      // 更新選中的項目
      updateSelectedItems(newSelectedItems) {
        this.selectedItems = newSelectedItems;
      },
      goBack() {
        this.$router.go(-1);
      },
    },
    mounted() {
      this.fetchItems("overview"); // 獲取非垃圾桶中的項目
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
