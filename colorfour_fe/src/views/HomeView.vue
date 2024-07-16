<template>
  <div class="container">
    <section class="banner mb-5">
      <div class="banner-background">
        <img src="@/assets/img/index_banner.jpg" alt="index_banner" class="banner-image img-fluid" />
      </div>
      <div class="banner-text" id="understand">
        <router-link to="/about" class="btn btn-main">了解更多</router-link>
      </div>
    </section>
    <div class="content">
      <div class="content-box">
        <div class="image-text-pair card m-3">
          <img src="@/assets/img/makeup.png" alt="Image 2" class="card-img-top" />
          <div class="card-body text-center">
            <h3 class="card-title">我的氣色</h3>
            <p class="card-text">判斷你的四季型色彩及推薦。</p>
            <router-link to="/color_index" class="btn btn-main">前往</router-link>
          </div>
        </div>
        <div class="image-text-pair card m-3">
          <img src="@/assets/img/community.png" alt="Image 3" class="card-img-top" />
          <div class="card-body text-center">
            <h3 class="card-title">社群互動</h3>
            <p class="card-text">與其他使用者分享穿搭經驗。</p>
            <router-link to="/social_index" class="btn btn-main">前往</router-link>
          </div>
        </div>
        <div class="image-text-pair card m-3">
          <img src="@/assets/img/To_do_list.png" alt="Image 4" class="card-img-top" />
          <div class="card-body text-center">
            <h3 class="card-title">日程安排</h3>
            <p class="card-text">將穿搭推薦納入你的行程表。</p>
            <router-link to="/todo_index" class="btn btn-main">前往</router-link>
          </div>
        </div>
      </div>
    </div>
    <section class="container my-5">
      <div class="row mb-4">
        <div class="col-md-6 order-md-2 d-flex flex-column justify-content-center mx-auto">
          <h2>線上衣櫃</h2>
          <p>把你的實體衣櫃搬到線上，方便管理。</p>
          <router-link to="/closet_index" class="btn btn-main">前往</router-link>
        </div>
        <div class="col-md-6 order-md-1 position-relative">
          <div class="image-container">
            <img src="@/assets/img/closet.png" class="img-fluid rounded" alt="線上衣櫃" />
            <div class="overlay1"></div>
          </div>
        </div>
      </div>
      <div style="height: 100px"></div>
      <div class="row mb-4 extra-margin">
        <div class="col-md-6 d-flex flex-column justify-content-center mx-auto">
          <h2>穿搭建議</h2>
          <p>獲得適合你的穿搭建議。</p>
          <router-link to="/suggest_index" class="btn btn-main">前往</router-link>
        </div>
        <div class="col-md-6 position-relative">
          <div class="image-container">
            <img src="@/assets/img/outfit.png" class="img-fluid rounded" alt="穿搭建議" />
            <div class="overlay2"></div>
          </div>
        </div>
      </div>
      <div class="row mb-4 extra-margin position-relative">
        <div class="overlay3"></div>
        <div class="col-md-6 order-md-2 d-flex flex-column justify-content-center mx-auto adjusted">
          <h2>採購建議</h2>
          <p>判斷你的衣櫃有無重複衣物並提供採購建議。</p>
          <router-link to="/buy" class="btn btn-main">前往</router-link>
        </div>
        <div class="col-md-5 order-md-1 position-relative">
          <div class="image-container">
            <img src="@/assets/img/advice.png" class="img-fluid rounded" alt="採購建議" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  export default {
    name: "HomeView",
  };
</script>

