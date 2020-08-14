<template>
  <b-card bg-variant="dark" text-variant="white" class="my-2 mx-2 member-card"> 
    <div class="member-name">{{name}}</div>
    <b-card-img-lazy :src="getSprite(slug)" :alt="slug" bottom 
      blank-color='#343a40' blank-width="68px" blank-height="56px">
    </b-card-img-lazy>
    <p class="member-number">{{id}}</p>
  </b-card>
</template>

<script>
  export default {
    name: 'MemberCard',
    props: [
      'id', 'dex_id', 'sprite_id', 'name', 'dexno', 'slug', 
      'nickname', 'gender', 'level', 'slot', 'shiny'
    ],
    methods: {
      getSprite(slug){
        return `https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/${slug}.png`
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
</style>