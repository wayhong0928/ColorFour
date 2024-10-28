<template>
  <main class="container">
    <div class="row mb-4">
      <div class="col-md-6 order-md-2 text-left">
        <div class="text-center">
          <h3 class="featurette-heading">{{ title }}</h3>
          <p>測驗日期：{{ formatDate(testDate) }}</p>
          <p v-for="paragraph in description" :key="paragraph">{{ paragraph }}</p>
        </div>
        <div class="text-center retest-button">
          <button class="btn btn-outline-secondary me-2" @click="goBack">返回</button>
          <button @click="goToRetest" class="btn btn-primary me-2">重新測驗</button>
        </div>
      </div>
      <div class="col-md-6 order-md-1">
        <img :src="uploadedImage" class="img-fluid rounded" :alt="`${resultType} 型人`" />
      </div>
    </div>

    <section class="text-center">
      <h3>適合的色彩</h3>
      <table class="table table-bordered color-table">
        <tbody>
          <tr v-for="(row, rowIndex) in colorRows" :key="rowIndex">
            <td v-for="(color, colorIndex) in row" :key="colorIndex" :style="{ backgroundColor: color }"></td>
          </tr>
        </tbody>
      </table>
    </section>
  </main>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        uploadedImage: "",
        resultType: "",
        title: "",
        description: [],
        colorRows: [],
        testDate: "", // 測驗日期
      };
    },
    methods: {
      async fetchTestDetail() {
        const id = this.$route.params.id; // 從路由參數中取得 ID
        try {
          const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/color/user-tests/${id}/`, {
            headers: {
              Authorization: `Bearer ${sessionStorage.getItem("my-app-auth")}`,
            },
          });
          const data = response.data;
          this.uploadedImage = data.uploaded_image;
          this.resultType = data.result_type;
          this.testDate = data.test_date;
          this.setContentByResultType();
        } catch (error) {
          console.error("無法載入測驗詳細資料:", error.response);
        }
      },
      setContentByResultType() {
        const contentMap = {
          Spring: {
            title: "春季型人",
            description: [
              "☆ 春季型人具備自然的春天所帶來的美好特質，例如：生機、活潑、明媚。",
              "☆ 他們皮膚明亮，眼神閃耀、光潔，是生活中最具快樂和靚麗的一族，正如大自然春天帶給我們的欣悅一般，春季型人是朝氣而充滿活力的。",
              "☆ 適合高明亮、高飽和、生動且清新的色系，如俏皮的春季花卉色調。",
              "☆ 黃色是首選，帶有淡黃色調的象牙白、橘紅色、略帶黃色的淺藍色等，都是不錯的選擇。",
              "☆ 盡量避免穿黑色，過深過重的顏色會蓋著自己的光芒，也襯托不出春季型人的俏麗和光彩。",
              "☆ 飾品類適合光澤明亮的黃金飾品。",
              "☆ 若搭配了適合的顏色：",
              "✓ 臉部變得明亮",
              "✓ 可呈現出血色感",
              "✓ 看起來彈力有光澤、生氣蓬勃",
            ],
            colorRows: [
              ["#f7d0c3", "#ec7c88", "#f2993f", "#a9cf60", "#a2d7db", "#3a548f", "#e6c88c"],
              ["#f9c498", "#e9636e", "#ffed53", "#80bf4a", "#989dba", "#914a8c", "#d8ae64"],
            ],
          },
          Summer: {
            title: "夏季型人",
            description: [
              "☆ 夏季型人就像夏天一樣給人一種溫柔、清新、淡雅的特質。",
              "☆ 他們給人溫婉飄逸、柔和而親切的感覺，如同一潭靜謐的湖水。",
              "☆ 適合低飽和、低彩度、柔和的淺冷色系，如粉藍色、粉紫色。",
              "☆ 也非常適合帶白或帶灰的莫蘭迪色系，涼爽沉靜的顏色最能襯托出夏季型人自身的氣質。",
              "☆ 最好避免過於沉重或太純淨的顏色。",
              "☆ 飾品類適合啞光銀色、鑽石、水晶、寶石、乳白色珍珠。",
              "☆ 若搭配了適合的顏色：",
              "✓ 顯白、肌膚看起來變明亮",
              "✓ 呈現出透明感",
              "✓ 肌膚看起來光滑",
            ],
            colorRows: [
              ["#f4cfd7", "#e73d64", "#c1517f", "#a6d2ae", "#73bce7", "#c5bfe1", "#ab8767"],
              ["#f3b3c3", "#e5314a", "#e46a9b", "#67bd90", "#5082ad", "#913381", "#784f39"],
            ],
          },
          Autumn: {
            title: "秋季型人",
            description: [
              "☆ 秋季型人就像秋天一樣穩重、成熟、高雅華貴。",
              "☆ 他們是大地色的代言人，給人深邃知性美的感覺。",
              "☆ 適合低亮度、厚重大氣的暖色調，如棕色、卡其色、橄欖綠。",
              "☆ 應避免穿冷色調及鮮艷的顏色，會讓皮膚暗沉、泛黃。",
              "☆ 飾品類適合啞光的金色、琥珀、瑪瑙、木質的飾品。",
              "☆ 若搭配了適合的顏色：",
              "✓ 讓血色感變好",
              "✓ 肌膚看起來像陶器般平滑",
              "✓ 輪廓看起來更俐落",
            ],
            colorRows: [
              ["#f7c080", "#f4a23e", "#feda0d", "#b7bf36", "#877e43", "#4fb8ae", "#aa7d3c"],
              ["#ed6d50", "#f0851b", "#deae48", "#667d31", "#967029", "#04787e", "#64471f"],
            ],
          },
          Winter: {
            title: "冬季型人",
            description: [
              "☆ 冬季型人讓人聯想到冷冽的冬日空氣、純白的雪。",
              "☆ 他們給人酷帥、華麗的氣質，本身的存在感非常強烈。",
              "☆ 適合高彩度的深色系色彩及冰冷色系的純色調。",
              "☆ 純正、飽和的色彩最能襯托出冬季型人的存在感。",
              "☆ 應避免統一或相鄰的色彩搭配。",
              "☆ 飾品類適合閃亮的銀色、白金色、寶石。",
              "☆ 若搭配了適合的顏色：",
              "✓ 看起來洗練俐落",
              "✓ 緊緻輪廓",
              "✓ 肌膚看起來有光澤",
            ],
            colorRows: [
              ["#f19dbf", "#b01f2e", "#09aa5c", "#0ba1de", "#fae3e5", "#dff1f3", "#888888"],
              ["#e76e9b", "#c40d23", "#016d3c", "#00469e", "#fffad4", "#e2d5e7", "#413b3b"],
            ],
          },
        };

        const resultContent = contentMap[this.resultType];
        if (resultContent) {
          this.title = resultContent.title;
          this.description = resultContent.description;
          this.colorRows = resultContent.colorRows;
        }
      },
      goToRetest() {
        this.$router.push({ name: "color_retest" });
      },
      formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString(); // 格式化為日期+時間
      },
      goBack() {
        this.$router.go(-1); // 返回上一頁
      },
    },
    mounted() {
      this.fetchTestDetail(); // 取得測驗詳細資料
    },
  };
</script>

<style scoped>
  /* Add main content specific styles here */
  .container {
    margin-top: 15px;
    margin-bottom: 30px;
  }

  .text-center {
    color: #917b56;
    text-shadow: 2px 2px 4px rgba(127, 125, 125, 0.4);
    text-align: center;
    justify-content: center;
    align-items: center;
    padding-bottom: 15px;
  }

  .text-left p {
    font-size: 16px;
    font-weight: 350;
    margin-right: 7%;
  }

  .color-table {
    width: 100%;
    margin: 20px 0;
    border-collapse: separate;
    border-spacing: 10px;
    padding-bottom: 50px;
  }
  .color-table td {
    width: 50px;
    height: 50px;
    border-radius: 10px;
  }
  /* 调整图片的容器和图片样式 */
  .col-md-6.order-md-1 {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
  }

  .col-md-6.order-md-1 img {
    max-width: 100%;
    height: auto;
    object-fit: cover;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .retest-button {
    margin-top: 10px; 
  }

  /* 小屏幕下调整图片样式 */
  @media (max-width: 768px) {
    .col-md-6.order-md-1 {
      text-align: center;
    }

    .col-md-6.order-md-1 img {
      max-width: 80%;
      margin-top: 10px;
    }
  }
</style>
