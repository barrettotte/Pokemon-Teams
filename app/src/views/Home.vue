<template>
  <div>
    <b-jumbotron>
      <template v-slot:header>Pokemon Teams</template>
      <template v-slot:lead>An app to track Pokemon teams used across various games/playthroughs.</template>
      <hr class="my-3">
      <div class="home-buttons">
        <p class="mb-4">Make new teams, edit your team members, or simply browse the Pokedex for team inspiration.</p>
        <b-button class="mx-4 home-btn" variant="primary" href="/teams">Manage Teams</b-button>
        <b-button class="mx-4 home-btn" variant="success" href="/pokedex">Browse Pokedex</b-button>
      </div>
      <app-example-team></app-example-team>
    </b-jumbotron>
  </div>
</template>

<script>
  import ExampleTeam from '@/components/ExampleTeam.vue';

  export default {
    name: 'Home',
    components: {
      'app-example-team': ExampleTeam
    }
  }
</script>

<style lang="scss">
  .home-buttons{
    padding-bottom: 40px;

    .home-btn{
      border: 4px solid black;
    }

    .home-btn:hover{
      border: 4px solid black;
      transform: rotate(3deg);
    }
  }
</style>