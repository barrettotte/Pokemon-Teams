<template>
  <div>
    <app-page-header :title="'About'"
      :desc="'General information about this application'">
    </app-page-header>
    <b-container class="text-left">
      <h3 class="section-header">Purpose:</h3>
      <p>
        I always wanted to learn how to use VueJS so I slapped together a project idea to practice with.
        I'm currently going through a huge Pokemon binge, so this was an idea I could stay interested in.
        <br><br>
        When I start a new playthrough of a Pokemon game, I never use the same Pokemon twice.
        This forces me to use different teams that I would have never used.
        Often times I forget what I have and haven't used, so an application like this would be pretty useful.
      </p>
      <h3 class="section-header">Project Details</h3>
      <p>
        The main focus of this side project was to mess with Vue, so the backend is kind of garbage.
        Additionally, this is for a single user and only ran locally. 
        I was feeling really lazy and didn't want to go through authentication, deploying, containerizing, etc.
        <br><br>
        For this little side project, I wanted to accomplish the following:
        <ul>
          <li>Introduction to VueJS</li>
          <li>Routing with vue-router</li>
          <li>CRUD functionality on a model</li>
          <li>External API usage with vue-resource</li>
          <li>State management with vuex</li>
          <li>Simple Python backend (Flask) and local Postgres DB (on Pi)</li>
        </ul>
        Overall I think VueJS is pretty neat. 
        However, I still think Angular is going to be my main frontend for other projects.

        <br><br>
        The repository for this little application is located at 
        <a href="https://github.com/barrettotte/Pokemon-Teams">
          https://github.com/barrettotte/Pokemon-Teams
        </a>
      </p>
      <h3 class="section-header">Credit</h3>
      <ul>
        <li>The sprite images are © Nintendo/Creatures Inc./GAME FREAK Inc.</li>
        <li>
          PokeSprite Project - <a href="https://github.com/msikma/pokesprite">Github Repository</a> (MIT)
        </li>
        <li>
          GitHub Corners - <a href="https://github.com/tholman/github-corners">Github Repository</a> (MIT)
        </li>
      </ul>
    </b-container>
  </div>
</template>

<script>
  import PageHeader from '@/components/PageHeader.vue';

  export default {
    name: 'About',
    components: {
      'app-page-header': PageHeader
    }
  }
</script>

<style lang="scss">
  .section-header{
    padding-top: 10px;
    font-weight: bold;
    text-decoration: underline;
  }
</style>