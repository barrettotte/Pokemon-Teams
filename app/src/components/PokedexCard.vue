<template>
  <b-card bg-variant="dark" text-variant="white" class="my-2 mx-2 dex-card">
    <div class="dex-body">
      <div class="dex-name">
        <a :href="getPokemonDb()" target="_blank">{{name}}</a>
      </div>
      <a :href="getPokemonDb()" target="_blank">
        <b-card-img-lazy :src="getSprite()" :alt="slug" bottom 
          blank-color='#343a40' blank-width="68px" blank-height="56px">
        </b-card-img-lazy>
      </a>
      <p class="dex-number">{{dexno}}</p>
    </div>
  </b-card>
</template>

<script>
  export default {
    name: 'PokedexCard',
    props: ['name', 'dexno', 'slug'],
    methods: {
      getSprite(){
        return `https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/${this.slug}.png`;
      },
      getPokemonDb(){
        return `https://pokemondb.net/pokedex/${this.slug}`;
      }
    }
  }
</script>

<style lang="scss" scoped>
  .dex-card{
    border: 4px solid black;
    width: 10rem;
    height: 10rem;
  }
  .dex-card:hover{
    transform: rotate(3deg);
    border: 4px solid rgb(155, 153, 153);
  }

  .dex-body{
    height: 100%;
  }

  .dex-name a{
    font-size: 14px;
    color: white;
    font-weight: bold;
  }
  
  .dex-number{
    text-align: right;
    color: #b6b4b4;
    font-size: 9px;
    font-weight: bold;
  }
</style>