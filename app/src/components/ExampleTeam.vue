<template>
  <b-container class="team-container">
    <b-row class="justify-content-center">
      <div class="team-label">
        My SwSh Team
      </div>
    </b-row>
    <b-row class="justify-content-center">
      <b-card-group deck>
        <app-member v-for="member in exampleTeam" :key="member.member_id" 
          :id="member.member_id" :dex_id="0" :sprite_id="0" :gender="member.gender" 
          :level="member.level" :slot_idx="0" :nickname="''" :shiny="member.shiny"
          :slug="member.slug" :name="member.name" :dexno="0">
        </app-member>
      </b-card-group>
    </b-row>
  </b-container>  
</template>

<script>
  import MemberCard from '@/components/MemberCard.vue';

  export default {
    name: 'ExampleTeam',
    components: {
      'app-member': MemberCard
    },
    data(){
      return {
        exampleTeam: [
          {
            'member_id': 2,
            'name': 'Lanturn',
            'slug': 'lanturn',
            'gender': 'F',
            'level': 88,
            'shiny': false
          },
          {
            'member_id': 3,
            'name': 'Appletun',
            'slug': 'appletun',
            'gender': 'M',
            'level': 89,
            'shiny': false
          },
          {
            'member_id': 1,
            'name': 'Centiskorch',
            'slug': 'centiskorch',
            'gender': 'M',
            'level': 90,
            'shiny': false
          },
          {
            'member_id': 4,
            'name': 'Dragapult',
            'slug': 'dragapult',
            'gender': 'M',
            'level': 84,
            'shiny': false
          },
          {
            'member_id': 5,
            'name': 'Hatterene',
            'slug': 'hatterene',
            'gender': 'F',
            'level': 77,
            'shiny': false
          },
          {
            'member_id': 6,
            'name': 'Froslass',
            'slug': 'froslass',
            'gender': 'F',
            'level': 79,
            'shiny': false
          }
        ]
      }
    }
  }
</script>

<style lang="scss" scoped>
  .team-container{
    border: 4px solid black;
    background-color: rgb(167, 167, 167);
    padding: 25px 25px 50px 25px;

    .team-label{
      font-weight: bold;
      font-size: 22px;
      padding-bottom: 10px;
    }
  }
</style>