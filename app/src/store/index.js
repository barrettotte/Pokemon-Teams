import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    pokedexEntries: [],
    sprites: [],
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
    sprites(state){
      return state.sprites;
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
    SET_SPRITES(state, sprites){
      state.sprites = sprites;
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
      const res = await axios.get(`${process.env.VUE_APP_API_ROOT}/api/v1/pokedex/`); 
      return res['data']['data'];
    },

    async requestSprites(){
      const res = await axios.get(`${process.env.VUE_APP_API_ROOT}/api/v1/sprites/`); 
      const sprites = res['data']['data'];
      return sprites;
    },

    fetchSprite({state}, {dexId, form}){
      return state.sprites.find(s => s.form === form && s.dex_id === dexId);
    },

    fetchPokedexEntry({state}, {dexno}){
      return state.pokedexEntries[dexno - 1];
    },

    async requestTeams(){
      const res = await axios.get(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/`); 
      const teams = res['data']['data'].sort((a,b) => a.team_id - b.team_id).reverse();
      for(var i = 0; i < teams.length; i++){
        const membersRes = await axios.get(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/${teams[i]['team_id']}`);
        teams[i].members = membersRes['data']['data']['members'].sort((a,b) => a.slot - b.slot);
      }
      return teams;
    },

    async addTeam({commit, dispatch, state}, {label}){
      commit('SET_SPINNER', true);
      const res = await axios.post(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/`, {label: label});
      const newId = res['data']['data']['team_id'];
      const teams = state.teams;

      teams.unshift({label: label, team_id: newId, members: []});
      dispatch('updatePagination', {data: teams, currentPage: state.currentPage, perPage: state.perPage});

      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
      commit('SET_ACTIVE_TEAM', newId);
      return newId;
    },

    async deleteTeam({commit, dispatch, state}, {teamId}){
      commit('SET_SPINNER', true);
      await axios.delete(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/${teamId}`);
      const teams = state.teams;
      
      const deleteIdx = teams.map(team => team.team_id).indexOf(teamId);
      teams.splice(deleteIdx, 1);
      dispatch('updatePagination', {data: teams, currentPage: state.currentPage, perPage: state.perPage});

      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
    },

    editTeam({commit, state}, {teamId}){
      if(state.activeTeam !== null){
        // TODO: commit prior active team's stuff
      }
      commit('SET_ACTIVE_TEAM', teamId);
    },

    async saveTeam({commit, dispatch, state}, {teamId, label, members}){
      commit('SET_SPINNER', true);
      await axios.put(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/${teamId}/`, {label});

      const teamIdx = state.teams.map(team => team.team_id).indexOf(teamId);
      state.teams[teamIdx].label = label;
      state.teams[teamIdx].members = members.filter(mbr => mbr.member_id > 0);

      commit('SET_ACTIVE_TEAM', null);
      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
    },

    async addMember({commit, dispatch}, {teamId, memberData}){
      commit('SET_SPINNER', true);
      const res = await axios.post(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/${teamId}/members`, memberData);
      const newId = res['data']['data']['member_id'];
      
      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
      return newId;
    },

    async updateMember({commit, dispatch}, {teamId, memberId, memberData}){
      commit('SET_SPINNER', true);
      await axios.put(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/${teamId}/members/${memberId}`, memberData);
      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
    },

    async deleteMember({commit, dispatch, state}, {teamId, memberId, slotIdx}){
      commit('SET_SPINNER', true);
      await axios.delete(`${process.env.VUE_APP_API_ROOT}/api/v1/teams/${teamId}/members/${memberId}`);

      const teamIdx = state.teams.map(team => team.team_id).indexOf(teamId);
      state.teams[teamIdx].members = state.teams[teamIdx].members.filter(mbr => mbr.slot !== slotIdx);

      await dispatch('simulateLoad');
      commit('SET_SPINNER', false);
    },

    async populateDataStore({dispatch, commit}){
      commit('SET_SPINNER', true);
      await dispatch('fetchPokedexEntries');
      await dispatch('fetchTeams');
      await dispatch('fetchSprites');
      commit('SET_SPINNER', false);
    },

    async fetchSprites({dispatch, commit}){
      const res = await dispatch('requestSprites');
      await dispatch('simulateLoad');
      commit('SET_SPRITES', res);
    },

    async fetchTeams({dispatch, commit}){
      const res = await dispatch('requestTeams');
      await dispatch('simulateLoad');
      commit('SET_TEAMS', res);
      commit('SET_ROWS', res.length);
      commit('SET_PAGE_TEAMS', res.slice(0, 3));
      commit('SET_ROWS', res.length);
    },

    async fetchPokedexEntries({dispatch, commit}){
      const res = await dispatch('requestPokedex');
      await dispatch('simulateLoad');
      commit('SET_POKEDEX_ENTRIES', res);
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
