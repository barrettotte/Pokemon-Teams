<template>
  <div class="view-teams">
    <app-page-header :title="'Teams'"
      :desc="'Browse and edit your teams/team members'">
    </app-page-header>
    <div v-if="pageTeams.length > 0">
      
        <app-team v-for="team in pageTeams" :key="team.team_id" :label="team.label" :id="team.team_id">
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
      paginate(currentPage){
        this.$store.dispatch('paginate', {currentPage, perPage: this.perPage});
      }
    }
  }
</script>

<style lang="scss">

</style>