<template>
  <div>
    <div id="header"></div>
    <main class="container">
      <!-- test area -->
      <div>
        <h1>User Profile</h1>
        <div v-if="user">
          <p><strong>First Name:</strong> {{ user.first_name }}</p>
          <p><strong>Last Name:</strong> {{ user.last_name }}</p>
          <p><strong>Email:</strong> {{ user.email }}</p>
          <!-- test area -->
        </div>
        <div v-else>
          <p>Loading...</p>
        </div>
      </div>
      <!--  -->
      <div class="row my-4">
        <!-- Existing profile information section -->
        <div class="col-6 d-flex justify-content-between align-items-center">
          <div>
            <img
              src="https://picsum.photos/100/100?random=1"
              alt="user profile image"
              class="rounded-circle"
              width="100"
              height="100"
            />
            <div>
              <h2>ColorFour</h2>
              <p>@ColorFourAdmin</p>
              <p>讓你的專屬穿搭造型師，給你點顏色瞧瞧！</p>
            </div>
          </div>
          <div></div>
        </div>
        <div class="col-6">
          <!-- Existing stats section -->
          <div class="row my-4">
            <div class="col-12">
              <div class="d-flex flex-column align-items-start position-relative">
                <p>男性</p>
                <p>0 貼文 | 0 粉絲 | 0 追蹤中</p>
                <img src="@/assets/img/bell_icon.png" alt="gender icon" class="corner-icon" />
              </div>
            </div>
          </div>
          <div></div>
        </div>
      </div>

      <!-- Buttons section -->
      <div class="buttons d-flex justify-content-center">
        <button
          class="btn btn-outline-secondary d-flex justify-content-center"
          style="width: 45%; margin: 0 2%; border-radius: 20px"
        >
          分享個人檔案
        </button>
        <a
          href="#personal-info"
          class="btn btn-outline-secondary d-flex justify-content-center"
          style="width: 45%; margin: 0 2%; border-radius: 20px"
        >
          編輯個人簡介
        </a>
      </div>

      <!-- Navigation tabs section -->
      <div class="row my-4">
        <div class="col-12">
          <ul class="nav nav-tabs d-flex justify-content-center" style="border-radius: 10px">
            <li class="nav-item">
              <a class="nav-link active" style="border-radius: 10px" href="#">我的貼文</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" style="border-radius: 10px" href="#">收藏穿搭</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" style="border-radius: 10px" href="#">最愛單品</a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Existing content for no posts -->
      <div class="row my-4">
        <div class="col-12 text-center">
          <p>尚未發布任何穿搭</p>
        </div>
      </div>

      <!-- New profile information section with two columns -->
      <div class="row my-4">
        <div class="col-lg-6">
          <h3>個人色彩分析結果</h3>
          <div class="result-item">
            <span class="date">2023/12/25</span> 夏季型人
            <br />
            ☆ 若搭配了適合的顏色
            <br />
            ✓ 顯白、肌膚看起來變明亮
            <br />
            ✓ 呈現出透明感
            <br />
            ✓ 肌膚看起來光滑
            <br />
            <img src="@/assets/img/next_icon.png" class="icon" alt="next icon" />
          </div>
          <div class="line-qr-code">
            <h4>Line QR-code</h4>
            <img src="@/assets/img/line_QRcode.png" alt="Line QR-code" class="img-fluid" />
          </div>
        </div>

        <div class="col-lg-6" id="personal-info">
          <h3>個人資訊</h3>
          <div class="mb-3">
            <label for="nickname" class="form-label">暱稱設定</label>
            <input type="text" class="form-control" id="nickname" placeholder="輸入暱稱" />
          </div>
          <div class="mb-3">
            <label for="id" class="form-label">ID設定</label>
            <input type="text" class="form-control" id="id" placeholder="輸入ID" />
          </div>
          <div class="mb-3">
            <label for="birthday" class="form-label">生日</label>
            <input type="date" class="form-control" id="birthday" />
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" placeholder="輸入Email" />
          </div>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
  import axios from "axios";
  export default {
    name: "user_profile",
    data() {
      return {
        user: null,
      };
    },
    async mounted() {
      try {
        const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}/dj-rest-auth/user/`);
        this.user = response.data;
      } catch (error) {
        console.error("Failed to fetch user profile:", error);
      }
    },
  };
</script>

<style scoped>
  .container {
    width: 90%;
    display: flex;
    flex-direction: column;
    max-width: 1200px;
    margin: 100px auto 100px auto;
  }

  .img-fluid {
    border-radius: 10px;
  }

  .nav-tabs .nav-link {
    color: #333;
  }

  .nav-tabs .nav-link.active {
    color: #000;
    font-weight: bold;
  }

  .text-center p {
    font-size: 1.2rem;
    color: #777;
  }

  .rounded-circle {
    border-radius: 50%;
  }

  /* Two-column layout */
  .result-item {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
  }

  .result-item .date {
    font-weight: bold;
    display: block;
    margin-bottom: 10px;
  }

  .line-qr-code img {
    max-width: 50%;
    height: auto;
    border-radius: 10px;
  }

  .icon {
    width: 20px; /* Adjust the size as needed */
    height: 20px;
    margin-left: 5px; /* Add some margin if needed */
  }

  /* Position small icon in the top right corner */
  .corner-icon {
    width: 26px;
    height: 26px;
    position: absolute;
    top: 0;
    right: 0;
    transform: translate(50%, -50%); /* Adjust position to align with the corner */
  }

  @media (min-width: 992px) {
    .col-lg-6 {
      margin-bottom: 20px;
    }
  }
</style>
