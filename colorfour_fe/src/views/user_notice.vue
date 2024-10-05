<template> 
  <div>
    <div id="header"></div>
    <ol class="bread">
        <li><router-link to="/user_profile">ㄑ</router-link></li>
      </ol>
    <main class="container">
      <div v-if="loading" class="text-center my-4">
        <p>Loading...</p>
      </div>
      <div v-else-if="error" class="text-center my-4">
        <p>{{ error }}</p>
      </div>
      <div v-else>
        <div class="row my-4">
          <!-- Notification Title -->
          <div class="col-12">
            <div class="notification-tabs">
              <button class="tab active-tab">動態消息</button>
            </div>
            <ul class="list-group">
              <!-- Render each notification item -->
              <li v-for="notice in notices" :key="notice.id" class="list-group-item d-flex align-items-center">
                <div class="notice-content">
                  <p>{{ notice.message }}</p>
                  <small>{{ formatDate(notice.date) }}</small>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
export default {
  name: "user_notice",
  data() {
    return {
      loading: true,
      error: null,
      notices: [], // Your notification data
    };
  },
  methods: {
    async fetchNotices() {
      try {
        this.loading = true;
        // Simulate an API call to fetch user notices
        // Replace this with your actual API request
        this.notices = await this.getFakeNotices(); 
      } catch (error) {
        this.error = "無法載入通知，請稍後再試。";
      } finally {
        this.loading = false;
      }
    },
    getFakeNotices() {
      // This is a placeholder, replace with your real data fetching logic
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve([
            { id: 1, message: "你有一個新的留言", date: "2024-10-02", thumbnail: "path-to-thumbnail1.jpg" },
            { id: 2, message: "你的收藏已更新", date: "2024-09-30", thumbnail: "path-to-thumbnail2.jpg" },
          ]);
        }, 1000);
      });
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    },
  },
  mounted() {
    this.fetchNotices(); // Fetch notices when component is mounted
  },
};
</script>

<style scoped>
.bread {
    display: flex;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .bread li {
    padding: 0 20px;
  }

  .bread li + li {
    padding-left: 0;
  }

  .bread li + li:before {
    content: ">";
    color: #333;
    margin-right: 20px;
  }

  .bread a {
    text-decoration: none;
    color: #333;
  }

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding-top: 20px;
}

h2 {
  font-weight: bold;
  margin-bottom: 20px;
}

.notification-tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.tab {
  background: none;
  border: none;
  font-size: 30px;
  margin: 0 10px;
  padding: 10px 20px;
  cursor: pointer;
  border-bottom: 2px solid transparent;
}

.active-tab {
  border-bottom: 2px solid black;
}

.list-group-item {
  display: flex;
  align-items: center;
  padding: 15px;
  border-radius: 10px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
  border: 1px solid #eaeaea;
}

.notice-icon {
  width: 40px;
  height: 40px;
  margin-right: 15px;
}

.notice-content {
  flex: 1;
}

.notice-thumbnail {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
}
</style>
