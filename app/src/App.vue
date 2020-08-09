<template>
  <div id="app">
    <div class="page" v-if="showSpinner">
      <b-spinner class="spinner" variant="primary" key="primary"></b-spinner>
    </div>
    <div id="nav">
      <app-navbar></app-navbar>
    </div>
    <router-view/>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex';
  import Navbar from '@/components/Navbar.vue';
  
  export default {
    name: 'App',
    components: {
      'app-navbar': Navbar
    },
    computed: {
      ...mapGetters(['showSpinner'])
    }
  }
</script>

<style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .page{
    position: absolute;
    background: rgba(0, 0, 0, 0.3);
    z-index: 25;
    width: 100%;
    height: 100%;
  }

  .spinner{
    position: relative;
    top: 50%;
  }
</style>
