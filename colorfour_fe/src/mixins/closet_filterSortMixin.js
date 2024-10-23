export const closet_filterSortMixin = {
  data() {
    return {
      selectedCategory: "all",
      selectedBrand: "all",
      sortBy: "newest",
      brands: [],
      items: [], // 存放所有的 Item
      filteredItems: [], // 存放篩選後的結果
    };
  },
  watch: {
    // 當 items 資料變動時，自動執行篩選與排序
    items() {
      this.applyFiltersAndSorting();
      this.extractBrands(); // 更新品牌列表
    },
  },
  computed: {
    sortedAndFilteredItems() {
      return this.filteredItems;
    },
  },
  methods: {
    applyFiltersAndSorting() {
      let filtered = [...this.items]; // 複製 items 進行篩選

      // 依照類別篩選
      if (this.selectedCategory !== "all") {
        filtered = filtered.filter((item) => item.main_category === parseInt(this.selectedCategory));
      }

      // 依照品牌篩選
      if (this.selectedBrand !== "all") {
        filtered = filtered.filter((item) => item.brand === parseInt(this.selectedBrand));
      }

      // 排序
      filtered.sort((a, b) => {
        if (this.sortBy === "newest") {
          return new Date(b.add_date) - new Date(a.add_date);
        } else if (this.sortBy === "oldest") {
          return new Date(a.add_date) - new Date(b.add_date);
        } else if (this.sortBy === "price-low-high") {
          return a.price - b.price;
        } else if (this.sortBy === "price-high-low") {
          return b.price - a.price;
        }
      });

      this.filteredItems = filtered;
    },
    extractBrands() {
      const uniqueBrands = new Set(this.items.map((item) => item.brand));
      this.brands = Array.from(uniqueBrands);
    },
  },
};
