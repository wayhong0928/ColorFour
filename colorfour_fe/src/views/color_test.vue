<template>
  <div class="container">
    <header>
      <nav>
        <router-link to="/color_index" class="close-btn" id="close-questionnaire">x</router-link>
      </nav>
    </header>

    <!-- 圖片上傳區 -->
    <div class="image-upload-container">
      <input type="file" @change="onImageUpload" accept="image/*" />
    </div>

    <!-- 四季圖片與上傳圖片 -->
    <div v-if="uploadedImage" class="seasons">
      <div v-for="(season, index) in seasons" :key="season.name" class="season col-6">
        <div class="card" :class="{ selected: selectedSeason === season.name }">
          <img :src="season.image" class="card-img-top season-image" :alt="season.name" />
          <div class="uploaded-image-container">
            <img :src="uploadedImage" alt="Uploaded Image" class="uploaded-image" />
          </div>
          <div class="card-body text-center">
            <button class="btn btn-primary" @click="selectSeason(season.name)">選擇</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 題目表單 -->
    <main v-if="selectedSeason !== null">
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label for="analysis-name" class="form-label">請選擇分析名稱</label>
          <select id="analysis-name" v-model="selectedName" class="form-select" required>
            <option v-for="name in nameOptions" :key="name" :value="name">{{ name }}</option>
          </select>
        </div>
        <div v-for="(question, index) in questions" :key="index" class="question-container">
          <h2 class="question-title">{{ question.title }}</h2>
          <div class="options">
            <label v-for="option in question.options" :key="option.value" class="option-label">
              <input
                type="radio"
                :name="'q' + index"
                :value="option.value"
                v-model="answers[index].selected_option"
                class="option-input"
              />
              {{ option.text }}
            </label>
          </div>
        </div>
        <button type="submit" id="submit-button">提交</button>
      </form>
    </main>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        uploadedImage: null,
        uploadedImageFile: null,
        selectedSeason: null,
        selectedName: "",
        nameOptions: ["素顏", "全妝", "簡單淡妝", "派對妝", "日常妝", "晚宴妝", "戶外妝", "正式場合妝", "專業妝"],
        answers: [
          { question_index: 1, selected_option: null },
          { question_index: 2, selected_option: null },
          { question_index: 3, selected_option: null },
          { question_index: 4, selected_option: null },
        ],
        submitting: false,
        seasons: [
          { name: "Spring", image: require("@/assets/img/color_season_1.jpeg") },
          { name: "Summer", image: require("@/assets/img/color_season_2.jpeg") },
          { name: "Autumn", image: require("@/assets/img/color_season_3.jpeg") },
          { name: "Winter", image: require("@/assets/img/color_season_4.jpeg") },
        ],
        questions: [
          {
            title: "嘴唇較無血色",
            options: [
              { text: "是", value: "yes" },
              { text: "否", value: "no" },
            ],
          },
          {
            title: "比起黑髮更適合棕色或是淺髮",
            options: [
              { text: "是", value: "yes" },
              { text: "否", value: "no" },
            ],
          },
          {
            title: "臉部有紅潤感",
            options: [
              { text: "是", value: "yes" },
              { text: "否", value: "no" },
            ],
          },
          {
            title: "眼珠偏淺棕色，眼神柔和",
            options: [
              { text: "是", value: "yes" },
              { text: "否", value: "no" },
            ],
          },
        ],
      };
    },
    methods: {
      onImageUpload(event) {
        const file = event.target.files[0];
        if (file) {
          this.uploadedImageFile = file;
          this.uploadedImage = URL.createObjectURL(file);
        }
      },
      selectSeason(seasonName) {
        this.selectedSeason = seasonName;
      },
      async handleSubmit() {
        if (!this.selectedSeason || !this.uploadedImageFile || !this.selectedName) {
          alert("請填寫所有欄位！");
          return;
        }

        const formData = new FormData();
        formData.append("test_name", this.selectedName);
        formData.append("result_type", this.selectedSeason);
        formData.append("uploaded_image", this.uploadedImageFile);

        try {
          const backendUrl = `${process.env.VUE_APP_BACKEND_URL}/color/user-tests/`;
          const response = await axios.post(backendUrl, formData, {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });

          const testId = response.data.id; // 確保後端返回 ID
          alert("測驗成功提交！");
          this.$router.push({ name: "color_result", params: { id: testId } });
        } catch (error) {
          console.error("提交失敗:", error.response);
          alert(error.response?.data?.message || "提交失敗，請重試！");
        }
      },
    },
  };
</script>

<style scoped>
  /* 容器樣式 */
  .container {
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    padding: 1.5rem;
    background-color: #f9f9f9;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    overflow: hidden;
  }

  /* Header 樣式 */
  header {
    display: flex;
    justify-content: flex-end;
    padding-bottom: 1rem;
    width: 100%;
  }

  .close-btn {
    font-size: 1.5rem;
    text-decoration: none;
    color: #333;
    font-weight: bold;
  }

  /* 圖片上傳區 */
  .image-upload-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
    width: 100%;
  }

  .image-upload-container input[type="file"] {
    max-width: 300px;
    width: 95%;
    box-sizing: border-box;
  }

  .image-upload-container button,
  .image-upload-container input[type="file"] {
    background-color: #f1f1f1;
    color: #333;
    border: 1px solid #ccc;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
  }

  .image-upload-container button:hover,
  .image-upload-container input[type="file"]:hover {
    background-color: #7b838a;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }

  /* 四季圖片區 */
  .seasons {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 15px;
    margin-top: 20px;
    width: 100%;
  }

  .season {
    position: relative;
    width: 45%;
  }

  /* 卡片樣式 */
  .card {
    border: 1px solid #ccc;
    border-radius: 15px;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.3s ease;
    height: 100%; /* 卡片占滿父容器高度 */
  }

  .card.selected {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  }

  /* 圖片樣式 */
  .season-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  /* 上傳圖片容器 */
  .uploaded-image-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 70%;
    height: 70%;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  }

  /* 上傳圖片 */
  .uploaded-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
  }

  /* 卡片內容 */
  .card-body {
    padding: 10px;
    text-align: center;
  }

  /* 按鈕樣式 */
  .btn-primary {
    background-color: #007bff;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    border-radius: 5px;
    transition: background-color 0.3s ease;
  }

  .btn-primary:hover {
    background-color: #0056b3;
  }

  /* 題目表單 */
  .question-container {
    margin-bottom: 1.5rem;
  }

  .question-title {
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
    color: #444;
    text-align: left;
  }

  .options {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .option-label {
    display: flex;
    align-items: center;
    background-color: #e9ecef;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
  }

  .option-label:hover {
    background-color: #dee2e6;
    transform: translateY(-2px);
  }

  .option-input {
    margin-right: 0.75rem;
  }

  /* 提交按鈕 */
  #submit-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    font-size: 1.25rem;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    display: block;
    margin: 1rem auto;
  }

  #submit-button:hover {
    background-color: #0056b3;
    transform: translateY(-2px);
  }

  /* 響應式調整 */
  @media (max-width: 320px) {
    .seasons {
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    .season {
      width: 90%;
    }

    .image-upload-container input[type="file"] {
      max-width: 90%;
    }
  }
</style>
