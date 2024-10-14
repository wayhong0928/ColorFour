export const closet_filterSortMixin = {
  data() {
    return {
      selectedCategory: "all",
      selectedBrand: "all",
      sortBy: "newest",
      brands: [],
      items: [], // Include items to make it self-contained
    };
  },
  computed: {
    sortedAndFilteredItems() {
      if (!this.items || this.items.length === 0) {
        console.log("No items available to sort or filter");
        return [];
      }

      let filtered = this.items;

      // Filtering by category
      if (this.selectedCategory !== "all") {
        filtered = filtered.filter((item) => item.category === this.selectedCategory);
      }

      // Filtering by brand
      if (this.selectedBrand !== "all") {
        filtered = filtered.filter((item) => item.brand === this.selectedBrand);
      }

      // Sorting
      return filtered.sort((a, b) => {
        if (this.sortBy === "newest") {
          return new Date(b.add_date) - new Date(a.add_date);
        } else if (this.sortBy === "oldest") {
          return new Date(a.add_date) - new Date(b.add_date);
        } else if (this.sortBy === "price-low-high") {
          return a.price - b.price;
        } else if (this.sortBy === "price-high-low") {
          return b.price - a.price;
        } else if (this.sortBy === "brand") {
          return a.brand.localeCompare(b.brand);
        }
      });
    },
  },
  methods: {
    extractBrands() {
      if (!this.items || this.items.length === 0) {
        console.log("No items available to extract brands");
        return;
      }
      const uniqueBrands = new Set(this.items.map((item) => item.brand));
      this.brands = Array.from(uniqueBrands);
    },
  },
};
