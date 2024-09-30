<template>
  <div class="container">
    <header>
      <nav>
        <router-link to="/color_index" class="close-btn" id="close-result">x</router-link>
      </nav>
    </header>
    <main>
      <div class="result-container">
        <h2 class="result-title">您的測驗結果：春季型人</h2>
        <img src="@/assets/img/spring_person.jpeg" alt="春季型人" class="result-image" />
        <div class="result-description">
          <p>☆ 春季型人具備自然的春天所帶來的美好特質，例如：生機、活潑、明媚。</p>
          <p>
            ☆
            他們皮膚明亮，眼神閃耀、光潔，是生活中最具快樂和靚麗的一族，正如大自然春天帶給我們的欣悅一般，春季型人是朝氣而充滿活力的。
          </p>
          <p>☆ 適合高明亮、高飽和、生動且清新的色系，像是俏皮的春季花卉色調。</p>
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
export default {
  name: "color_result",
  methods: {
    confirmResult() {
      // 在此處添加確認紀錄的邏輯，例如將數據存儲到數據庫中
      this.$router.push('/color_index'); // 假設確認後跳轉到詳細頁面
    },
    deleteResult() {
      // 在此處添加刪除紀錄的邏輯，例如清除測驗結果
      this.$router.push('/color_test'); // 假設刪除後返回測驗頁面
    }
  }
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

.confirm-btn, .delete-btn {
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
