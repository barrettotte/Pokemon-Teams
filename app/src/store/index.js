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
    currentPage: 1,
    perPage: 3,
    activeTeam: null,
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
    currentPage(state){
      return state.currentPage;
    },
    perPage(state){
      return state.perPage;
    },
    activeTeam(state){
      return state.activeTeam;
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
      state.teams = teams;
    },
    SET_ROWS(state, rows){
      state.rows = rows;
    },
    SET_PAGE_TEAMS(state, pageTeams){
      state.pageTeams = pageTeams;
    },
    SET_CURRENT_PAGE(state, currentPage){
      state.currentPage = currentPage;
    },
    SET_PER_PAGE(state, perPage){
      state.perPage = perPage;
    },
    SET_ACTIVE_TEAM(state, activeTeam){
      state.activeTeam = activeTeam;
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
      // TODO: strip url into config/env var
      const res = await axios.get('http://127.0.0.1:8020/api/v1/pokedex/'); 
      return res['data']['data'];
    },

    async requestTeams(){
      // TODO: strip url into config/env var
      const res = await axios.get('http://127.0.0.1:8020/api/v1/teams/'); 
      const teams = res['data']['data'].sort((a,b) => a.team_id - b.team_id).reverse();
      for(var i = 0; i < teams.length; i++){
        const membersRes = await axios.get(`http://127.0.0.1:8020/api/v1/teams/${teams[i]['team_id']}`);
        teams[i].members = membersRes['data']['data']['members'].sort((a,b) => a.slot - b.slot);
      }
      return teams;
    },

    async addTeam({commit, dispatch, state}, {label}){
      commit('SET_SPINNER', true);
      const res = await axios.post('http://127.0.0.1:8020/api/v1/teams/', {label: label});
      const new_id = res['data']['data']['team_id'];
      const teams = state.teams;

      teams.unshift({label: label, team_id: new_id, members: []});
      dispatch('updatePagination', {data: teams, currentPage: state.currentPage, perPage: state.perPage});

      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
      return new_id;
    },

    async deleteTeam({commit, dispatch, state}, {id}){
      commit('SET_SPINNER', true);
      await axios.delete(`http://127.0.0.1:8020/api/v1/teams/${id}`);
      const teams = state.teams;
      
      const deleteIdx = teams.map(team => team.team_id).indexOf(id);
      teams.splice(deleteIdx, 1);
      console.log('deleting ' + deleteIdx)

      dispatch('updatePagination', {data: teams, currentPage: state.currentPage, perPage: state.perPage});

      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
    },

    editTeam({commit, state}, {id}){
      console.log('Editing activated for ' + id);
      commit('SET_ACTIVE_TEAM', id);
      if(state.activeTeam !== null){
        // commit prior active team's stuff
      }
    },

    // async saveTeam({dispatch, commit}, {id}){

    // },

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
      commit('SET_CURRENT_PAGE', currentPage);
      commit('SET_PER_PAGE', perPage);
    },

    updatePagination({commit, dispatch}, {data, currentPage, perPage}){
      commit('SET_TEAMS', data);
      commit('SET_ROWS', data.length);
      dispatch('paginate', {currentPage, perPage});
    },

    async search({dispatch}, {text}){
      const data = await this.dispatch('requestTeams');
      const results = data.filter(val => val.label.toLowerCase().includes(text.toLowerCase()));
      dispatch('updatePagination', {data: results, currentPage: 1, perPage: 3});
    }
  },
  modules: {}
});
