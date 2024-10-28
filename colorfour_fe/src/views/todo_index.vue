<template>
  <div>
    <div class="container text-center">
      <h2>穿搭日程</h2>
      <div class="my-4">
        <button @click="showModal = true" class="btn btn-custom">新增穿搭</button>
      </div>

      <!-- 穿搭日程顯示區域 -->
      <div v-if="schedules.length">
        <h3>已安排的日程</h3>
        <div class="d-flex justify-content-between align-items-center mb-3">
          <button @click="deleteSelected" class="btn btn-custom">刪除選中項目</button>
        </div>
        <ul class="list-group">
          <li v-for="(schedule, index) in sortedSchedules" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
            <div class="form-check">
              <input type="checkbox" class="form-check-input" v-model="schedule.selected" />
              <label class="form-check-label"></label>
            </div>
            <div class="schedule-info d-flex flex-column">
              <span class="schedule-date">日期：{{ schedule.date }}</span>
              <span class="schedule-title">穿搭：{{ schedule.recTitles.join(', ') }}</span>
            </div>
            <button @click="showDetail(schedule)" class="btn btn-custom detail-btn">詳細資訊</button>
          </li>
        </ul>
      </div>

      <!-- 新增穿搭的 Modal -->
      <div v-if="showModal" class="modal-backdrop">
        <div class="modal-content">
          <h3>選擇穿搭組合</h3>
          <div class="form-group">
            <label for="date">選擇日期：</label>
            <input type="date" v-model="newSchedule.date" />
          </div>
          <div class="form-group">
            <h4>可選擇的推薦穿搭：</h4>
            <div v-for="rec in recommendations" :key="rec.id" class="form-check">
              <input type="checkbox" class="form-check-input" v-model="newSchedule.selectedRecs" :value="rec.id" />
              <label class="form-check-label">{{ rec.title }}</label>
            </div>
          </div>
          <div class="text-center mt-3">
            <button @click="saveSchedule" class="btn btn-custom">儲存</button>
            <button @click="showModal = false" class="btn btn-custom ml-2">取消</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "todo_index",
  data() {
    return {
      showModal: false,
      newSchedule: {
        date: '',
        selectedRecs: []
      },
      schedules: [], // 存儲已安排的日程
      recommendations: [
        { id: 1, title: "表演服" },
        { id: 2, title: "期末報告穿搭" },
        { id: 3, title: "上課裝" },
      ],
    };
  },
  computed: {
    sortedSchedules() {
      return this.schedules.sort((a, b) => new Date(a.date) - new Date(b.date));
    },
  },
  methods: {
    saveSchedule() {
      if (this.newSchedule.date && this.newSchedule.selectedRecs.length > 0) {
        // 根據選中的推薦項目ID來找出相對應的名稱
        const recTitles = this.newSchedule.selectedRecs.map(recId => {
          const rec = this.recommendations.find(r => r.id === recId);
          return rec ? rec.title : '';
        });

        // 儲存包含日期與推薦名稱的日程
        this.schedules.push({
          date: this.newSchedule.date,
          selectedRecs: this.newSchedule.selectedRecs,
          recTitles: recTitles,  // 儲存穿搭名稱
          selected: false
        });
        this.newSchedule = { date: '', selectedRecs: [] }; // 重置
        this.showModal = false;
      } else {
        alert("請選擇日期和穿搭組合");
      }
    },
    deleteSelected() {
      this.schedules = this.schedules.filter(schedule => !schedule.selected);
    },
    showDetail(schedule) {
      // 實現查看詳細資訊的邏輯
      console.log("查看詳細資訊", schedule);
    },
  },
};
</script>


<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

h2, h3 {
  font-weight: bold;
}

.my-4 {
  margin: 20px 0;
}

.list-group {
  padding: 0;
}

.list-group-item {
  padding: 15px;
  border-radius: 10px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.schedule-date {
  flex: 1;
  text-align: center; /* 日期至中 */
}

.schedule-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* 對齊到左邊 */
  margin-left: 10px; /* 調整與勾選框的距離 */
}

.schedule-date,
.schedule-title {
  margin: 0; /* 移除預設邊距 */
}


button {
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
}

.btn-custom {
  background-color: #d4b7a1;
  color: white;
  border: none;
  transition: background-color 0.3s ease;
}

.btn-custom:hover {
  background-color: #D9A68C;
  color: white;
}

.detail-btn {
  margin-left: auto;
  margin-right: 0;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

.form-check {
  margin-bottom: 10px;
}

.text-center {
  text-align: center;
}

.mt-3 {
  margin-top: 15px;
}

.ml-2 {
  margin-left: 10px;
}
</style>
