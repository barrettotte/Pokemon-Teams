<template>
  <b-container class="mb-4">
    <b-card-group deck class="team-container">
      <b-card bg-variant="dark" text-variant="white" class="member-body"> 
        <div class="member-card">
          <div class="dex-name">
            <a href="" target="_blank">{{label}}</a>
          </div>
          <p class="member-number">{{id}}</p>
        </div>
      </b-card>
      <b-card bg-variant="dark" text-variant="white" class="member-body"> 
        <div class="member-card">
          <div class="dex-name">
            <a href="" target="_blank">{{label}}</a>
          </div>
          <p class="member-number">{{id}}</p>
        </div>
      </b-card>
      <b-card bg-variant="dark" text-variant="white" class="member-body"> 
        <div class="member-card">
          <div class="dex-name">
            <a href="" target="_blank">{{label}}</a>
          </div>
          <p class="member-number">{{id}}</p>
        </div>
      </b-card>
      <b-card bg-variant="dark" text-variant="white" class="member-body"> 
        <div class="member-card">
          <div class="dex-name">
            <a href="" target="_blank">{{label}}</a>
          </div>
          <p class="member-number">{{id}}</p>
        </div>
      </b-card>
      <b-card bg-variant="dark" text-variant="white" class="member-body"> 
        <div class="member-card">
          <div class="dex-name">
            <a href="" target="_blank">{{label}}</a>
          </div>
          <p class="member-number">{{id}}</p>
        </div>
      </b-card>
      <b-card bg-variant="dark" text-variant="white" class="member-body"> 
        <div class="member-card">
          <div class="dex-name">
            <a href="" target="_blank">{{label}}</a>
          </div>
          <p class="member-number">{{id}}</p>
        </div>
      </b-card>
    </b-card-group>
  </b-container>
</template>

<script>
  export default {
    name: 'TeamCardGroup',
    props: ['label', 'id']
  }
</script>

<style lang="scss" scoped>
  .team-container{
    height: 100%;
    border: 4px solid black;
    padding: 25px;
  }
  .member-body{
    border: 4px solid black;
    width: 10rem;
    height: 10rem;
  }
  .member-name a{
    font-size: 14px;
    color: white;
    font-weight: bold;
  }
  .member-number{
    text-align: right;
    color: #b6b4b4;
    font-size: 9px;
    font-weight: bold;
  }
</style>