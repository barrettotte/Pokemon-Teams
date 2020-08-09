<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark" class="p-2">
      <b-navbar-brand href="/" class="mr-5">Pokemon Teams</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">Home</b-nav-item>
          <b-nav-item to="/teams">Teams</b-nav-item>
          <b-nav-item to="/pokedex">Pokedex</b-nav-item>
          <b-nav-item to="/about">About</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="team-search ml-auto">
          <b-nav-form @submit.prevent="search">
            <b-form-input size="md" class="mr-md-2" placeholder="Search for Team" v-model="searchText"></b-form-input>
            <b-button size="md" class="my-2 my-md-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <app-github-corner :width="58" :height="58" 
      :repoUrl="'https://github.com/barrettotte/Pokemon-Teams'">
    </app-github-corner>
  </div>
</template>

<script>
  import GithubCorner from '@/components/GithubCorner';

  export default {
    name: 'Navbar',
    components: {
      'app-github-corner': GithubCorner
    },
    data(){
      return {
        searchText: ''
      }
    },
    methods: {
      search(){
        this.$store.dispatch('search', {text: this.searchText});
      }
    }
  }
</script>

<style lang="scss" scoped>
  #nav {
    a {
      font-weight: bold;
      color: #e6e6e6;

      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
  
  #nav a.router-link-exact-active{
    color: rgb(143, 143, 143);
  }

  .nav-link{
     border-bottom: 2px solid rgba(0,0,0,0);
  }

  .nav-link:hover{
    border-bottom: 2px solid white;
  }

  .team-search{
    margin-right: 100px;
  }

</style>