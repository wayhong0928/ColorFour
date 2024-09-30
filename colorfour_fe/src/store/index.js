import { createStore } from "vuex";
import auth from './modules/auth';

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

export default createStore({
  modules: {
    auth,
    collection // 新增收藏模組
  },
});
