<!-- 原來的template 
<template>
  <div class="container">
    <header>
      <nav>
        <router-link to="/color_index" class="close-btn" id="close-questionnaire">x</router-link>
      </nav>
    </header>
    <img src="@/assets/img/face.png" alt="Header Image" class="header-image" />
    <main>
      <form @submit.prevent="handleSubmit">
        <div class="question-container">
          <div
            :class="['question', { active: currentQuestionIndex === index }]"
            v-for="(question, index) in questions"
            :key="question.title"
          >
            <h2 class="question-title">{{ question.title }}</h2>
            <div class="options" v-if="question.options">
              <label v-for="(option, idx) in question.options" :key="option.value" class="option-label">
                <input type="radio" :name="`q${index + 1}`" :value="option.value" v-model="answers[index]" class="option-input" />
                <span v-if="option.color" class="color-block" :style="{ backgroundColor: option.color }"></span>
                {{ option.text }}
              </label>
            </div>
            <div v-else>
              <label v-for="(option, idx) in question.colors" :key="option.value" class="option-label">
                <input type="radio" :name="`q${index + 1}`" :value="option.value" v-model="answers[index]" class="option-input" />
                <div class="color-blocks">
                  <span
                    v-for="color in option.colors"
                    :key="color"
                    class="color-block"
                    :style="{ backgroundColor: color }"
                  ></span>
                </div>
              </label>
            </div>
            <p v-if="error && !answers[index]" class="error-text">此問題為必填</p>
          </div>
        </div>

        <div class="button-container">
          <button v-if="currentQuestionIndex > 0" @click="prevQuestion" id="prev-button" type="button">上一題</button>
          <button
            v-if="currentQuestionIndex < questions.length - 1"
            @click="nextQuestion"
            id="next-button"
            type="button"
            :disabled="!answers[currentQuestionIndex]"
          >
            下一題
          </button>
          <button v-if="currentQuestionIndex === questions.length - 1" type="submit" id="submit-button">提交</button>
        </div>
      </form>
    </main>
  </div>
</template>
-->
<!-- 修改後的template  -->
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
      <img v-if="uploadedImage" :src="uploadedImage" alt="Uploaded Image" class="header-image" />
    </div>

    <!-- 顯示測驗表單 -->
    <main v-if="uploadedImage">
      <form @submit.prevent="handleSubmit">
        <div class="question-container">
          <div
            :class="['question', { active: currentQuestionIndex === index }]"
            v-for="(question, index) in questions"
            :key="question.title"
          >
            <h2 class="question-title">{{ question.title }}</h2>

            <!-- 文字選項 -->
            <div class="options" v-if="question.options">
              <label v-for="(option, idx) in question.options" :key="option.value" class="option-label">
                <input 
                  type="radio" 
                  :name="`q${index + 1}`" 
                  :value="option.value" 
                  v-model="answers[index]" 
                  class="option-input" 
                />
                <span 
                  v-if="option.color" 
                  class="color-block" 
                  :style="{ backgroundColor: option.color }"
                ></span>
                {{ option.text }}
              </label>
            </div>

            <!-- 顏色塊選項 -->
            <div class="color-options" v-else-if="question.colors">
              <label 
                v-for="(colorOption, idx) in question.colors" 
                :key="colorOption.value" 
                class="option-label"
              >
                <input 
                  type="radio" 
                  :name="`q${index + 1}`" 
                  :value="colorOption.value" 
                  v-model="answers[index]" 
                  class="option-input" 
                />
                <div class="color-blocks">
                  <span
                    v-for="color in colorOption.colors"
                    :key="color"
                    class="color-block"
                    :style="{ backgroundColor: color }"
                  ></span>
                </div>
              </label>
            </div>

            <p v-if="error && !answers[index]" class="error-text">此問題為必填</p>
          </div>
        </div>

        <!-- 上一題/下一題/提交按鈕 -->
        <div class="button-container">
          <button 
            v-if="currentQuestionIndex > 0" 
            @click="prevQuestion" 
            id="prev-button" 
            type="button"
          >
            上一題
          </button>
          <button
            v-if="currentQuestionIndex < questions.length - 1"
            @click="nextQuestion"
            id="next-button"
            type="button"
            :disabled="!answers[currentQuestionIndex]"
          >
            下一題
          </button>
          <button 
            v-if="currentQuestionIndex === questions.length - 1" 
            type="submit" 
            id="submit-button"
          >
            提交
          </button>
        </div>
      </form>
    </main>
  </div>
