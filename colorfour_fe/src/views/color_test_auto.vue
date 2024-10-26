<template>
  <div class="container">
    <section class="form-container my-5">
      <h2 class="mb-4">自動化色彩測驗</h2>

      <!-- 名稱選擇區（單選） -->
      <div class="mb-4">
        <label for="selected-name" class="form-label">請選擇分析氣色(妝容)</label>
        <select id="selected-name" v-model="selectedName" class="form-select" required>
          <option v-for="name in nameOptions" :key="name" :value="name">{{ name }}</option>
        </select>
      </div>

      <!-- 圖片上傳區 -->
      <div class="mb-4">
        <label class="form-label">上傳圖片</label>
        <input type="file" accept="image/*" @change="handleFileUpload" class="form-control" />
        <div v-if="imagePreview" class="image-preview mt-3">
          <img :src="imagePreview" alt="圖片預覽" class="img-fluid rounded" />
        </div>
      </div>

      <!-- 繳交按鈕 -->
      <div class="d-flex justify-content-between">
        <router-link to="/color_index">
          <button class="btn btn-outline-secondary">取消</button>
        </router-link>
        <button @click="startTest" class="btn btn-primary" :disabled="loading">提交測驗</button>
      </div>
    </section>

    <!-- Loading Spinner -->
    <div v-if="loading" class="loading-overlay">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        selectedName: "",
        imagePreview: null,
        uploadedImageFile: null,
        nameOptions: ["素顏", "全妝", "簡單淡妝", "派對妝", "日常妝", "晚宴妝", "戶外妝", "正式場合妝", "專業妝"],
        loading: false,
      };
    },
    methods: {
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
          this.uploadedImageFile = file;
          const reader = new FileReader();
          reader.onload = (e) => {
            this.imagePreview = e.target.result;
          };
          reader.readAsDataURL(file);
        }
      },
      async startTest() {
        if (!this.selectedName || !this.uploadedImageFile) {
          alert("請填寫所有欄位");
          return;
        }

        this.loading = true;

        const formData = new FormData();
        formData.append("test_name", this.selectedName);
        formData.append("result_type", "Spring"); // 預設結果為 Spring
        formData.append("uploaded_image", this.uploadedImageFile);

        try {
          const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}/color/user-tests/`, formData, {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });

          const testId = response.data.id;
          alert("測驗成功提交！");
          this.$router.push({ name: "color_result", params: { id: testId } });
        } catch (error) {
          console.error("提交失敗:", error.response);
          alert(error.response?.data?.message || "提交失敗，請重試！");
        } finally {
          this.loading = false;
        }
      },
    },
  };
</script>

<style scoped>
  .image-preview {
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    background-color: #f9f9f9;
  }

  .image-preview img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
  }

  .loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1050;
  }
</style>
