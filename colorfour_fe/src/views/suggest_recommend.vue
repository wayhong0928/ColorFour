<template>
  <div>
    <div id="header"></div>
    <main class="container">
      <div class="row my-4">
        <div class="col-12">
          <h2 class="text-center my-3">請選擇智慧穿搭推薦選項</h2>
          <form @submit.prevent="submitForm">
            <div class="mb-3">
              <label for="title" class="form-label">推薦穿搭名稱</label>
              <input type="text" class="form-control" id="title" v-model="formData.title" required />
            </div>
            <div class="mb-3">
              <label for="location" class="form-label">目的地（將會自動抓取天氣資訊）</label>
              <input type="text" class="form-control" id="location" v-model="formData.location" required />
            </div>
            <div class="mb-3">
              <label for="occasion" class="form-label">場合/目的</label>
              <div class="border p-3 mb-3">{{ Array.isArray(formData.occasion) ? formData.occasion.join(", ") : formData.occasion }}</div>
              <div id="occasion" class="btn-group flex-wrap" role="group">
                <button v-for="option in occasionOptions" :key="option" type="button"
                        class="btn btn-outline-secondary m-1"
                        :class="{ selected: formData.occasion.includes(option) }"
                        @click="toggleSelection('occasion', option)">
                  {{ option }}
                </button>
              </div>
            </div>
            <div class="mb-3">
              <label for="color" class="form-label">我的氣色</label>
              <div class="border p-3 mb-3">{{ formData.color.join(", ") }}</div>
              <div id="color" class="btn-group flex-wrap" role="group">
                <button v-for="option in colorOptions" :key="option" type="button"
                        class="btn btn-outline-secondary m-1"
                        :class="{ selected: formData.color.includes(option) }"
                        @click="toggleSelection('color', option)">
                  {{ option }}
                </button>
              </div>
            </div>
            <div class="mb-3">
              <label for="want" class="form-label">想要穿搭的服飾種類</label>
              <div class="border p-3 mb-3">{{ formData.want.join(", ") }}</div>
              <div id="want" class="btn-group flex-wrap" role="group">
                <button v-for="option in wantOptions" :key="option" type="button"
                        class="btn btn-outline-secondary m-1"
                        :class="{ selected: formData.want.includes(option) }"
                        @click="toggleSelection('want', option)">
                  {{ option }}
                </button>
              </div>
            </div>
            <div class="mb-3">
              <label for="notWant" class="form-label">不想穿搭的服飾種類</label>
              <div class="border p-3 mb-3">{{ formData.notWant.join(", ") }}</div>
              <div id="not-want" class="btn-group flex-wrap" role="group">
                <button v-for="option in notWantOptions" :key="option" type="button"
                        class="btn btn-outline-secondary m-1"
                        :class="{ selected: formData.notWant.includes(option) }"
                        @click="toggleSelection('notWant', option)">
                  {{ option }}
                </button>
              </div>
            </div>
            <div class="submit-section">
            <button type="submit" class="btn btn-primary">送出</button>
            <button class="back-button" @click="goBack">返回</button>
            </div>
          </form>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "suggest_recommend",
  data() {
    return {
      formData: {
        recommendation_name: '', // 替換 title 為 recommendation_name 為了更後端對應
        location: '',
        occasion: '', //對應後端改成字串
        color: [],
        want: [],
        notWant: []
      },
      occasionOptions: ['春天', '夏天', '秋天', '冬天', '百搭', '休閒', '正式', '報告', '商務', '旅行', '海邊', '山上', '露營'],
      colorOptions: ['素顏', '淡妝', '全妝'],
      wantOptions: ['上衣', '長袖T恤', '短袖T恤', '無袖上衣', '長袖襯衫', '短袖襯衫', '帽T/大學T', '針織衫', '毛衣', '長裙', '短裙', '連身裙', '吊帶褲', '牛仔褲', '一般長褲', '短褲', '外套', '大衣', '風衣', '皮夾克', '羽絨外套', '洋裝', '禮服', '西裝外套', '西裝褲', '西裝裙'],
      notWantOptions: ['上衣', '長袖T恤', '短袖T恤', '無袖上衣', '長袖襯衫', '短袖襯衫', '帽T/大學T', '針織衫', '毛衣', '長裙', '短裙', '連身裙', '吊帶褲', '牛仔褲', '一般長褲', '短褲', '外套', '大衣', '風衣', '皮夾克', '羽絨外套', '洋裝', '禮服', '西裝外套', '西裝褲', '西裝裙']
    };
  },
  methods: {
    toggleSelection(type, option) {
      if (type === 'occasion') {
        this.formData.occasion = option;  // 直接儲存為字串
      } else {
        const index = this.formData[type].indexOf(option);
        if (index > -1) {
          this.formData[type].splice(index, 1);
        } else {
          this.formData[type].push(option);
        }
      }
    },
    async submitForm() {
      // 將 title 映射為 recommendation_name
      this.formData.recommendation_name = this.formData.title;

      // 將 occasion 轉為單一字串（只取第一個選擇的值）
      if (Array.isArray(this.formData.occasion) && this.formData.occasion.length > 0) {
        this.formData.occasion = this.formData.occasion[0];
      }

      try {
        const response = await axios.post(
          'http://localhost:8000/recommender/recommendations/recommend/',
          this.formData
        );
        console.log('成功提交表單', response.data);
        alert('推薦已提交成功');
        this.$router.push({ path: '/suggest_results' });
      } catch (error) {
        console.error(
          '提交推薦失敗',
          error.response ? error.response.data : error  // 捕捉詳細錯誤
        );
        alert('提交失敗，請稍後再試');
      }
    },
    goBack() {
      this.$router.go(-1);
    }
  }
};
</script>

<style scoped>
.border {
  border: 1px solid #dee2e6;
  border-radius: 5px;
}

.selected {
  background-color: #6c757d !important;
  color: white;
}

.submit-section button {
  padding: 10px 20px;
  background-color: #d4b7a1;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  margin: 0 10px; /* 增加按鈕間距 */
}
</style>

