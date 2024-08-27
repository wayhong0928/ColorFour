<template>
  <div>
    <div id="header"></div>
    <main class="main-content container">
      <div class="left-sidebar">
        <div class="icon-search">
          <img src="@/assets/img/search_icon.png" alt="Search Icon" />
          <input type="text" placeholder="search" />
        </div>

        <div class="icon-link">
          <router-link to="social_index">
            <img src="@/assets/img/social_home_icon.png" alt="Home Icon" />
            <span>社群平台首頁</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_collect">
            <img src="@/assets/img/like_icon.png" alt="Saved Posts Icon" />
            <span>收藏貼文</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_follow_list">
            <img src="@/assets/img/followers_icon.png" alt="Overview Icon" />
            <span>追蹤總覽</span>
          </router-link>
        </div>
      </div>

      <div id="follow-list-container" class="content">
        <div v-for="follower in followers" :key="follower.id" class="follower-row">
          <div class="follower-info">
            <img :src="follower.avatar" alt="Follower Avatar" class="follower-avatar rounded-circle" />
            <router-link :to="{ name: 'user_profile', params: { userId: follower.id } }" class="follower-name">
              {{ follower.name }}
            </router-link>
            <div class="follower-actions">
              <button @click="toggleFollow(follower)" class="follow-button btn btn-outline-primary">
                {{ follower.isFollowing ? '追蹤中' : '追蹤' }}
              </button>
              <button @click="unfollow(follower)" class="unfollow-icon btn btn-outline-danger">
                &times;
              </button>
            </div>
          </div>
          <div class="color-analysis">
            {{ follower.colorAnalysis }}
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
  data() {
    return {
      followers: [
        {
          id: 1,
          name: "小紅",
          avatar: "https://picsum.photos/40?random=1",
          isFollowing: true,
          colorAnalysis: "春季型人"
        },
        {
          id: 2,
          name: "小明",
          avatar: "https://picsum.photos/40?random=2",
          isFollowing: true,
          colorAnalysis: "夏季型人"
        },
        {
          id: 3,
          name: "小花",
          avatar: "https://picsum.photos/40?random=3",
          isFollowing: true,
          colorAnalysis: "秋季型人"
        },
      ],
    };
  },
  methods: {
    toggleFollow(follower) {
      follower.isFollowing = !follower.isFollowing;
    },
    unfollow(follower) {
      this.followers = this.followers.filter((f) => f.id !== follower.id);
    },
  },
};
</script>



<style scoped>
.main-content {
  width: 90%;
  position: relative;
  display: flex;
  flex-direction: column;
}

.follower-row {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
  max-width: 600px;
  margin: 0 auto;
}

.follower-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap; /* Allow wrapping for small screens */
}

.follower-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.follower-name {
  font-size: 1.2em;
  color: #333;
  text-decoration: none;
  margin-left: 5px;
}

.color-analysis {
  background-color: #f0f0f0;
  padding: 5px 10px;
  border-radius: 4px;
  margin-top: 10px; /* Ensure spacing on small screens */
}

.follower-name:hover {
  text-decoration: underline;
}

.follow-button {
  border-radius: 20px;
  padding: 5px 10px;
  margin-right: 10px;
}

.unfollow-icon {
  border-radius: 20px;
  padding: 1px 5px;
}

.left-sidebar {
  width: 200px;
  background-color: #f0f0f0;
  padding: 20px;
  position: fixed;
  top: 70px;
  left: 0;
  height: calc(100% - 120px);
  overflow-y: auto;
  z-index: 10;
  transition: all 0.3s ease;
}

.left-sidebar .icon-search,
.left-sidebar .icon-link {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.left-sidebar .icon-search img,
.left-sidebar .icon-link img {
  margin-right: 10px;
  width: 30px;
  height: 30px;
  transition: all 0.3s ease;
}

.left-sidebar .icon-search input {
  flex: 1;
}

.left-sidebar .icon-link a {
  text-decoration: none;
  color: var(--primary-text-color);
  font-weight: 600;
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .left-sidebar {
    width: 100%;
    position: fixed;
    top: 90px;
    left: 0;
    height: 60px;
    display: flex;
    justify-content: space-around;
    padding: 15px;
    background-color: var(--header-footer-bg-color);
  }

  .main-content {
    margin-top: 90px;
  }

  .left-sidebar .icon-search {
    display: none;
  }

  .left-sidebar .icon-link {
    flex-direction: column;
    align-items: center;
    margin-bottom: 0;
  }

  .left-sidebar .icon-link span {
    display: none;
  }

  .left-sidebar .icon-link img {
    margin-right: 0;
    width: 40px;
    height: 40px;
  }
}

.left-sidebar .icon-search input {
  width: 100px; /* 设置搜索框的宽度 */
  height: 30px; /* 设置搜索框的高度 */
  padding: 5px; /* 调整内边距 */
  font-size: 14px; /* 调整字体大小 */
  border-radius: 10px; /* 调整圆角 */
  border: 1px solid #ccc; /* 设置边框 */
}

/* 在小屏幕时也可以相应调整搜索框大小 */
@media (max-width: 768px) {
  .left-sidebar .icon-search input {
    width: 100px; /* 调整小屏幕时的宽度 */
    height: 25px; /* 调整小屏幕时的高度 */
    font-size: 12px; /* 调整小屏幕时的字体大小 */
  }
}

@media (max-width: 768px) {
  .follower-info {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }

  .color-analysis {
    margin-top: 10px;
    display: block; /* Ensure it’s on a new line */
  }

  .follower-actions {
    display: flex;
    align-items: center;
  }
}
</style>
