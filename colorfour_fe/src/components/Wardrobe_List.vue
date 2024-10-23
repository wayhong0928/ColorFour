<template>
  <div class="row" id="wardrobe-list">
    <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4" v-for="item in items" :key="item.id">
      <div class="card mb-3">
        <img :src="item.photo_url" class="card-img-top" :alt="item.item_name" />
        <div class="card-body">
          <h5 class="card-title">
            <router-link :to="{ name: 'closet_detail', params: { id: item.id } }">{{ item.item_name }}</router-link>
          </h5>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" :value="item.id" @change="onItemSelected($event)" />
            <label class="form-check-label"></label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      items: Array,
      selectedItems: Array,
    },
    data() {
      return {
        localSelectedItems: [...this.selectedItems],
      };
    },
    methods: {
      onItemSelected(event) {
        const itemId = parseInt(event.target.value);
        let updatedSelectedItems = [...this.selectedItems];

        if (event.target.checked) {
          if (!updatedSelectedItems.includes(itemId)) {
            updatedSelectedItems.push(itemId);
          }
        } else {
          updatedSelectedItems = updatedSelectedItems.filter((id) => id !== itemId);
        }

        console.log("更新 selectedItems:", updatedSelectedItems);
        this.$emit("update:selectedItems", updatedSelectedItems);
      },
    },
    watch: {
      selectedItems(newItems) {
        this.localSelectedItems = [...newItems];
      },
    },
  };
</script>

<style scoped>
  .row {
    display: flex;
    flex-wrap: wrap;
    margin: 0 -0.5rem;
  }

  .col-12,
  .col-sm-6,
  .col-md-4,
  .col-lg-3 {
    padding: 0 0.5rem;
    margin-bottom: 1.5em;
  }

  .card {
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .card-img-top {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  .card-title {
    font-size: 1.25em;
    margin-bottom: 0.5em;
    text-align: center;
  }

  .card-title a {
    color: black; 
    text-decoration: none; /* 移除底線 */
  }

  .card-title a:hover {
    color: black; 
    text-decoration: none; /* 保持無底線 */
  }

  .form-check {
    position: absolute;
    top: 10px;
    right: 10px;
  }
</style>
