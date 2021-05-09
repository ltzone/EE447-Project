<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
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
          { text: 'Task_Name', value: 'task_name' },
          { text: 'State', value: 'status' },
          { text: 'Worker', value: 'worker' },
          { text: 'Finished_Time ', value: 'date_done' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1%',
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1%',
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7%',
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8%',
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16%',
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0%',
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2%',
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45%',
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22%',
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6%',
          },
        ],
        running_tasks: [
          {
            id: 1,
            name: 'Map Reduce',
            state: 'Tony Zhou',
            when: 'Map Reducing',
            worker: '70min',
          },
        ],
      }
    },

    mounted () {
      server.get('/get').then(
        res => {
          var ta = []
          for (var i = 0; i < res.data.length; i++) {
            var ob = { id: 'eed', task_name: 'e', status: 'dd', worker: 'dd', date_done: '2020' }

            if (res.data[i].status) {
              ob.id = res.data[i].task_id
              ob.task_name = res.data[i].task_name
              ob.status = res.data[i].status
              ob.worker = res.data[i].worker
              ob.date_done = res.data[i].date_done
              ta.push(ob)
            }
          }

          this.desserts = ta
        },
        error => {
          this.desserts = error
        })
    },
  }
</script>
