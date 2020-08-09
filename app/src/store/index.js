import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    members: [],
    displayMembers: [],
    rows: 0,
    showSpinner: false
  },
  getters: {
    members(state){
      return state.members;
    },
    rows(state){
      return state.rows;
    },
    displayMembers(state){
      return state.displayMembers;
    },
    showSpinner(state){
      return state.showSpinner;
    }
  },
  mutations: {
    SET_MEMBERS(state, members){
      state.members = members;
    },
    SET_ROWS(state, rows){
      state.rows = rows;
    },
    SET_DISPLAY_MEMBERS(state, displayMembers){
      state.displayMembers = displayMembers;
    },
    SET_SPINNER(state, spinner){
      state.showSpinner = spinner;
    }
  },
  actions: {
    async fetchData({commit}){
      commit('SET_SPINNER', true);
      return new Promise(resolve => {
        setTimeout(async () => {
          const res = await fetch('test.json');
          const val = await res.json();
          resolve(val);
          commit('SET_SPINNER', false);
        }, 500); // simulate delay of getting data (spinner)
      });
    },
    async fetchMembers({dispatch, commit}){
      const data = await dispatch('fetchData');
      commit('SET_MEMBERS', data);
      commit('SET_ROWS', data.length);
      commit('SET_DISPLAY_MEMBERS', data.slice(0, 3));
      commit('SET_ROWS', data.length);
    },
    async paginate({commit, state}, {currentPage, perPage}){
      const start = (currentPage - 1) * perPage;
      commit('SET_DISPLAY_MEMBERS', state.members.slice(start, start + 3));
    },
    updatePagination({commit, dispatch}, {data, currentPage, perPage}){
      commit('SET_MEMBERS', data);
      commit('SET_ROWS', data.length);
      dispatch('paginate', {currentPage, perPage});
    },
    async search({dispatch}, {text}){
      const data = await this.dispatch('fetchData');
      const results = data.filter(val => val.name.toLowerCase().includes(text.toLowerCase()));
      dispatch('updatePagination', {data: results, currentPage: 1, perPage: 3});
    }
  },
  modules: {}
})
