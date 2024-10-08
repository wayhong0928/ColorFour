<template>
  <div>
    <header id="header"></header>
    <div class="container mt-5">
      <h1>新增單品</h1>
      <form @submit.prevent="handleSubmit">
        <div class="mb-3">
          <label for="itemName" class="form-label">商品名稱</label>
          <input type="text" class="form-control" v-model="item.name" id="itemName" placeholder="輸入商品名稱" required />
        </div>
        <div class="mb-3">
          <label for="itemBrand" class="form-label">品牌</label>
          <input type="text" class="form-control" v-model="item.brand" id="itemBrand" placeholder="輸入品牌名稱" required />
        </div>
        <div class="mb-3">
          <label for="itemPrice" class="form-label">價格</label>
          <input type="number" class="form-control" v-model="item.price" id="itemPrice" placeholder="輸入價格" required />
        </div>
        <div class="mb-3">
          <label for="itemCategory" class="form-label">種類</label>
          <select id="itemCategory" class="form-select" v-model="item.category" required>
            <option value="top">上衣</option>
            <option value="bottom">下身</option>
            <option value="coat">外套</option>
            <option value="shoes">鞋子</option>
            <option value="accessories">配件</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="itemTags" class="form-label">標籤</label>
          <input type="text" class="form-control" v-model="item.tags" id="itemTags" placeholder="輸入標籤，以逗號分隔" required />
        </div>
        <div class="mb-3">
          <label for="itemImage" class="form-label">上傳圖片</label>
          <input type="file" class="form-control" id="itemImage" accept="image/*" @change="handleImageUpload" required />
          <button type="button" class="btn btn-outline-primary mt-2" @click="openCamera">開啟相機</button>
        </div>
        <div class="submit-section">
        <button type="submit" class="btn btn-primary">新增單品</button>
        <button class="back-button" @click="goBack">返回</button>
        </div>
      </form>
    </div>

    <div class="zone"></div>
    <footer id="footer"></footer>
  </div>
</template>

<script>
  export default {
    name: "closet_new",
    data() {
      return {
        item: {
          name: "",
          brand: "",
          price: "",
          category: "top",
          tags: "",
          image: null,
        },
      };
    },
    methods: {
      handleSubmit() {
        const item = {
          ...this.item,
          tags: this.item.tags.split(",").map((tag) => tag.trim()),
          addedDate: new Date().toLocaleDateString(),
        };

        console.log(item);
        alert("商品已新增！");
        this.$router.push({ path: "/closet_index" }); // 使用 Vue Router 進行頁面跳轉
      },
      handleImageUpload(event) {
        this.item.image = event.target.files[0];
      },
      openCamera() {
        const cameraInput = document.createElement("input");
        cameraInput.type = "file";
        cameraInput.accept = "image/*";
        cameraInput.capture = "camera";
        cameraInput.click();

        cameraInput.onchange = (event) => {
          const file = event.target.files[0];
          if (file) {
            this.item.image = file;
            alert("照片已拍攝並選擇");
          }
        };
      },
      goBack() {
      this.$router.go(-1);
    },
    },
  };
</script>

<style scoped>
  h1 {
    margin-bottom: 30px;
  }

  .submit-section {
  text-align: center;
  margin: 20px 0;
}

.submit-section button {
  padding: 10px 20px;
  background-color: #d4b7a1;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  margin: 0 10px; /* 增加按鈕間距 */
}

</style>