</template>


<!-- 原來的script
<script>
  export default {
    name: "ColorTest",
    data() {
      return {
        currentQuestionIndex: 0,
        questions: [
          {
            title: "問題 1 - 肌膚",
            options: [
              { text: "容易曬紅或是曬傷", value: "A", color: "" },
              { text: "容易曬黑，曬後立刻暗沈", value: "B", color: "" },
              { text: "先曬紅後轉黑", value: "C", color: "" },
            ],
          },
          {
            title: "問題 2 - 瞳色",
            options: [
              { text: "茶棕色", value: "brown", color: "#654321" },
              { text: "古銅色", value: "brown2", color: "#8B4513" },
              { text: "焦棕色", value: "brown3", color: "#5C4033" },
              { text: "黑棕色", value: "brown4", color: "#3D2B1F" },
            ],
          },
          {
            title: "問題 3 - 髮色",
            options: [
              { text: "淺茶色", value: "tea", color: "#D2B48C" },
              { text: "灰黑色", value: "gray", color: "#708090" },
              { text: "黑茶色", value: "btea", color: "#3B2F2F" },
              { text: "黑色", value: "black", color: "#000000" },
            ],
          },
          {
            title: "問題 4 - 彩度（哪種顏色在您身上看起來最亮？）",
            colors: [
              { value: "A", colors: ["#fef8ca", "#cce6cf", "#efdbd9", "#cae4ec"] },
              { value: "B", colors: ["#fdef87", "#a2d193", "#e7a6a1", "#8fccdf"] },
              { value: "C", colors: ["#f4ea62", "#7fba4a", "#e16565", "#45b0e1"] },
              { value: "D", colors: ["#fdec4d", "#26aa39", "#e72828", "#282aff"] },
              { value: "E", colors: ["#fce610", "#10681d", "#dc0000", "#0000ea"] },
            ],
          },
          {
            title: "問題 5 - 選擇一個適合自己的顏色，讓氣色更好，更白",
            options: [
              { text: "", value: "purple", color: "#800080" },
              { text: "", value: "purple2", color: "#9370DB" },
              { text: "", value: "purple3", color: "#DDA0DD" },
              { text: "", value: "purple4", color: "#EE82EE" },
            ],
          },
          {
            title: "問題 6 - 選擇一個適合自己的顏色，讓氣色更好，更白",
            options: [
              { text: "", value: "yellow", color: "#FFFF00" },
              { text: "", value: "yellow2", color: "#FFD700" },
              { text: "", value: "yellow3", color: "#FFA500" },
              { text: "", value: "yellow4", color: "#FF8C00" },
            ],
          },
          {
            title: "問題 7 - 選擇一個適合自己的顏色，讓氣色更好，更白",
            options: [
              { text: "", value: "orange", color: "#FFA07A" },
              { text: "", value: "orange2", color: "#FF7F50" },
              { text: "", value: "orange3", color: "#FF6347" },
              { text: "", value: "orange4", color: "#FF4500" },
            ],
          },
          {
            title: "問題 8 - 選擇一個適合自己的顏色，讓氣色更好，更白",
            options: [
              { text: "", value: "red", color: "#FF0000" },
              { text: "", value: "red2", color: "#DC143C" },
              { text: "", value: "red3", color: "#B22222" },
              { text: "", value: "red4", color: "#8B0000" },
            ],
          },
        ],
        answers: Array(8).fill(null),
        error: false,
      };
    },
    methods: {
      nextQuestion() {
        if (this.answers[this.currentQuestionIndex]) {
          this.currentQuestionIndex++;
          this.error = false;
        } else {
          this.error = true;
        }
      },
      prevQuestion() {
        if (this.currentQuestionIndex > 0) {
          this.currentQuestionIndex--;
          this.error = false;
        }
      },
      handleSubmit() {
        if (this.answers.includes(null)) {
          this.error = true;
        } else {
          console.log(this.answers);
          this.$router.push("/color_detail_1"); // 提交後進行路由導航
        }
      },
    },
  };
