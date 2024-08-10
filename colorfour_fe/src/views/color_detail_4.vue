<template>
  <main class="container">
    <div class="row mb-4">
      <div class="col-md-6 order-md-2 text-left">
        <div class="text-center">
          <h3 class="featurette-heading">冬季型人</h3>
        </div>
        <p>☆ 冬季型人就像冬天一樣讓人聯想到冷冽的冬日空氣、純白的雪、聖誕中與綠色強烈對比的紅、黑色和夜空中閃亮的星星。</p>
        <p>
          ☆
          他們給人酷帥、華麗的氣質，本身的存在感非常強烈。
        </p>
        <p>☆ 適合高彩度的深色系色彩及冰冷色系的純色調。</p>
        <p>☆ 純正、飽和的色彩最能襯托出冬季型人本身的存在感，不僅不會顯得突兀，也完全不會輸給鮮艷的顏色。</p>
        <p>☆ 應避免統一或相鄰的色彩搭配，低彩度和低飽和度的顏色也無法展現他們的魅力。</p>
        <p>☆ 飾品類適合閃亮的銀色、白金色、純正色彩的珍珠及寶石。應該盡量避免黃金類和木製品。</p>
        <p>☆ 若搭配了適合的顏色：</p>
        <p>&emsp;&ensp;✓ 看起來洗練俐落</p>
        <p>&emsp;&ensp;✓ 緊緻輪廓</p>
        <p>&emsp;&ensp;✓ 肌膚看起來有光澤</p>
      </div>
      <div class="col-md-6 order-md-1">
        <img src="@/assets/img/winter_person.jpg" class="img-fluid rounded" alt="冬季型明星" />
      </div>
    </div>

    <section class="text-center">
      <h3>適合的色彩</h3>
      <table class="table table-bordered color-table">
        <tbody>
          <tr>
            <td style="background-color: #f19dbf"></td>
            <td style="background-color: #b01f2e"></td>
            <td style="background-color: #09aa5c"></td>
            <td style="background-color: #0ba1de"></td>
            <td style="background-color: #fae3e5"></td>
            <td style="background-color: #dff1f3"></td>
            <td style="background-color: #888888"></td>
          </tr>
          <tr>
            <td style="background-color: #e76e9b"></td>
            <td style="background-color: #c40d23"></td>
            <td style="background-color: #016d3c"></td>
            <td style="background-color: #00469e"></td>
            <td style="background-color: #fffad4"></td>
            <td style="background-color: #e2d5e7"></td>
            <td style="background-color: #413b3b"></td>
          </tr>
          <tr>
            <td style="background-color: #e75582"></td>
            <td style="background-color: #e5007e"></td>
            <td style="background-color: #11492c"></td>
            <td style="background-color: #0d3191"></td>
            <td style="background-color: #ecefda"></td>
            <td style="background-color: #fefefe"></td>
            <td style="background-color: #322618"></td>
          </tr>
          <tr>
            <td style="background-color: #982d4d"></td>
            <td style="background-color: #f4ef89"></td>
            <td style="background-color: #252853"></td>
            <td style="background-color: #262656"></td>
            <td style="background-color: #d6e8dc"></td>
            <td style="background-color: #c9c9c9"></td>
            <td style="background-color: #c9c9c9"></td>
          </tr>
        </tbody>
      </table>
    </section>
  </main>
</template>

<script>
export default {
  name: 'color_detail'
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

.text-center::after {
  content: "";
  display: block;
  width: 93%;
  height: 1px;
  background-color: #ccc;
  margin-top: 15px;
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
