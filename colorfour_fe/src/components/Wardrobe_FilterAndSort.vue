<template>
  <main>
    <div class="filter-sort">
      <h2 class="filter-title">篩選</h2>

      <label for="category" class="form-label">分類:</label>
      <select v-model="selectedCategory" @change="applyFiltersAndSorting" class="form-select">
        <option value="all">全部</option>
        <option value="clothing">服飾</option>
        <option value="shoes">鞋子</option>
      </select>

      <label for="brand" class="form-label">品牌:</label>
      <select v-model="selectedBrand" @change="applyFiltersAndSorting" class="form-select">
        <option value="all">全部</option>
        <option v-for="brand in brands" :key="brand.id" :value="brand.id">
          {{ brand.name }}
        </option>
      </select>

      <label for="sort-by" class="form-label">排序方式:</label>
      <select v-model="sortBy" @change="applyFiltersAndSorting" class="form-select">
        <option value="newest">新增時間 (先到後)</option>
        <option value="oldest">新增時間 (後到先)</option>
        <option value="brand">品牌名稱</option>
        <option value="price-low-high">價格 (低到高)</option>
        <option value="price-high-low">價格 (高到低)</option>
      </select>

      <label for="favorites" class="form-label">我的最愛:</label>
      <select v-model="filteredItems" @change="updateFavorites" class="form-select">
        <option value="all">無</option>
        <option value="favorites">我的最愛</option>
      </select>
    </div>
  </main>
</template>

<script>
  import { closet_filterSortMixin } from "../mixins/closet_filterSortMixin.js";

  export default {
    mixins: [closet_filterSortMixin],
    mounted() {
      this.applyFiltersAndSorting(); // 頁面載入後執行一次篩選
    },
  };
</script>

<style scoped>
  .filter-sort {
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 20px;
  }

  .filter-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #3d3d3d;
  }

  .form-label {
    font-size: 16px;
    margin-bottom: 5px;
    color: #3d3d3d;
  }

  .form-select {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 10px;
    border: 1px solid #ccc;
    background-color: #ffffff;
    font-size: 14px;
  }

  .form-select:focus {
    outline: none;
    border-color: #b5a191;
    box-shadow: 0 0 5px rgba(181, 161, 145, 0.5);
  }

  .filter-sort select {
    margin-right: 10px;
    padding: 5px;
  }
</style>
