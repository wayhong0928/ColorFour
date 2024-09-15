<template>
  <main class="container">
    <div class="row mb-4">
      <div class="col-md-6 order-md-2 text-left">
        <div class="text-center">
          <h3 class="featurette-heading">夏季型人</h3>
        </div>
        <p>☆ 夏季型人就像夏天一樣給人一種溫柔、清新、淡雅的特質。</p>
        <p>
          ☆
          他們給人溫婉飄逸、柔和而親切的感覺，如同一潭靜謐的湖水，會使人在焦躁中慢慢沉靜下來，去感受清靜的空間。
        </p>
        <p>☆ 適合低飽和、低彩度、柔和的淺冷色系。如給人恬靜的粉藍色、粉紫色；代表知性的藍灰色、海軍藍；可以表現可愛的淺檸檬黃、淺粉色。</p>
        <p>☆ 也非常適合帶白或帶灰的莫蘭迪色系，涼爽沉靜的顏色最能襯托出夏季型人自身的氣質。</p>
        <p>☆ 最好避免過於沉重的顏色，以及太純淨的顏色，太暗的色彩或過於明亮的色彩會奪去自身柔和的氣質。</p>
        <p>☆ 飾品類適合啞光銀色、鑽石、水晶、寶石、乳白色珍珠、玻璃質感等飾品。應盡量避免黃金類、木製品和銅製品。</p>
        <p>☆ 若搭配了適合的顏色：</p>
        <p>&emsp;&ensp;✓ 顯白、肌膚看起來變明亮</p>
        <p>&emsp;&ensp;✓ 呈現出透明感</p>
        <p>&emsp;&ensp;✓ 肌膚看起來光滑</p>
      </div>
      <div class="col-md-6 order-md-1">
        <img src="@/assets/img/summer_person.jpg" class="img-fluid rounded" alt="夏季型明星" />
      </div>
    </div>

    <section class="text-center">
      <h3>適合的色彩</h3>
      <table class="table table-bordered color-table">
        <tbody>
          <tr>
            <td style="background-color: #f4cfd7"></td>
            <td style="background-color: #e73d64"></td>
            <td style="background-color: #c1517f"></td>
            <td style="background-color: #a6d2ae"></td>
            <td style="background-color: #73bce7"></td>
            <td style="background-color: #c5bfe1"></td>
            <td style="background-color: #ab8767"></td>
          </tr>
          <tr>
            <td style="background-color: #f3b3c3"></td>
            <td style="background-color: #e5314a"></td>
            <td style="background-color: #e46a9b"></td>
            <td style="background-color: #67bd90"></td>
            <td style="background-color: #5082ad"></td>
            <td style="background-color: #913381"></td>
            <td style="background-color: #784f39"></td>
          </tr>
          <tr>
            <td style="background-color: #f19dbf"></td>
            <td style="background-color: #cc293a"></td>
            <td style="background-color: #f7f0ba"></td>
            <td style="background-color: #01a87c"></td>
            <td style="background-color: #426585"></td>
            <td style="background-color: #fcfbe6"></td>
            <td style="background-color: #98aab4"></td>
          </tr>
          <tr>
            <td style="background-color: #ed7bae"></td>
            <td style="background-color: #cd005b"></td>
            <td style="background-color: #d1ecf3"></td>
            <td style="background-color: #b6ddec"></td>
            <td style="background-color: #374560"></td>
            <td style="background-color: #faeac9"></td>
            <td style="background-color: #5c5f64"></td>
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
