<template>
  <v-container
    id="regular-tables"
    fluid
  >
    <base-material-card
      icon="mdi-account"
      title=""
      class="px-5 py-3"
    >
      <v-data-table
        :headers="headers"
        :items="success"
        :items-per-page="5"
        class="elevation-1"
      />
    </base-material-card>
  </v-container>
</template>

<script>
  import server from '@/server.js'
  export default {
    name: 'Workers',
    components: {},
    data () {
      return {
        headers: [
          {
            text: 'Worker_Name',
            align: 'start',
            sortable: false,
            value: 'hostname',
          },
          { text: 'Last_Heartbeat', value: 'last_heartbeat' },
          { text: 'Last_Update', value: 'last_update' },
        ],
        success: [],
        running: [],
        others: [],
      }
    },
    mounted () {
      server.get('/workers').then(
        res => {
          var task = []
          for (var i = 0; i < res.data.length; i++) {
            var ob = { hostname: '', last_heartbeat: '', last_update: '' }
            ob.hostname = res.data[i].hostname
            ob.last_heartbeat = res.data[i].last_heartbeat
            ob.last_update = res.data[i].last_update
            task.push(ob)
          }
          this.success = task
        },
        error => {
          this.success = error
        })
    },
  }
</script>
