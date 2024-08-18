<template>
  <div>
    <div id="header"></div>

    <main class="container">
      <div class="row my-4">
        <div class="col-12">
          <!-- 這裡要自動帶入表單標題  title + 推薦結果 -->
          <h3>{{ title }}推薦結果</h3>
        </div>
      </div>
      <div class="row">
        <div v-for="(recommendation, index) in recommendations" :key="index" class="col-12 col-md-4 mb-3">
          <div class="card" :class="{ selected: selectedIndex === index }">
            <img :src="recommendation.imgSrc" class="card-img-top" :alt="recommendation.altText" />
            <div class="card-body text-center">
              <button class="btn btn-primary save-button" @click="selectRecommendation(index)">選擇</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row my-4">
        <div class="col-12 text-center">
          <button class="btn btn-primary submit-button" @click="submitSelection">確認送出</button>
        </div>
      </div>
    </main>
    <div id="footer"></div>
  </div>
</template>

<script>
export default {
    name:"suggest_results",
  data() {
    return {
      title: '表演服',
      recommendations: [
        { imgSrc: require('@/assets/img/suggest_01.png'), altText: '推薦1' },
        { imgSrc: require('@/assets/img/suggest_02.png'), altText: '推薦2' },
        { imgSrc: 'https://picsum.photos/300/200?random=1', altText: '推薦3' }
      ],
      selectedIndex: null
    };
  },
  methods: {
    selectRecommendation(index) {
      this.selectedIndex = index;
    },
    submitSelection() {
      if (this.selectedIndex !== null) {
        alert('儲存成功！');
        this.$router.push({ path: '/suggest_index' });
      } else {
        alert('請選擇一個推薦方案！');
      }
    }
  }
};
</script>

<style scoped>
.card.selected {
  border: 2px solid #ff5555;
  box-shadow: 0 0 10px rgba(255, 123, 255, 0.5);
}
</style>
