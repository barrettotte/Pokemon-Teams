<template>
  <b-card bg-variant="dark" text-variant="white" class="my-2 mx-2 member-card"> 
    <div class="member-name">
      {{(member.nickname && member.nickname.length > 0) ? member.nickname : member.name}}
      <a v-if="isFull()" :href="getPokemonDb()" class="member-info float-right">
        <b-icon icon="info-circle"></b-icon>
      </a>
    </div>
    <div v-if="isFull()">
      <b-card-img-lazy :src="getSprite()" :alt="member.slug" bottom 
        blank-color='#343a40' blank-width="68px" blank-height="56px">
      </b-card-img-lazy>
      <div class="member-gender float-left" v-html="getGenderSymbol()"></div>
      <div class="member-number">Lv {{member.level}}</div>
    </div>
    <div v-else>
      <div v-if="isActive">
        <b-button class="btn-new-member" block @click="$bvModal.show(modalId)">
          <b-icon icon="plus-circle" class="icon-new-member"></b-icon>
        </b-button>
      </div>
    </div>
    <b-modal :id="modalId" :hide-footer="true" v-model="showModal" :title="(isFull() ? 'Edit' : 'Create') + ' Member'">
      <b-container class="member-modal">
        <b-row class="justify-content-center">
          <b-form @submit.stop.prevent="handleSubmit">
            <b-form-group label="Pokedex Number:">
              <b-form-input v-model="form.dexno" type="number" required min="1" :max="getPokedexSize()"></b-form-input>
            </b-form-group>
            <b-form-group label="Level:">
              <b-form-input v-model="form.level" type="number" required min="1" max="100"></b-form-input>
            </b-form-group>
            <b-form-group label="Gender:">
              <b-form-select v-model="form.gender" required :options="genderOptions"></b-form-select>
            </b-form-group>
            <b-form-group label="Shiny:">
              <b-form-checkbox v-model="form.shiny" value="Y" unchecked-value="N"></b-form-checkbox>
            </b-form-group>
            <b-form-group label="Nickname:">
              <b-form-input v-model="form.nickname" type="text"></b-form-input>
            </b-form-group>
          </b-form>
        </b-row>
        <b-row class="justify-content-center modal-buttons">
          <b-button variant="danger" class="btn-modal mx-4" @click="leaveForm()">Cancel</b-button>
          <b-button variant="primary" class="btn-modal mx-4" @click="createMember()">Create</b-button>
        </b-row>
      </b-container>
    </b-modal>
  </b-card>
</template>

<script>
  export default {
    name: 'MemberCard',
    props: [
      'member', 'teamId', 'isActive'
    ],
    computed: {
      modalId(){
        return `member-modal-${this.member.member_id}-${this.teamId}`;
      },
    },
    data(){
      return{
        showModal: false,
        genderOptions: [
          { value: ' ', text: 'None'   },
          { value: 'M', text: 'Male'   },
          { value: 'F', text: 'Female' }
        ],
        form: {
          dexno:    this.member['dexno'],
          level:    this.member['level'],
          gender:   this.member['gender'],
          shiny:    this.member['shiny'],
          nickname: this.member['nickname']
        }
      }
    },
    methods: {
      getSprite(){
        const prefix = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8';
        const slugType = (this.member.shiny) ? 'shiny' : 'regular';
        return `${prefix}/${slugType}/${this.member.slug}.png`
      },
      getGenderSymbol(){
        if(this.member.gender.toUpperCase() === 'M'){
          return '&#9794;';
        } else if(this.member.gender.toUpperCase() === 'F'){
          return '&#9792;';
        }
        return null;
      },
      getPokedexSize(){
        return this.$store.state.pokedexEntries.length;
      },
      getPokemonDb(){
        return `https://pokemondb.net/pokedex/${this.member.slug}`;
      },
      isFull(){
        return this.member.member_id > 0;
      },
      createMember(){
        console.log('creating!');
        const newMember = {
          // TODO:
        };
        console.log(newMember);
        this.leaveForm();
      },
      leaveForm(){
        this.showModal = false;
      }
    }
  }
</script>

<style lang="scss" scoped>
  .member-card{
    border: 4px solid black;
    width: 10rem;
    height: 10rem;
  }

  .member-name {
    font-size: 14px;
    color: white;
    font-weight: bold;
  }

  .member-number{
    text-align: right;
    color: #b6b4b4;
    font-size: 9px;
    font-weight: bold;
  }

  .member-gender{
    text-align: left;
    color: #b6b4b4;
    font-size: 20px;
    font-weight: bold;
    margin-top: -10px;
  }

  .member-modal{
    padding-bottom: 25px;

    .modal-buttons{
      padding-top: 25px;

      .btn-modal{
        border: 4px solid black;
      }

      .btn-modal:hover{
        border: 4px solid black;
        transform: rotate(3deg);
      }
    }
  }

  .btn-new-member{
    background-color: rgba(0, 0, 0, 0);
    border: none;
    margin-top: 25%;

    .icon-new-member{
      color: #5e5d5d;
      height: 50px;
      width: 50px;
    }
    .icon-new-member:hover{
      color: white;
    }
  }

  .member-info{
    color: white;
  }
</style>