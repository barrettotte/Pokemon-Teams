<template>
  <div>
    <b-jumbotron>
      <template v-slot:header>Pokemon Teams</template>
      <template v-slot:lead>An app to track Pokemon teams used across various games/playthroughs.</template>
      <hr class="my-4">
      <p>Add new teams, edit your team members, or simply browse the Pokedex for team inspiration.</p>
      <b-button class="mx-4 mt-3" variant="primary" href="#">Manage Teams</b-button>
      <b-button class="mx-4 mt-3" variant="success" href="#">Browse Pokedex</b-button>
    </b-jumbotron>
    <b-container>
      <b-row align-v="center">
        <b-col class="md-12">
          <p>TODO: random team display here</p>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    components: {
      //'app-member': MemberCard
    }
  }
</script>

<style lang="scss">

</style>