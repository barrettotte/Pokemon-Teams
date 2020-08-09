<template>
  <div class="view-teams">
    <app-page-header :title="'Teams'"
      :desc="'Browse and edit your teams/team members'">
    </app-page-header>
    <div v-if="displayMembers.length > 0">
        <b-container>
          <b-row align-v="center">
            <app-member v-for="member in displayMembers" :key="member.id" 
              :name="member.name" :id="member.id">
            </app-member>
          </b-row>
        </b-container>
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
  import MemberCard from '@/components/MemberCard.vue';
  import PageHeader from '@/components/PageHeader.vue';
  import {mapGetters} from 'vuex';

  export default {
    name: 'Teams',
    components: {
      'app-member': MemberCard,
      'app-page-header': PageHeader
    },
    computed: {
      ...mapGetters(['members', 'displayMembers', 'rows'])
    },
    data(){
      return {
        currentPage: 1,
        perPage: 3
      }
    },
    mounted(){
      this.fetchData();
    },
    methods: {
      async fetchData(){
        await this.$store.dispatch('fetchMembers');
      },
      paginate(currentPage){
        this.$store.dispatch('paginate', {currentPage, perPage: this.perPage});
      }
    }
  }
</script>

<style lang="scss">

</style>