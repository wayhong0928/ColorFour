import { createStore } from "vuex";
import auth from './modules/auth';

// 模組：追蹤
const follow = {
  namespaced: true, // 啟用命名空間，避免命名衝突
  state: {
    followingList: []
  },
  mutations: {
    FOLLOW_USER(state, user) {
      // 檢查用戶是否已經存在於追蹤列表
      const existingUser = state.followingList.find(u => u.username === user.username);
      if (!existingUser) {
        // 如果用戶尚未在追蹤列表中，將其加入，並設置 isFollowing 為 true
        state.followingList.push({ ...user, isFollowing: true });
      }
    },
    UNFOLLOW_USER(state, username) {
      // 將指定用戶從追蹤列表中移除
      state.followingList = state.followingList.filter(user => user.username !== username);
    },
    UPDATE_FOLLOW_STATUS(state, { username, isFollowing }) {
      const user = state.followingList.find(user => user.username === username);
      if (user) {
        user.isFollowing = isFollowing;
      }
    }
  },
  actions: {
    followUser({ commit }, user) {
      commit('FOLLOW_USER', user);
    },
    unfollowUser({ commit }, username) {
      commit('UNFOLLOW_USER', username);
    },
    toggleFollowStatus({ commit, state }, username) {
      const isFollowing = state.followingList.some(user => user.username === username);
      commit('UPDATE_FOLLOW_STATUS', { username, isFollowing: !isFollowing });
    }
  },
  getters: {
    isFollowing: (state) => (username) => {
      return state.followingList.some(user => user.username === username && user.isFollowing);
    },
    followingList: (state) => state.followingList
  }
};


// 收藏貼文的模組
const collection = {
  state: {
    collectedPosts: []
  },
  mutations: {
    ADD_TO_COLLECTION(state, post) {
      const isAlreadyCollected = state.collectedPosts.some(p => p.id === post.id);
      if (!isAlreadyCollected) {
        state.collectedPosts.push(post);
      }
    },
    REMOVE_POST_FROM_COLLECTION(state, post) {
      // 从收藏中移除帖子
      state.collectedPosts = state.collectedPosts.filter(p => p.id !== post.id);
    }
  },
  actions: {
    addToCollection({ commit }, post) {
      commit('ADD_TO_COLLECTION', post);
    },
    removeFromCollection({ commit }, post) {
      commit('REMOVE_POST_FROM_COLLECTION', post);
    }
  },
  getters: {
    collectedPosts: (state) => state.collectedPosts
  },
  removePost(post) {
    this.removeFromCollection(post); // 调用 Vuex 的 action 来移除收藏帖子
  }
};

// 建立 Vuex Store
export default createStore({
  modules: {
    follow,
    auth,
    collection
  },
});