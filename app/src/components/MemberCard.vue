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
      <b-button-group v-if="isActive" class="edit-btn-group">
        <b-button class="btn-edit" block> <!-- @click="$bvModal.show(modalId)" -->
          <b-icon icon="pencil" class="icon-edit float-left mx-2" scale="0.80"></b-icon>
        </b-button>
        <b-button class="btn-delete" block @click="deleteMember()">
          <b-icon icon="trash" class="icon-delete float-right mx-2" scale="0.80"></b-icon>
        </b-button>
      </b-button-group>
      <div v-else>
        <div class="member-gender float-left" v-html="getGenderSymbol()"></div>
        <div class="member-number float-right">Lv {{member.level}}</div>
      </div>
    </div>
    <div v-else>
      <div v-if="isActive">
        <b-button class="btn-new" block @click="$bvModal.show(modalId)">
          <b-icon icon="plus-circle" class="icon-new"></b-icon>
        </b-button>
      </div>
    </div>
    <!-- separate component for modal ? -->
    <b-modal :id="modalId" :hide-footer="true" v-model="showModal" :title="(isFull() ? 'Edit' : 'Create') + ' Member'">
      <b-container class="member-modal">
        <b-row class="justify-content-center">
          <b-form @submit.stop.prevent="handleSubmit">
            <!-- A Pokemon lookup would be nice ... -->
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
      }
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
          dexno:    this.member['dexno'] || 1,
          level:    this.member['level'] || 50,
          gender:   this.member['gender'] || ' ',
          shiny:    this.member['shiny'] || false,
          nickname: this.member['nickname'] || null
        }
      }
    },
    methods: {
      getSprite(){
        const prefix = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8';
        const slugType = (this.member.shiny) ? 'shiny' : 'regular';
        return `${prefix}/${slugType}/${this.member.slug}.png`;
      },
      getGenderSymbol(){
        if(!this.member.gender || this.member.gender === ' '){
          return null;
        } else if(this.member.gender.toUpperCase() === 'M'){
          return '&#9794;';
        } else if(this.member.gender.toUpperCase() === 'F'){
          return '&#9792;';
        }
        console.error('Gender in unexpected state ' + this.member.gender);
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
      async createMember(){
        const dexEntry = await this.$store.dispatch('fetchPokedexEntry', {dexno: this.form['dexno']});
        const sprite = await this.$store.dispatch('fetchSprite', {dexId: dexEntry['dex_id'], form: '$'});

        const newMember = {
          'dex_id': dexEntry['dex_id'],
          'sprite_id': sprite['sprite_id'],
          'gender': this.form['gender'],
          'level': this.form['level'],
          'slot': this.member['slot'],
          'nickname': this.form['nickname'],
          'shiny': this.form['shiny'] === 'Y',
          'slug': dexEntry['slug'],
          'name': dexEntry['name'],
          'dexno': this.form['dexno']
        };
        const newId = await this.$store.dispatch('addMember', {teamId: this.teamId, memberData: newMember});
        this.member['member_id'] = newId;
        this.member['dex_id'] = newMember['dex_id'];
        this.member['sprite_id'] = newMember['sprite_id'];
        this.member['gender'] = newMember['gender'];
        this.member['level'] = newMember['level'];
        this.member['slot'] = newMember['slot'];
        this.member['nickname'] = newMember['nickname'];
        this.member['shiny'] = newMember['shiny'];
        this.member['slug'] = newMember['slug'];
        this.member['name'] = newMember['name'];
        this.member['dexno'] = newMember['dexno'];
        this.leaveForm();
      },
      async deleteMember(){
        const payload = {teamId: this.teamId, memberId: this.member['member_id'], slotIdx: this.member['slot']};
        await this.$store.dispatch('deleteMember', payload);
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
    color: white;
    font-size: 14px;
    font-weight: bold;
  }

  .member-number{
    color: #b6b4b4;
    font-size: 9px;
    font-weight: bold;
  }

  .member-gender{
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

  .member-info{
    color: white;
  }

  .member-info:hover{
    color: cyan;
  }

  .btn-new{
    background-color: rgba(0, 0, 0, 0);
    border: none;
    margin-top: 25%;

    .icon-new{
      color: #5e5d5d;
      height: 50px;
      width: 50px;
    }
    .icon-new:hover{
      color: white;
    }
  }

  .edit-btn-group{
    height: 20px;
    margin-top: -20px;

    .btn-edit, .btn-delete{
      background-color: rgba(0, 0, 0, 0);
      border: none;
    }

    .icon-edit{
      color: #c2c1c1;
    } 
    
    .icon-delete{
      color: #c2c1c1;
      margin-top: -8px;
    }

    .icon-edit:hover{
      color: green;
      cursor: pointer;
    }

    .icon-delete:hover{
      color: red;
      cursor: pointer;
    }
  }
</style>