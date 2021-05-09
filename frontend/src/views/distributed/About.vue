<template>
  <div class="about">
    <h1>This is about page, {{ data }}</h1>
  </div>
</template>

<script>
  import server from '@/server.js'

  export default {
    name: 'About',
    components: {},
    data () {
      return {
        data: 'init',
      }
    },

    mounted () {
      server.get('/', {
        param: 'param1',
      }).then(
        res => {
          this.data = res.data
        },
        error => {
          this.data = error
        })
    },
  }
</script>
