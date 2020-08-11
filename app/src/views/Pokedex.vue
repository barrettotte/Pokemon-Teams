<template>
  <div>
    <app-page-header :title="'Pokedex'"
      :desc="'Browse the Pokedex for future team inspiration'">
    </app-page-header>
    <b-container>
      <b-row class="justify-content-center">
        <app-pokedex-card v-for="entry in pokedexEntries" :key="entry.id" 
          :name="entry.name" :dexno="entry.dexno" :slug="entry.slug">
        </app-pokedex-card>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import PageHeader from '@/components/PageHeader.vue';
  import PokedexCard from '@/components/PokedexCard.vue';
  import {mapGetters} from 'vuex';
  
  export default {
    name: 'Pokedex',
    components: {
      'app-page-header': PageHeader,
      'app-pokedex-card': PokedexCard
    },
    computed: {
      ...mapGetters(['pokedexEntries'])
    },
    mounted(){
      this.fillPokedex();
    },
    methods: {
      async fillPokedex(){
        await this.$store.dispatch('fetchPokedexEntries');
      }
    }
  }
</script>

<style lang="scss">

</style>