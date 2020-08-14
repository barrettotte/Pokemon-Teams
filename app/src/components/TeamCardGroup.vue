<template>
  <b-container class="mb-4" style="padding-bottom: 25px">
    <b-row class="team-container justify-content-center">
      <div class="team-label">{{label}}</div>
      <b-card-group deck>
        <!-- TODO: Edit and delete buttons (probably centered at bottom) -->
        <app-member v-for="member in sortedMembers()" :key="member.member_id" :id="member.member_id"
          :dex_id="member.dex_id" :sprite_id="member.sprite_id" :name="member.name" :dexno="member.dexno"
          :slug="member.slug" :nickname="member.nickname" :gender="member.gender" :level="member.level" 
          :slot="member.slot" :shiny="member.shiny">
        </app-member>
      </b-card-group>
      <div class="mt-4">
        <b-button variant="primary" class="team-btn mx-4">Edit</b-button>
        <b-button variant="danger" class="team-btn mx-4">Delete</b-button>
      </div>
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
      sortedMembers(){
        return this.members.sort((a, b) => a.slot - b.slot);
      }
    }
  }
</script>

<style lang="scss" scoped>
  .team-container{
    height: 100%;
    border: 4px solid black;
    background-color: rgb(167, 167, 167);
    padding: 25px;

    .team-label{
      font-weight: bold;
      font-size: 22px;
      padding-bottom: 10px;
    }

    .team-btn{
      border: 4px solid black;
    }
  }
</style>