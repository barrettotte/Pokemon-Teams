<template>
  <b-container class="mb-5 team-container">
    <b-row class="justify-content-center">
      <div class="team-label">
        {{label}} | {{id}}
      </div>
    </b-row>
    <b-row class="justify-content-center">
      <b-card-group deck v-if="members && members.length > 0">
        <app-member v-for="member in members" :key="member.member_id" 
          :id="member.member_id" :dex_id="member.dex_id" :sprite_id="member.sprite_id" :gender="member.gender" 
          :level="member.level" :slot_idx="member.slot" :nickname="member.nickname" :shiny="member.shiny"
          :slug="member.slug" :name="member.name" :dexno="member.dexno">
        </app-member>
      </b-card-group>
    </b-row>
    <b-row class="mt-4 justify-content-center">
      <b-button variant="primary" class="team-btn mx-4">Edit</b-button>
      <b-button variant="danger" class="team-btn mx-4" @click="deleteTeam(id)">Delete</b-button>
    </b-row>
  </b-container>
</template>

<script>
  import MemberCard from '@/components/MemberCard.vue';

  export default {
    name: 'TeamCardGroup',
    props: ['label', 'id', 'members'],
    components: {
      'app-member': MemberCard,
    },
    methods: {
      async deleteTeam(id){
        await this.$store.dispatch('deleteTeam', {id});
      }
    }
  }
</script>

<style lang="scss" scoped>
  .team-container{
    border: 4px solid black;
    background-color: rgb(167, 167, 167);
    padding: 25px 25px 50px 25px;  //TRBL

    .team-label{
      font-weight: bold;
      font-size: 22px;
      padding-bottom: 10px;
    }

    .team-btn{
      border: 4px solid black;
    }

    .team-btn:hover{
      border: 4px solid black;
      transform: rotate(3deg);
    }
  }
</style>