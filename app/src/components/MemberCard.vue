<template>
  <b-card bg-variant="dark" text-variant="white" class="my-2 mx-2 member-card"> 
    <div class="member-name">{{(nickname && nickname.length > 0) ? nickname : name}}</div>
    <b-card-img-lazy v-if="slug" :src="getSprite()" :alt="slug" bottom 
      blank-color='#343a40' blank-width="68px" blank-height="56px">
    </b-card-img-lazy>
    <div v-if="id > 0">
      <div class="member-gender float-left" v-html="getGenderSymbol()"></div>
      <div class="member-number">Lv {{level}}</div>
    </div>
  </b-card>
</template>

<script>
  export default {
    name: 'MemberCard',
    props: [
      'id', 'dex_id', 'sprite_id', 'name', 'dexno', 'slug', 
      'nickname', 'gender', 'level', 'slot_idx', 'shiny'
    ],
    methods: {
      getSprite(){
        const prefix = 'https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8';
        const slugType = (this.shiny) ? 'shiny' : 'regular';
        return `${prefix}/${slugType}/${this.slug}.png`
      },
      getGenderSymbol(){
        if(this.gender.toUpperCase() === 'M'){
          return '&#9794;';
        } else if(this.gender.toUpperCase() === 'F'){
          return '&#9792;';
        }
        return null;
      }
    },
    computed: {
      modalId(){
        return `modal-${this.id}`;
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
</style>