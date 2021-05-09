<template>
  <div class="stat">
    <h1>This is stat page, {{ data }}</h1>
  </div>
</template>

<script>
  import server from '@/server.js'

  export default {
    name: 'Stat',
    components: {},
    data () {
      return {
        data: 'init',
      }
    },

    mounted () {
      server.get('/')
    },
  }
</script>