</script>
*/
-->

<!-- 修改後的script  -->
<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  data() {
    return {
      uploadedImage: null,
      uploadedImageFile: null,
      currentQuestionIndex: 0,
      questions:[
        {
          title: "問題 1 - 肌膚",
          options: [
            { text: "容易曬紅或是曬傷", value: "A", color: "" },
            { text: "容易曬黑，曬後立刻暗沈", value: "B", color: "" },
            { text: "先曬紅後轉黑", value: "C", color: "" },
          ],
        },
        {
          title: "問題 2 - 瞳色",
          options: [
            { text: "茶棕色", value: "brown", color: "#654321" },
            { text: "古銅色", value: "brown2", color: "#8B4513" },
            { text: "焦棕色", value: "brown3", color: "#5C4033" },
            { text: "黑棕色", value: "brown4", color: "#3D2B1F" },
          ],
        },
        {
          title: "問題 3 - 髮色",
          options: [
            { text: "淺茶色", value: "tea", color: "#D2B48C" },
            { text: "灰黑色", value: "gray", color: "#708090" },
            { text: "黑茶色", value: "btea", color: "#3B2F2F" },
            { text: "黑色", value: "black", color: "#000000" },
          ],
        },
        {
          title: "問題 4 - 彩度（哪種顏色在您身上看起來最亮？）",
          colors: [
            { value: "A", colors: ["#fef8ca", "#cce6cf", "#efdbd9", "#cae4ec"] },
            { value: "B", colors: ["#fdef87", "#a2d193", "#e7a6a1", "#8fccdf"] },
            { value: "C", colors: ["#f4ea62", "#7fba4a", "#e16565", "#45b0e1"] },
            { value: "D", colors: ["#fdec4d", "#26aa39", "#e72828", "#282aff"] },
            { value: "E", colors: ["#fce610", "#10681d", "#dc0000", "#0000ea"] },
          ],
        },
        {
          title: "問題 5 - 選擇一個適合自己的顏色，讓氣色更好，更白",
          options: [
            { text: "", value: "purple", color: "#800080" },
            { text: "", value: "purple2", color: "#9370DB" },
            { text: "", value: "purple3", color: "#DDA0DD" },
            { text: "", value: "purple4", color: "#EE82EE" },
          ],
        },
        {
          title: "問題 6 - 選擇一個適合自己的顏色，讓氣色更好，更白",
          options: [
            { text: "", value: "yellow", color: "#FFFF00" },
            { text: "", value: "yellow2", color: "#FFD700" },
            { text: "", value: "yellow3", color: "#FFA500" },
            { text: "", value: "yellow4", color: "#FF8C00" },
          ],
        },
        {
          title: "問題 7 - 選擇一個適合自己的顏色，讓氣色更好，更白",
          options: [
            { text: "", value: "orange", color: "#FFA07A" },
            { text: "", value: "orange2", color: "#FF7F50" },
            { text: "", value: "orange3", color: "#FF6347" },
            { text: "", value: "orange4", color: "#FF4500" },
          ],
        },
        {
          title: "問題 8 - 選擇一個適合自己的顏色，讓氣色更好，更白",
          options: [
            { text: "", value: "red", color: "#FF0000" },
            { text: "", value: "red2", color: "#DC143C" },
            { text: "", value: "red3", color: "#B22222" },
            { text: "", value: "red4", color: "#8B0000" },
          ],
        },
      ],
      answers: Array(8).fill(null),
      error: false,
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
    nextQuestion() {
      if (this.answers[this.currentQuestionIndex]) {
        this.currentQuestionIndex++;
        this.error = false;
      } else {
        this.error = true;
      }
    },
    prevQuestion() {
      if (this.currentQuestionIndex > 0) {
        this.currentQuestionIndex--;
        this.error = false;
      }
    },
async handleSubmit() {
  try {
    const formData = new FormData();
    formData.append('skin_color', this.answers[0]);
    formData.append('hair_color', this.answers[1]);
    formData.append('eye_color', this.answers[2]);
    formData.append('description', this.answers[3]);
    formData.append('fitness_problem1', this.answers[4]);
    formData.append('fitness_problem2', this.answers[5]);
    formData.append('fitness_problem3', this.answers[6]);
    formData.append('fitness_problem4', this.answers[7]);
    formData.append('uploaded_image', this.uploadedImageFile);
    const token = sessionStorage.getItem('token');

    const response = await axios.post('http://127.0.0.1:8000/color/add/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${token}`,
      },
    });

    if (response && response.status === 201) {
      console.log('提交成功:', response.data.message);
      this.$router.push('/color_result');
    }
  } catch (error) {
    console.error('提交錯誤:', error);
    const toast = useToast();
    toast.error('提交失敗，請稍後再試');
  }
},
    },
};
</script>


