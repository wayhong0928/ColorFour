<template>
  <main class="container">
    <div class="row mb-4">
      <div class="col-md-6 order-md-2 text-left">
        <div class="text-center">
          <h3 class="featurette-heading">秋季型人</h3>
        </div>
        <p>☆ 秋季型人就像秋天一樣穩重、成熟、高雅華貴。正如大自然的秋天帶給我們秋意深濃、一叢金黃的感覺，</p>
        <p>
          ☆
          他們是大地色的代言人，給人深邃知性美的感覺。
        </p>
        <p>☆ 秋季型適合低亮度、厚重大氣的暖色調，就像是秋天一樣沉穩。</p>
        <p>☆ 帶暖橘色調或混濁的色彩會是不錯的選擇，如棕色、卡其色、暖橘色、橄欖綠、磚紅色等。</p>
        <p>☆ 應該避免穿冷色調及鮮艷的顏色，太淡的顏色或冷色調會讓秋季型人皮膚暗沉、泛黃，顯得氣色不好。</p>
        <p>☆ 飾品類適合啞光的金色、琥珀、瑪瑙、銅色、木質的飾品。</p>
        <p>☆ 若搭配了適合的顏色：</p>
        <p>&emsp;&ensp;✓ 讓血色感變好</p>
        <p>&emsp;&ensp;✓ 肌膚看起來像陶器般平滑</p>
        <p>&emsp;&ensp;✓ 輪廓看起來更俐落</p>
      </div>
      <div class="col-md-6 order-md-1">
        <img src="@/assets/img/autumn_person.jpg" class="img-fluid rounded" alt="秋季型明星" />
      </div>
    </div>

    <section class="text-center">
      <h3>適合的色彩</h3>
      <table class="table table-bordered color-table">
        <tbody>
          <tr>
            <td style="background-color: #f7c080"></td>
            <td style="background-color: #f4a23e"></td>
            <td style="background-color: #feda0d"></td>
            <td style="background-color: #b7bf36"></td>
            <td style="background-color: #877e43"></td>
            <td style="background-color: #4fb8ae"></td>
            <td style="background-color: #aa7d3c"></td>
          </tr>
          <tr>
            <td style="background-color: #ed6d50"></td>
            <td style="background-color: #f0851b"></td>
            <td style="background-color: #deae48"></td>
            <td style="background-color: #667d31"></td>
            <td style="background-color: #967029"></td>
            <td style="background-color: #04787e"></td>
            <td style="background-color: #64471f"></td>
          </tr>
          <tr>
            <td style="background-color: #e23726"></td>
            <td style="background-color: #e67817"></td>
            <td style="background-color: #9faa70"></td>
            <td style="background-color: #4a9433"></td>
            <td style="background-color: #312519"></td>
            <td style="background-color: #f3e4bb"></td>
            <td style="background-color: #7c401d"></td>
          </tr>
          <tr>
            <td style="background-color: #e13728"></td>
            <td style="background-color: #a20612"></td>
            <td style="background-color: #b7bf50"></td>
            <td style="background-color: #0f492b"></td>
            <td style="background-color: #4b3065"></td>
            <td style="background-color: #d6ae65"></td>
            <td style="background-color: #322618"></td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- Add the "重新測驗" button here -->
    <div class="text-center retest-button">
      <button @click="goToRetest" class="btn btn-primary mt-3">重新測驗</button>
    </div>
  </main>
</template>

<script>
export default {
  name: 'color_detail',
  methods: {
    goToRetest() {
      this.$router.push({ name: 'color_retest' }); // Assuming the route name is 'color_retest'
    }
  }
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
  margin-top: -40px; /* 调整此值以控制按钮与上方元素之间的距离 */
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
