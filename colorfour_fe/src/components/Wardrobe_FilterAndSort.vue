<template>
<main>
  <div class="filter-sort">
    <h2 class="filter-title">篩選</h2>
    <label for="category" class="form-label">分類:</label>
    <select v-model="localSelectedCategory" @change="updateCategory" class="form-select">
      <option value="all">全部</option>
      <option value="clothing">服飾</option>
      <option value="shoes">鞋子</option>
    </select>

    <label for="brand" class="form-label">品牌:</label>
    <select v-model="localSelectedBrand" @change="updateBrand" class="form-select">
      <option value="all">全部</option>
      <option v-for="brand in brands" :key="brand" :value="brand">{{ brand }}</option>
    </select>

    <label for="sort-by" class="form-label">排序方式:</label>
    <select v-model="localSortBy" @change="updateSortBy" class="form-select">
      <option value="newest">新增時間 (先到後)</option>
      <option value="oldest">新增時間 (後到先)</option>
      <option value="brand">品牌名稱</option>
      <option value="price-low-high">價格 (低到高)</option>
      <option value="price-high-low">價格 (高到低)</option>
    </select>
  </div>
  </main>
</template>

<script>
  export default {
    props: {
      brands: Array,
      selectedCategory: String,
      selectedBrand: String,
      sortBy: String,
    },
    data() {
      return {
        localSelectedCategory: this.selectedCategory || "all",
        localSelectedBrand: this.selectedBrand || "all",
        localSortBy: this.sortBy || "newest",
      };
    },
    methods: {
      updateCategory() {
        this.$emit("update:selectedCategory", this.localSelectedCategory);
      },
      updateBrand() {
        this.$emit("update:selectedBrand", this.localSelectedBrand);
      },
      updateSortBy() {
        this.$emit("update:sortBy", this.localSortBy);
      },
    },
    watch: {
      selectedCategory(newVal) {
        this.localSelectedCategory = newVal;
      },
      selectedBrand(newVal) {
        this.localSelectedBrand = newVal;
      },
      sortBy(newVal) {
        this.localSortBy = newVal;
      },
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
