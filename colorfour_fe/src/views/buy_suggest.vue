<template>
  <div>
    <h1>上傳照片，進行建議</h1>

    <!-- 上傳照片區域 -->
    <div class="upload-section">
      <label for="file-upload" class="custom-file-upload">
        上傳照片
      </label>
      <input type="file" id="file-upload" accept="image/*" @change="handleFileUpload" />
    </div>

    <!-- 顯示上傳的照片 -->
    <div v-if="imageUrl" class="image-preview">
      <h3>預覽</h3>
      <img :src="imageUrl" alt="Uploaded Image" />
    </div>

    <!-- 提交按鈕 -->
    <div class="submit-section">
      <button @click="submitPhoto" :disabled="!image">送出</button>
      <button class="back-button" @click="goBack">返回</button>
    </div>
  </div>
</template>

<script>
export default {
    name:"buy_suggest",
  data() {
    return {
      image: null, // 用於存儲選擇的圖片文件
      imageUrl: null // 用於預覽上傳的圖片
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.image = file;
        this.imageUrl = URL.createObjectURL(file);
      }
    },
    submitPhoto() {
      if (!this.image) {
        alert("請先上傳圖片");
        return;
      }

      // 模擬圖片上傳及處理
      const formData = new FormData();
      formData.append('image', this.image);

      // 這裡應該使用 API 調用上傳圖片，然後獲得建議結果
      // 模擬上傳和結果生成，完成後跳轉至結果頁面

      this.$router.push('/buy_result');
    },
    goBack() {
      this.$router.go(-1);
    }
  }
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin: 20px 0;
}

.upload-section {
  text-align: center;
  margin: 40px 0;
}

.custom-file-upload {
  display: inline-block;
  padding: 10px 20px;
  cursor: pointer;
  background-color: #d4b7a1;
  color: white;
  border-radius: 5px;
}

#file-upload {
  display: none;
}

.image-preview {
  text-align: center;
  margin: 20px 0;
}

.image-preview img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
  padding: 5px;
  border-radius: 5px;
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

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

</style>

