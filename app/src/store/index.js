import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    pokedexEntries: [],
    members: [],
    displayMembers: [],
    rows: 0,
    showSpinner: false
  },
  getters: {
    pokedexEntries(state){
      return state.pokedexEntries;
    },
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
    SET_POKEDEX_ENTRIES(state, pokedexEntries){
      state.pokedexEntries = pokedexEntries;
    },
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
    async simulateLoad(){
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve();
        }, 500)
      });
    },
    async fetchPokedex(){
      const res = await axios.get('http://127.0.0.1:8020/api/v1/pokedex/'); // TODO: strip url into config/env var
      return res['data']['data'];
    },

    // TODO: switch to HTTP to Flask server
    async fetchData(){
      const res = await fetch('test.json');
      const val = await res.json();
      return val;
    },

    async fetchMembers({dispatch, commit}){
      commit('SET_SPINNER', true);
      const res = await dispatch('fetchData');
      await dispatch('simulateLoad');
      commit('SET_MEMBERS', res);
      commit('SET_ROWS', res.length);
      commit('SET_DISPLAY_MEMBERS', res.slice(0, 3));
      commit('SET_ROWS', res.length);
      commit('SET_SPINNER', false);
    },

    async fetchPokedexEntries({dispatch, commit}){
      commit('SET_SPINNER', true);
      const res = await dispatch('fetchPokedex');
      await dispatch('simulateLoad');
      commit('SET_POKEDEX_ENTRIES', res);
      commit('SET_SPINNER', false);
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
});
