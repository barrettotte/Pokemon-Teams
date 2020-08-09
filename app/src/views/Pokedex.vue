<template>
  <app-page-header :title="'Pokedex'"
    :desc="'Browse the Pokedex for future team inspiration!'">
  </app-page-header>
</template>

<script>
  import PageHeader from '@/components/PageHeader.vue';
  
  export default {
    name: 'Pokedex',
    components: {
      'app-page-header': PageHeader
    }
  }
</script>

<style lang="scss">

</style>