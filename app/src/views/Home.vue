<template>
  <b-container>
    <b-row align-v="center">
      <app-member></app-member>
      <app-member></app-member>
      <app-member></app-member>
      <app-member></app-member>
    </b-row>
  </b-container>
</template>

<script>
  import MemberCard from '@/components/MemberCard.vue'

  export default {
    name: 'Home',
    components: {
      'app-member': MemberCard
    },
    mounted(){
      this.fetchData();
    },
    methods: {
      async fetchData(){
        const res = await fetch('test.json');
        const val = await res.json();
        console.log(val);
      }
    }
  }
</script>
