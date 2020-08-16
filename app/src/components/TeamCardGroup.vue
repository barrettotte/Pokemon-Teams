<template>
  <b-container class="mb-5 team-container" 
    :style="isActive ? 'border: 4px dashed black' : 'border: 4px solid black'"
  >
    <b-row class="justify-content-center">
      <div class="team-label">
        <b-form-input v-if="isActive" v-model="form.label"></b-form-input>
        <div v-else>{{label}}</div>
      </div>
    </b-row>
    <b-row class="justify-content-center">
      <b-card-group deck class="mx-5">
        <app-member v-for="member in paddedMembers()" :key="member.member_id" 
          :member="member" :teamId="id" :isActive="isActive">
        </app-member>
      </b-card-group>
    </b-row>
    <b-row class="mt-3 justify-content-center">
      <b-button v-if="isActive" variant="success" class="team-btn mx-4" @click="saveTeam()">Save</b-button>
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
      ...mapGetters(['activeTeam']),
      isActive(){
        return this.id === this.activeTeam;
      }
    },
    data(){
      return {
        form: {
          label: this.label || 'Team'
        }
      }
    },
    methods: {
      async editTeam(){
        await this.$store.dispatch('editTeam', {teamId: this.id});
      },
      async deleteTeam(){
        await this.$store.dispatch('deleteTeam', {teamId: this.id});
      },
      async saveTeam(){
        await this.$store.dispatch('saveTeam', {teamId: this.id, label: this.form.label, members: this.members});
      },
      // fill empty slots with blank team members
      paddedMembers(){
        if(this.members.length < 6){
          const filled = this.members.map(m => m.slot);
          const minId = Math.min(...this.members.map(m => m.member_id));
          var blankId = (minId > 0) ? 0 : minId;

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