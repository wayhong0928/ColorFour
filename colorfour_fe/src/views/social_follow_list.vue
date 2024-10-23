<template>
  <div>
    <nav aria-label="breadcrumb">
      <ol class="bread">
        <li><router-link to="/user_profile">會員管理</router-link></li>
        <li><router-link to="/social_index">社群首頁</router-link></li>
        <li aria-current="page">追蹤中</li>
      </ol>
    </nav>
    <div id="header"></div>
    <main class="main-content container">
      <!-- 這裡我們要顯示 followingList 中的資料 -->
      <div id="follow-list-container" class="content">
        <h2 class="follow_list">追蹤名單</h2>
        <div v-for="follower in followingList" :key="follower.id" class="follower-row">
          <div class="follower-info">
            <img src="https://picsum.photos/25" alt="User Avatar" class="post-avatar rounded-circle" />
            <router-link :to="{ name: 'user_profile', params: { userId: follower.id } }" class="follower-name">
              {{ follower.username }}
            </router-link>
            <div class="follower-actions">
              <button
                @click="toggleFollow(follower)"
                :class="{ 'btn-primary': follower.isFollowing, 'btn-outline-primary': !follower.isFollowing }"
              >
                {{ follower.isFollowing ? "已追蹤" : "追蹤" }}
              </button>
              <button @click="unfollow(follower)" class="btn btn-outline-danger">&times;</button>
            </div>
          </div>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from "vuex";

  export default {
    computed: {
      ...mapGetters("follow", ["followingList"]),
    },
    methods: {
      ...mapActions("follow", ["followUser", "unfollowUser"]),
      async toggleFollow(follower) {
        try {
          if (follower.isFollowing) {
            await this.unfollowUser(follower.username);
          } else {
            await this.followUser(follower);
          }
          alert("追蹤狀態已更新！");
        } catch (error) {
          console.error("更新追蹤狀態失敗：", error);
        }
      },
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

  .main-content {
    width: 90%;
    position: relative;
    display: flex;
    flex-direction: column;
  }

  .post-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .follow_list {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    background-color: var(--primary-bg-color);
    color: #917b56;
    margin-bottom: 30px;
  }

  .follower-row {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fff;
    max-width: 600px;
    margin: 0 auto;
    margin-bottom: 10px;
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

  /* Responsive styles */
  @media (max-width: 768px) {
    .left-sidebar {
      width: 100%;
      position: fixed;
      top: 60px;
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
    width: 100px; /* Set the width of the search box */
    height: 30px; /* Set the height of the search box */
    padding: 5px; /* Adjust padding */
    font-size: 14px; /* Adjust font size */
    border-radius: 10px; /* Adjust border radius */
    border: 1px solid #ccc; /* Set border */
  }

  /* Adjust search box size on small screens */
  @media (max-width: 768px) {
    .left-sidebar .icon-search input {
      width: 100px; /* Adjust width for small screens */
      height: 25px; /* Adjust height for small screens */
      font-size: 12px; /* Adjust font size for small screens */
    }
  }

  @media (max-width: 768px) {
    .follower-info {
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
    }

    .follower-actions {
      display: flex;
      align-items: center;
    }
  }
</style>
