<template>
  <v-container
    id="regular-tables"
    fluid
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="On Running Tasks"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th
              class="primary--text"
              scope="col"
            >
              ID
            </th>
            <th
              class="primary--text"
              scope="col"
            >
              Name
            </th>
            <th
              class="primary--text"
              scope="col"
            >
              State
            </th>
            <th
              class="primary--text"
              scope="col"
            >
              When
            </th>
            <th
              class="primary--text text--right"
              scope="col"
            >
              Worker
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="task in running_tasks"
            :key="task.id"
          >
            <td>{{ task.id }}</td>
            <td>{{ task.name }}</td>
            <td>{{ task.state }}</td>
            <td>{{ task.when }}</td>
            <td>{{ task.worker }}</td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
    <div class="py-3" />
    <base-material-card
      color="success"
      dark
      icon="mdi-clipboard-plus"
      title="Other Tasks"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th
              class="primary--text"
              scope="col"
            >
              ID
            </th>
            <th
              class="primary--text"
              scope="col"
            >
              Name
            </th>
            <th
              class="primary--text"
              scope="col"
            >
              State
            </th>
            <th
              class="primary--text"
              scope="col"
            >
              When
            </th>
            <th
              class="primary--text text--right"
              scope="col"
            >
              Worker
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="task in other_tasks"
            :key="task.id"
          >
            <td>{{ task.id }}</td>
            <td>{{ task.name }}</td>
            <td>{{ task.state }}</td>
            <td>{{ task.when }}</td>
            <td>{{ task.worker }}</td>
          </tr>
        </tbody>
      </v-simple-table>
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
        running_tasks: [
          {
            id: 1,
            name: 'Map Reduce',
            state: 'Tony Zhou',
            when: 'Map Reducing',
            worker: '70min',
          },
        ],
        other_tasks: [
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
          for (var i = 0; i < res.data.length; i++) {
            if (res.data[i].status === 'SUCCESS') {
              this.other_tasks.push(res.data[i])
            }
          }

          this.running_tasks = [
            {
              id: 122,
              name: 'Map Reduce',
              state: 'Success',
              when: '2021-05-09',
              worker: 'aaa',
            },
          ]
        },
        error => {
          this.running_tasks = error
        })
    },
  }
</script>
