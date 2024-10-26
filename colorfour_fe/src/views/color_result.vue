<template>
  <div class="container">
    <header>
      <nav>
        <router-link to="/color_index" class="close-btn" id="close-result">x</router-link>
      </nav>
    </header>
    <main>
      <div class="result-container">
        <h2 class="result-title">{{ this.test_name }} 的測驗結果： {{ title }}</h2>
        <img :src="imageSrc" :alt="`${resultType} 型人`" class="result-image" />
        <div class="result-description">
          <p v-for="paragraph in description" :key="paragraph">{{ paragraph }}</p>
        </div>
        <div class="button-container">
          <button @click="confirmResult" class="confirm-btn">確認紀錄</button>
          <button @click="deleteResult" class="delete-btn">刪除紀錄</button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "color_result",
    data() {
      return {
        title: "",
        description: [],
        imageSrc: "",
        resultType: "",
        test_name: "",
      };
    },
    methods: {
      async fetchTestDetail(id) {
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/color/user-tests/${id}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          const data = response.data;
          console.log("測驗資料:", data);
          this.test_name = data.test_name;
          this.resultType = data.result_type;
          this.imageSrc = data.uploaded_image;
          this.setContentByResultType(data);
        } catch (error) {
          console.error("無法載入測驗詳細資料:", error.response);
        }
      },
      setContentByResultType(data) {
        const contentMap = {
          Spring: {
            title: "春季型人",
            description: [
              "☆ 春季型人具備自然的春天所帶來的美好特質，例如：生機、活潑、明媚。",
              "☆ 他們皮膚明亮，眼神閃耀、光潔，是生活中最具快樂和靚麗的一族。",
              "☆ 適合高明亮、高飽和、生動且清新的色系，如俏皮的春季花卉色調。",
            ],
          },
          Summer: {
            title: "夏季型人",
            description: [
              "☆ 夏季型人就像夏天一樣給人一種溫柔、清新、淡雅的特質。",
              "☆ 他們適合低飽和、低彩度、柔和的淺冷色系，如粉藍色、粉紫色。",
              "☆ 最適合的飾品包括啞光銀色、鑽石和水晶。",
            ],
          },
          Autumn: {
            title: "秋季型人",
            description: [
              "☆ 秋季型人就像秋天一樣穩重、成熟、高雅華貴。",
              "☆ 適合低亮度、厚重大氣的暖色調，如棕色和橄欖綠。",
              "☆ 飾品類適合啞光的金色、琥珀和木質。",
            ],
          },
          Winter: {
            title: "冬季型人",
            description: [
              "☆ 冬季型人聯想到冷冽的冬日空氣和純白的雪。",
              "☆ 適合高彩度的深色系和冰冷色系的純色調。",
              "☆ 飾品類適合銀色、白金色和寶石。",
            ],
          },
        };

        const resultContent = contentMap[data.result_type];
        if (resultContent) {
          this.title = resultContent.title;
          this.description = resultContent.description;
        }
      },
      confirmResult() {
        this.$router.push("/color_index");
      },
      async deleteResult() {
        const id = this.$route.params.id;
        try {
          await axios.delete(`${process.env.VUE_APP_BACKEND_URL}/color/user-tests/${id}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          this.$router.push("/color_test");
        } catch (error) {
          console.error("無法刪除測驗紀錄:", error.response);
        }
      },
    },
    mounted() {
      const id = this.$route.params.id;
      if (!id) {
        console.error("ID 未找到，請檢查路由設定。");
        return;
      }
      this.fetchTestDetail(id);
    },
  };
</script>

<style scoped>
  .container {
    margin-top: 20px;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
  }

  .result-title {
    text-align: center;
    color: #917b56;
    text-shadow: 2px 2px 4px rgba(127, 125, 125, 0.4);
    margin-bottom: 20px;
  }

  .result-image {
    display: block;
    margin: 0 auto 20px;
    max-width: 100%;
    border-radius: 10px;
  }

  .result-description {
    text-align: left;
    font-size: 16px;
    line-height: 1.6;
    color: #333;
    margin-bottom: 30px;
  }

  .button-container {
    display: flex;
    justify-content: space-around;
  }

  .confirm-btn,
  .delete-btn {
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .confirm-btn {
    background-color: #4caf50;
    color: white;
  }

  .delete-btn {
    background-color: #f44336;
    color: white;
  }
</style>
