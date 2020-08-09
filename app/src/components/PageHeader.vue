<template>
  <div class="page-header">
    <b-container>
      <b-row>
        <b-col>
          <h3 class="ph-title">{{title}}</h3>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <p class="ph-desc">{{desc}}</p>
        </b-col>
      </b-row>
    </b-container>
    <hr class="my-3">
  </div>
</template>

<script>
  export default {
    props: ['title', 'desc'],
  }
</script>

<style lang="scss" scoped>
  .page-header{
    padding-top: 20px;
    padding-bottom: 20px;

    .ph-title{
      font-weight: bold;
    }

    .ph-desc{
      font-size: 75%;
      color: rgb(144, 142, 142);
    }
  }
</style>