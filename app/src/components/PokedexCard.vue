<template>
  <div class="dex-card">
    <b-col>
      <b-card bg-variant="dark" text-variant="white" class="mb-4 dex-body"> 
        <div class="dex-name">
          <a :href="getPokemonDb(slug)" target="_blank">{{name}}</a>
        </div>
        <a :href="getPokemonDb(slug)" target="_blank">
          <b-card-img-lazy :src="getSprite(slug)" :alt="slug" bottom 
            blank-color='#343a40' blank-width="68px" blank-height="56px">
          </b-card-img-lazy>
        </a>
        <p class="dex-number">{{dexno}}</p>
      </b-card>
    </b-col>
  </div>
</template>

<script>
  export default {
    name: 'PokedexCard',
    props: ['name', 'dexno', 'slug'],
    methods: {
      getSprite(slug){
        return `https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/${slug}.png`
      },
      getPokemonDb(slug){
        return `https://pokemondb.net/pokedex/${slug}`
      }
    }
  }
</script>

<style lang="scss" scoped>
  .dex-card{
    height: 100%;
  }
  .dex-body{
    border: 4px solid black;
    width: 10rem;
    height: 10rem;
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