<style scoped>
  .container {
    width: 95%;
    margin: 0 auto;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  }

  header {
    display: flex;
    justify-content: flex-end;
    padding-bottom: 1rem;
  }

  .close-btn {
    font-size: 1.5rem;
    text-decoration: none;
    color: #333;
  }

  .header-image {
    display: block;
    margin: 0 auto 1.5rem;
    width: 300px;
    height: auto;
  }

  main {
    background-color: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  }

  .question-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px;
  }

  .question {
    display: none;
    width: 100%;
  }

  .question.active {
    display: block;
  }

  .question-title {
    font-size: 1.75rem;
    margin-bottom: 1.5rem;
    color: #444;
  }

  .options {
    display: block; /* 选项一行显示 */
  }

  .option-label {
    display: flex;
    align-items: center;
    padding: 0.75rem 1rem;
    background: #f1f3f5;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    margin-bottom: 1rem; /* 增加选项之间的间距 */
  }

  .option-label:hover {
    background-color: #dee2e6;
    transform: translateY(-2px);
  }

  .option-input {
    margin-right: 0.75rem;
  }

  .color-block {
    display: inline-block;
    width: 35px;
    height: 35px;
    border: 2px solid #ccc;
    border-radius: 5px;
    margin-right: 1rem;
  }

  .color-blocks {
    display: flex;
    gap: 0.5rem;
  }

  .button-container {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
  }

  #prev-button,
  #next-button,
  #submit-button {
    background-color: #e6b5ae;
    color: #fff;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1.25rem;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  #prev-button:hover,
  #next-button:hover,
  #submit-button:hover {
    background-color: #f9d9ca;
  }

.image-upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  gap: 1rem;
}

.image-upload-container button,
.image-upload-container input[type="file"] {
  background-color: #f1f1f1;
  color: #333;
  border: 1px solid #ccc;
  padding: 0.75rem 1.5rem;
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

.image-upload-container input[type="file"] {
  padding: 0.75rem;
  width: 230px;
  text-align: center;
  appearance: none;
  display: block;
  -webkit-appearance: none;
  text-align: center;
}

.image-upload-container img {
  margin-top: 1rem;
  max-width: 100%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

</style>