<style scoped>
  .banner {
    width: 90%;
    max-height: 90%;
    margin: 0 auto;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #fff;
    border-radius: 20px;
    overflow: hidden;
  }

  .banner-background {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border-radius: 20px;
  }

  .banner-image {
    width: 100%;
    height: auto;
    object-fit: cover; /* 保持圖片比例並填滿容器 */
  }

  #understand {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-start;
    width: 100%;
    height: 100%;
    padding: 20px;
  }

  #understand a {
    margin-left: 5%;
    margin-bottom: 5%;
  }

  .banner-text {
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 1;
    color: #917b56;
    text-shadow: 2px 2px 4px rgba(127, 125, 125, 0.4);
  }

  /* 三個功能區 */
  .content {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 60px;
    padding-bottom: 60px;
    margin: auto;
  }

  .content-box {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    padding-bottom: 20px;
  }

  .content-box::after {
    content: "";
    display: block;
    width: 100%;
    height: 1px;
    background-color: #ccc;
    margin-top: 20px;
  }

  .image-text-pair {
    width: 30%;
    margin: 0 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    border: 2px solid #ccc;
    padding: 20px;
    border-radius: 10px;
    background-color: white;
  }

  .image img {
    width: 100%;
    height: auto;
    border-radius: 10px;
    margin-bottom: 10px;
  }

  .text {
    max-width: 200px;
    margin-bottom: 20px;
  }

  @media (max-width: 768px) {
    .image-text-pair {
      width: 40%;
      margin: 20px;
    }
  }

  @media (max-width: 500px) {
    .image-text-pair {
      width: 100%;
      margin: 20px;
    }
  }

  /* 下排三 */
  .image-container {
    position: relative;
    display: inline-block;
    max-width: 100%; /* 確保圖片容器不超出畫面寬度 */
    overflow: hidden; /* 隱藏超出範圍的內容 */
  }

  .image-container img {
    display: block;
    border-radius: 10px;
    max-width: 100%; /* 確保圖片不超出容器寬度 */
    height: auto; /* 保持圖片比例 */
  }

  .image-container .overlay1,
  .image-container .overlay2 {
    position: absolute;
    z-index: -1;
    border-radius: 10px;
    max-width: 100%; /* 確保疊加層不超出容器寬度 */
  }

  .image-container .overlay1 {
    top: 150px;
    left: -100px;
    width: 100%;
    height: 80%;
    background-color: #7b695f;
  }

  .image-container .overlay1::after {
    content: "";
    position: absolute;
    top: -200px;
    left: 50px;
    width: 60%;
    height: 100%;
    border: 3px solid #fbf6f3;
    border-radius: 10px;
    z-index: -1;
    max-width: 100%; /* 確保疊加層不超出容器寬度 */
  }

  @media (max-width: 768px) {
    .order-md-2 {
      order: 1 !important;
    }

    .image-container .overlay1 {
      top: 140px;
    }

    .image-container .overlay1::after {
      top: -200px;
    }

    .col-md-6.order-md-2.d-flex.flex-column.justify-content-center.mx-auto {
      order: 2;
      margin-top: 80px;
      margin-bottom: 20px;
    }
  }

  .image-container .overlay2 {
    top: -50px;
    right: -30px;
    width: 100%;
    height: 65%;
    background-color: #c6c6bc;
  }

  @media (max-width: 768px) {
    .col-md-6.d-flex.flex-column.justify-content-center.mx-auto {
      order: 2 !important;
      margin-top: 20px;
    }
  }

  .row .overlay3 {
    position: absolute;
    top: -20px;
    left: -20px;
    width: calc(100% + 40px);
    height: calc(100% + 40px);
    background-color: #fbf6f3;
    z-index: -1;
    border-radius: 10px;
    max-width: 100%;
  }

  .extra-margin {
    margin-top: 100px;
  }

  @media (max-width: 768px) {
    .extra-margin {
      margin-top: 50px;
    }

    .col-md-6.order-md-2.d-flex.flex-column.justify-content-center.mx-auto.adjusted {
      margin-top: 50px;
    }

    .col-md-5.order-md-1.position-relative {
      margin-bottom: 20px;
    }
  }

  h2.featurette-heading {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #333;
  }

  p.lead {
    font-size: 1.25rem;
    margin-bottom: 1.5rem;
    color: #555;
  }

  img {
    max-width: 100%;
    height: auto;
    border-radius: 20px;
  }

  .featurette {
    margin-bottom: 2rem;
  }

  .spacer {
    height: 40px;
    background-color: transparent;
  }

  @media (min-width: 768px) {
    h2.featurette-heading {
      font-size: 2.5rem;
    }

    p.lead {
      font-size: 1.5rem;
    }

    .featurette {
      display: flex;
      align-items: center;
    }

    .featurette:nth-child(odd) .col-md-7 {
      order: 2;
    }

    .featurette:nth-child(odd) .col-md-5 {
      order: 1;
    }
  }
</style>
