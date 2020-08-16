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
          :member="member" :team_id="0" :isActive="false">
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
            'dex_id': 0,
            'sprite_id': 0,
            'gender': 'F',
            'level': 88,
            'slot_idx': 0,
            'nickname': null,
            'shiny': false,
            'slug': 'lanturn',
            'name': 'Lanturn',
            'dexno': 0
          },
          {
            'member_id': 3,
            'dex_id': 0,
            'sprite_id': 0,
            'gender': 'M',
            'level': 89,
            'slot_idx': 0,
            'nickname': null,
            'shiny': false,
            'slug': 'appletun',
            'name': 'Appletun',
            'dexno': 0
          },
          {
            'member_id': 1,
            'dex_id': 0,
            'sprite_id': 0,
            'gender': 'M',
            'level': 90,
            'slot_idx': 0,
            'nickname': null,
            'shiny': false,
            'slug': 'centiskorch',
            'name': 'Centiskorch',
            'dexno': 0
          },
          {
            'member_id': 4,
            'dex_id': 0,
            'sprite_id': 0,
            'gender': 'M',
            'level': 84,
            'slot_idx': 0,
            'nickname': null,
            'shiny': false,
            'slug': 'dragapult',
            'name': 'Dragapult',
            'dexno': 0
          },
          {
            'member_id': 5,
            'dex_id': 0,
            'sprite_id': 0,
            'gender': 'F',
            'level': 77,
            'slot_idx': 0,
            'nickname': null,
            'shiny': false,
            'slug': 'hatterene',
            'name': 'Hatterene',
            'dexno': 0
          },
          {
            'member_id': 6,
            'dex_id': 0,
            'sprite_id': 0,
            'gender': 'F',
            'level': 79,
            'slot_idx': 0,
            'nickname': null,
            'shiny': false,
            'slug': 'froslass',
            'name': 'Froslass',
            'dexno': 0
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