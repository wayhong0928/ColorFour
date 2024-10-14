<template>
  <div class="filter-sort">
    <label for="category">分類:</label>
    <select v-model="localSelectedCategory" @change="updateCategory">
      <option value="all">全部</option>
      <option value="clothing">服飾</option>
      <option value="shoes">鞋子</option>
    </select>

    <label for="brand">品牌:</label>
    <select v-model="localSelectedBrand" @change="updateBrand">
      <option value="all">全部</option>
      <option v-for="brand in brands" :key="brand" :value="brand">{{ brand }}</option>
    </select>

    <label for="sort-by">排序方式:</label>
    <select v-model="localSortBy" @change="updateSortBy">
      <option value="newest">新增時間 (先到後)</option>
      <option value="oldest">新增時間 (後到先)</option>
      <option value="brand">品牌名稱</option>
      <option value="price-low-high">價格 (低到高)</option>
      <option value="price-high-low">價格 (高到低)</option>
    </select>
  </div>
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
  }

  .filter-sort select {
    margin-right: 10px;
    padding: 5px;
  }
</style>
