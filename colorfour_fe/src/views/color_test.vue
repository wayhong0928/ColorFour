<template>
  <div class="container">
    <header>
      <nav>
        <router-link to="/color_index" class="close-btn" id="close-questionnaire">x</router-link>
      </nav>
    </header>

    <!-- 圖片上傳區 -->
    <div class="image-upload-container">
      <button @click="openCamera">開啟相機</button>
      <input type="file" @change="onImageUpload" accept="image/*" />
    </div>

    <!-- 四季圖片與上傳圖片 -->
    <div v-if="uploadedImage" class="seasons">
      <div v-for="season in seasons" :key="season.name" class="season">
        <img :src="season.image" alt="season image" class="season-image" />
        <div class="uploaded-image-container">
          <img :src="uploadedImage" alt="Uploaded Image" class="uploaded-image" />
        </div>
      </div>
    </div>

    <!-- 題目表單 -->
    <main v-if="uploadedImage">
      <form @submit.prevent="handleSubmit">
        <div v-for="(question, index) in questions" :key="index" class="question-container">
          <h2 class="question-title">{{ question.title }}</h2>
          <div class="options">
            <label v-for="option in question.options" :key="option.value" class="option-label">
              <input 
                type="radio" 
                :name="'q' + index" 
                :value="option.value" 
                v-model="answers[index]" 
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
export default {
  data() {
    return {
      uploadedImage: null,
      uploadedImageFile: null,
      answers: Array(4).fill(null),
      seasons: [
        { name: '春', image: require('@/assets/img/color_season_1.jpeg') },
        { name: '夏', image: require('@/assets/img/color_season_2.jpeg') },
        { name: '秋', image: require('@/assets/img/color_season_3.jpeg') },
        { name: '冬', image: require('@/assets/img/color_season_4.jpeg') },
      ],
      questions: [
        { title: '嘴唇較無血色', options: [{ text: '是', value: 'yes' }, { text: '否', value: 'no' }] },
        { title: '比起黑髮更適合棕色或是淺髮', options: [{ text: '是', value: 'yes' }, { text: '否', value: 'no' }] },
        { title: '臉部有紅潤感', options: [{ text: '是', value: 'yes' }, { text: '否', value: 'no' }] },
        { title: '眼珠偏淺棕色，眼神柔和', options: [{ text: '是', value: 'yes' }, { text: '否', value: 'no' }] },
      ],
      scores: { A: 0, B: 0, C: 0, D: 0 },
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
    openCamera() {
      const fileInput = document.createElement('input');
      fileInput.type = 'file';
      fileInput.accept = 'image/*';
      fileInput.capture = 'user';
      fileInput.onchange = this.onImageUpload;
      fileInput.click();
    },
    handleSubmit() {
      this.calculateScores();
      const result = this.getSeasonResult();
      alert(`您的季節分析結果是：${result}`);
    },
    calculateScores() {
      this.answers.forEach((answer, index) => {
        if (index === 0 || index === 2) {
          if (answer === 'yes') this.scores.C++, this.scores.D++;
          else this.scores.A++, this.scores.B++;
        } else if (index === 1) {
          if (answer === 'yes') this.scores.A++, this.scores.B++;
          else this.scores.C++, this.scores.D++;
        } else if (index === 3) {
          if (answer === 'yes') this.scores.A++, this.scores.C++;
          else this.scores.B++, this.scores.D++;
        }
      });
    },
    getSeasonResult() {
      const maxScore = Math.max(...Object.values(this.scores));
      const seasonMap = { A: '春', B: '夏', C: '秋', D: '冬' };
      const season = Object.keys(this.scores).find(key => this.scores[key] === maxScore);
      return seasonMap[season];
    },
  },
};
</script>

<style scoped>
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

.image-upload-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-bottom: 2rem;
  gap: 1rem;
  width: 100%;
  box-sizing: border-box;
}

.image-upload-container input[type="file"] {
  max-width: 300px; /* 限制選擇檔案按鈕的最大寬度 */
  width: 95%; /* 保持自適應 */
  box-sizing: border-box; /* 包含內邊距和邊框 */
}

/* 上傳按鈕的樣式 */
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
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 兩欄的排版 */
  gap: 1rem;
  margin-top: 1rem;
  width: 100%;
}

/* 圖片容器 */
.season {
  position: relative;
  width: 100%; /* 讓圖片撐滿容器寬度 */
  max-width: 300px; /* 避免圖片過大 */
  margin: 0 auto;
  aspect-ratio: 2 / 3; /* 維持 2:3 的比例 */
  overflow: hidden;
}

/* 四季圖片樣式 */
.season-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 40% / 50%; /* 直向橢圓 */
}

/* 上傳圖片容器 */
.uploaded-image-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 70%;
  height: 70%;
  overflow: hidden;
  border-radius: 40% / 50%; 
}

.uploaded-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  color: #fff;
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
    width: 90%; /* 撐滿小螢幕寬度 */
  }

  .image-upload-container input[type="file"] {
    max-width: 90%; /* 確保按鈕在小螢幕上不會超出容器 */
  }
}

</style>
