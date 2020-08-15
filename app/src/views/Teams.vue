<template>
  <div class="view-teams">
    <app-page-header :title="'Teams'"
      :desc="'Browse and edit your teams/team members'">
    </app-page-header>
    <b-container>
      <b-row class="mb-5 justify-content-center">
        <b-button class="add-btn" @click="addTeam()">Add New Team</b-button>
      </b-row>
      <b-row class="justify-content-center">
        <div v-if="pageTeams.length > 0">
          <app-team v-for="team in pageTeams" :key="team.team_id" 
            :label="team.label" :id="team.team_id" :members="team.members">
          </app-team>
          <hr class="my-3">
          <b-pagination v-model="currentPage" :total-rows="rows" :per-page="perPage"
            first-text="First" prev-text="Prev" next-text="Next" last-text="Last"
            @input="paginate(currentPage)" align="center">
          </b-pagination>
        </div>
        <div v-else>
          <h3>No teams found <b>: (</b></h3>
        </div>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import TeamCardGroup from '@/components/TeamCardGroup.vue';
  import PageHeader from '@/components/PageHeader.vue';
  import {mapGetters} from 'vuex';

  export default {
    name: 'Teams',
    components: {
      'app-team': TeamCardGroup,
      'app-page-header': PageHeader
    },
    computed: {
      ...mapGetters(['teams', 'pageTeams', 'rows'])
    },
    data(){
      return {
        currentPage: 1,
        perPage: 3
      }
    },
    mounted(){
      this.fillTeams();
    },
    methods: {
      async fillTeams(){
        await this.$store.dispatch('fetchTeams');
      },
      async addTeam(){
        await this.$store.dispatch('addTeam', {label: 'New Team'});
        await this.paginate(this.currentPage);
      },
      async paginate(currentPage){
        await this.$store.dispatch('paginate', {currentPage, perPage: this.perPage});
      }
    }
  }
</script>

<style lang="scss">
  .add-btn{
    border: 4px solid black;
  }

  .add-btn:hover{
    border: 4px solid black;
    transform: rotate(3deg);
  }
</style>