<template>
  <v-container
    id="regular-tables"
    fluid
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Success Tasks"
      class="px-5 py-3"
    >
      <v-data-table
        :headers="headers"
        :items="success"
        :items-per-page="5"
        class="elevation-1"
      />
    </base-material-card>
    <div class="py-3" />
    <base-material-card
      color="success"
      dark
      icon="mdi-clipboard-plus"
      title="Other Tasks"
      class="px-5 py-3"
    >
      <v-data-table
        :headers="headers2"
        :items="others"
        :items-per-page="5"
        class="elevation-1"
      />
    </base-material-card>
  </v-container>
</template>

<script>
  import server from '@/server.js'
  export default {
    name: 'Tasks',
    components: {},
    data () {
      return {
        headers: [
          {
            text: 'Task_ID',
            align: 'start',
            sortable: false,
            value: 'id',
          },
          { text: 'Task_Name', value: 'name' },
          { text: 'State', value: 'state' },
          { text: 'Worker', value: 'worker' },
          { text: 'Runtime(s) ', value: 'runtime' },
        ],
        headers2: [
          {
            text: 'Task_ID',
            align: 'start',
            sortable: false,
            value: 'id',
          },
          { text: 'Task_Name', value: 'name' },
          { text: 'State', value: 'state' },
          { text: 'Worker', value: 'worker' },
        ],
        success: [],
        running: [],
        others: [],
      }
    },
    mounted () {
      server.get('/tasks').then(
        res => {
          var task1 = []
          var task2 = []
          for (var i = 0; i < res.data.length; i++) {
            var ob = { id: '', name: '', state: '', worker: '' }
            ob.id = res.data[i].task_id
            ob.name = res.data[i].name
            ob.state = res.data[i].state
            ob.worker = res.data[i].worker
            if (res.data[i].state === 'SUCCESS') {
              ob.runtime = res.data[i].runtime
              task1.push(ob)
            } else {
              task2.push(ob)
            }
          }
          this.success = task1
          this.others = task2
        },
        error => {
          this.success = error
          this.others = error
        })
    },
  }
</script>
