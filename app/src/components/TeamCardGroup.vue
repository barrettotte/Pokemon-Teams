<template>
  <b-container class="mb-5 team-container" 
    :style="isActive() ? 'border: 4px dashed black' : 'border: 4px solid black'"
  >
    <b-row class="justify-content-center">
      <div class="team-label">
        <b-form-input v-if="isActive()" v-model="label"></b-form-input>
        <div v-else>
          {{label}} | {{id}}
        </div>
      </div>
    </b-row>
    <b-row class="justify-content-center">
      <b-card-group deck class="mx-5">
        <app-member v-for="member in paddedMembers()" :key="member.member_id" 
          :id="member.member_id" :dex_id="member.dex_id" :sprite_id="member.sprite_id" :gender="member.gender" 
          :level="member.level" :slot_idx="member.slot" :nickname="member.nickname" :shiny="member.shiny"
          :slug="member.slug" :name="member.name" :dexno="member.dexno">
        </app-member>
      </b-card-group>
    </b-row>
    <b-row class="mt-3 justify-content-center">
      <b-button v-if="isActive()" variant="success" class="team-btn mx-4" @click="saveTeam()">Save</b-button>
      <b-button v-else variant="primary" class="team-btn mx-4" @click="editTeam()">Edit</b-button>
      <b-button variant="danger" class="team-btn mx-4" @click="deleteTeam(id)">Delete</b-button>
    </b-row>
  </b-container>
</template>

<script>
  import MemberCard from '@/components/MemberCard.vue';
  import {mapGetters} from 'vuex';
  
  export default {
    name: 'TeamCardGroup',
    props: ['label', 'id', 'members'],
    components: {
      'app-member': MemberCard,
    },
    computed: {
      ...mapGetters(['activeTeam'])
    },
    methods: {
      editTeam(){
        this.$store.dispatch('editTeam', {id: this.id});
      },
      isActive(){
        return this.id === this.activeTeam;
      },
      async deleteTeam(){
        await this.$store.dispatch('deleteTeam', {id: this.id});
      },
      saveTeam(){
        console.log('SAVED!');
        // TODO: dispatch saveTeam()
      },

      // fill empty slots with blank team members
      paddedMembers(){
        if(this.members.length < 6){
          const filled = this.members.map(m => m.slot);
          var blankId = 0; // avoid duplicate keys in v-for
          for(var i = 0; i < 6; i++){
            if(!filled.includes(i)){
              this.members.push(this.createBlankMember(--blankId, i));
            }
          }
        }
        return this.members;
      },

      // create blank member for an empty slot
      createBlankMember(id, slot){
        return { 
          'member_id': id, 'dex_id': 0, 'sprite_id': 0, 'gender': null, 'level': 0, 
          'slot': slot, 'nickname': null, 'shiny': false, 'slug': null, 'name': null, 'dexno': 0
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .team-container{
    background-color: rgb(167, 167, 167);
    padding-top: 25px;
    padding-bottom: 20px;

    .team-label{
      font-weight: bold;
      font-size: 22px;
      padding-bottom: 15px;
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