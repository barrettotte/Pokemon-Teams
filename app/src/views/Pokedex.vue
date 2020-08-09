<template>
  <app-page-header :title="'Pokedex'"
    :desc="'Browse the Pokedex for future team inspiration!'">
  </app-page-header>
</template>

<script>
  import PageHeader from '@/components/PageHeader.vue';
  
  export default {
    components: {
      'app-page-header': PageHeader
    }
  }
</script>

<style lang="scss">

</style>