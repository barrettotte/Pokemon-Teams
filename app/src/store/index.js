import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    pokedexEntries: [],
    teams: [],
    pageTeams: [],
    rows: 0,
    showSpinner: false
  },
  getters: {
    pokedexEntries(state){
      return state.pokedexEntries;
    },
    teams(state){
      return state.teams;
    },
    rows(state){
      return state.rows;
    },
    pageTeams(state){
      return state.pageTeams;
    },
    showSpinner(state){
      return state.showSpinner;
    }
  },
  mutations: {
    SET_POKEDEX_ENTRIES(state, pokedexEntries){
      state.pokedexEntries = pokedexEntries;
    },
    SET_TEAMS(state, teams){
      state.members = teams;
    },
    SET_ROWS(state, rows){
      state.rows = rows;
    },
    SET_PAGE_TEAMS(state, pageTeams){
      state.pageTeams = pageTeams;
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

    async requestPokedex(){
      const res = await axios.get('http://127.0.0.1:8020/api/v1/pokedex/'); // TODO: strip url into config/env var
      return res['data']['data'];
    },

    async requestTeams(){
      const res = await fetch('test.json');
      const val = await res.json();
      return val;
      // TODO:
      // const res = await axios.get('http://127.0.0.1:8020/api/v1/teams/');
      // return res['data']['data'];
    },

    async fetchTeams({dispatch, commit}){
      commit('SET_SPINNER', true);
      const res = await dispatch('requestTeams');
      await dispatch('simulateLoad');
      commit('SET_TEAMS', res);
      commit('SET_ROWS', res.length);
      commit('SET_PAGE_TEAMS', res.slice(0, 3));
      commit('SET_ROWS', res.length);
      commit('SET_SPINNER', false);
    },

    async fetchPokedexEntries({dispatch, commit}){
      commit('SET_SPINNER', true);
      const res = await dispatch('requestPokedex');
      await dispatch('simulateLoad');
      commit('SET_POKEDEX_ENTRIES', res);
      commit('SET_SPINNER', false);
    },

    async paginate({commit, state}, {currentPage, perPage}){
      const start = (currentPage - 1) * perPage;
      commit('SET_PAGE_TEAMS', state.teams.slice(start, start + 3));
    },

    updatePagination({commit, dispatch}, {data, currentPage, perPage}){
      commit('SET_TEAMS', data);
      commit('SET_ROWS', data.length);
      dispatch('paginate', {currentPage, perPage});
    },

    async search({dispatch}, {text}){
      const data = await this.dispatch('requestTeams');
      const results = data.filter(val => val.name.toLowerCase().includes(text.toLowerCase()));
      dispatch('updatePagination', {data: results, currentPage: 1, perPage: 3});
    }
  },
  modules: {}
});
