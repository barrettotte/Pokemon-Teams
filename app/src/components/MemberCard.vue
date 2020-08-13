<template>
  <div>
    <b-col>
      <b-card :title="name" img-alt="member" img-top tag="article" style="min-width:10rem" class="mb-2"
        img-src="https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/regular/charizard.png"
      >
        <b-card-text>This is text</b-card-text>
        <b-button variant="primary" v-b-modal="modalId" v-b-tooltip.hover title="Launch modal">Info</b-button>
        <b-modal :id="modalId" title="I am a modal">
          <p class="my-4">Hello from modal</p>
        </b-modal>
      </b-card>
    </b-col>
  </div>
</template>

<script>
  export default {
    name: 'MemberCard',
    props: ['name', 'id'],
    computed: {
      modalId(){
        return `modal-${this.id}`;
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>