<template>
  <div class="user-setting">
    <!-- 登入帳戶管理 -->
    <div class="account-management">
      <h3>登入帳戶管理</h3>
      <div class="linked-accounts">
        <div v-if="isGoogleLinked" class="account-item linked"><i class="fab fa-google"></i> Google 已連結</div>
        <div v-if="isLineLinked" class="account-item linked"><i class="fab fa-line"></i> Line 已連結</div>
        <div v-if="!isGoogleLinked" class="account-item" @click="connectGoogle">
          <i class="fab fa-google"></i> Google 尚未連結
        </div>
        <div v-if="!isLineLinked" class="account-item" @click="connectLine"><i class="fab fa-line"></i> Line 尚未連結</div>
      </div>
    </div>

    <!-- 編輯個人資料 -->
    <div class="personal-info">
      <h3>編輯個人資料</h3>
      <div class="form-group">
        <label for="nickname">暱稱</label>
        <input type="text" id="nickname" v-model="nickname" placeholder="輸入暱稱" />
      </div>
      <div class="form-group">
        <label for="birthday">生日</label>
        <input type="date" id="birthday" v-model="birthday" />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" placeholder="輸入Email" />
      </div>
      <button @click="savePersonalInfo">保存</button>
    </div>

    <!-- 彈出登入框 -->
    <div v-if="showPopup" class="popup-overlay">
      <div class="popup-content">
        <h3>{{ popupTitle }}</h3>
        <p>這裡是 {{ popupTitle }} 的模擬登入畫面。</p>
        <button @click="closePopup">關閉</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "user_setting",
  data() {
    return {
      isGoogleLinked: false, // 模擬Google是否已連結
      isLineLinked: false, // 模擬Line是否已連結
      nickname: "", // 使用者暱稱
      birthday: "", // 使用者生日
      email: "", // 使用者Email
      showPopup: false, // 控制彈出框顯示
      popupTitle: "", // 彈出框標題
    };
  },
  methods: {
    connectGoogle() {
      this.popupTitle = "Google 登入";
      this.showPopup = true;
    },
    connectLine() {
      this.popupTitle = "Line 登入";
      this.showPopup = true;
    },
    closePopup() {
      this.showPopup = false;
    },
    savePersonalInfo() {
      // 模擬保存個人資料
      console.log("個人資料已保存", {
        nickname: this.nickname,
        birthday: this.birthday,
        email: this.email,
      });
      // 你可以在此添加實際的保存邏輯，例如發送API請求
    },
  },
};
</script>

<style scoped>
.user-setting {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

.account-management,
.personal-info {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h3 {
  margin-bottom: 15px;
  color: #333;
  font-size: 20px;
}

.linked-accounts {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.account-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
  color: #555;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  transition: background-color 0.3s ease;
  cursor: pointer;
}

.account-item.linked {
  background-color: #e0f7fa;
}

.account-item:hover {
  background-color: #f1f1f1;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #666;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  color: #333;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #d4b7a1;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #b3957e;
}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  background: white;
  padding: 30px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}
</style>
