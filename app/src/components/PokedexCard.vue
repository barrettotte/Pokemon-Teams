<template>
  <div>
    <b-col>
      <b-card :title="name" :img-alt="slug" :img-src="getSprite(slug)"
        img-top style="min-width:12rem" class="mb-2">
        <b-card-text>{{dexno}}</b-card-text>
        <b-button variant="primary" :href="getPokemonDb(slug)" 
          target="_blank" v-b-tooltip.hover title="View PokemonDB Entry">
          More Info
        </b-button>
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

</style>