<template>
  <div>
    <main>
      <section class="container my-5">
        <h2 class="mb-4">新增色彩分析</h2>

        <!-- 分析名稱選擇區 -->
        <div class="mb-4">
          <label for="analysis-name" class="form-label">已選擇分析名稱</label>
          <input
            type="text"
            id="analysis-name"
            :value="selectedNames.join(', ')"
            class="form-control"
            placeholder="請選擇名稱（如：素顏、全妝等）"
            readonly
            required
          />
        </div>

        <!-- 名稱選擇按鈕區 -->
        <div class="button-group mb-4">
          <button
            v-for="name in nameOptions"
            :key="name"
            @click="toggleSelection(name)"
            :class="{'btn-primary': selectedNames.includes(name), 'btn-outline-secondary': !selectedNames.includes(name)}"
            class="btn mx-1"
          >
            {{ name }}
          </button>
          <button 
            @click="enableCustomName" 
            class="btn btn-outline-secondary mx-1"
          >
            自訂名稱
          </button>
        </div>

        <!-- 自訂名稱區域 -->
        <div v-if="customName" class="mb-4">
          <label for="custom-name" class="form-label">自訂名稱</label>
          <input
            type="text"
            id="custom-name"
            v-model="customInput"
            class="form-control"
            placeholder="輸入自訂名稱"
          />
          <button class="btn btn-outline-secondary mt-2" @click="addCustomName">新增自訂名稱</button>
        </div>

        <!-- 上傳照片區 -->
        <div class="mb-4">
          <label class="form-label">上傳照片</label>
          <input
            type="file"
            accept="image/*"
            @change="handleFileUpload"
            class="form-control"
            required
          />
          <div v-if="imagePreview" class="image-preview mt-3">
            <img :src="imagePreview" alt="預覽圖片" class="img-fluid rounded" />
          </div>
        </div>

        <!-- 按鈕區 -->
        <div class="d-flex justify-content-between">
          <router-link to="/color_index">
            <button class="btn btn-outline-secondary">取消測驗</button>
          </router-link>
          <button class="btn btn-primary" @click="startTest" :disabled="loading">
            前往測驗
          </button>
        </div>
      </section>

      <!-- Loading Spinner -->
      <div v-if="loading" class="loading-overlay">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedNames: [],
      imagePreview: null,
      customName: false,
      customInput: "",
      nameOptions: [
        "素顏",
        "全妝",
        "簡單淡妝",
        "派對妝",
        "日常妝",
        "晚宴妝",
        "戶外妝",
        "正式場合妝",
        "專業妝",
      ],
      loading: false, // 控制 loading 狀態
    };
  },
  methods: {
    toggleSelection(name) {
      const index = this.selectedNames.indexOf(name);
      if (index === -1) {
        this.selectedNames.push(name);
      } else {
        this.selectedNames.splice(index, 1);
      }
    },
    enableCustomName() {
      this.customName = true;
    },
    addCustomName() {
      if (this.customInput) {
        this.selectedNames.push(this.customInput);
        this.customInput = "";
        this.customName = false;
      }
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imagePreview = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    startTest() {
      if (this.selectedNames.length > 0 && this.imagePreview) {
        this.loading = true; // 開始 loading
        setTimeout(() => {
          this.$router.push("/color_result"); // 模擬跳轉
        }, 2000); // 模擬2秒延遲
      } else {
        alert("請填寫所有欄位");
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

.button-group {
  display: flex;
  flex-wrap: wrap;
}

.button-group .btn {
  margin-bottom: 5px;
}

.btn-primary {
  background-color: #007bff;
  color: white;
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
