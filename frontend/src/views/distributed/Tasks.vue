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
              User
            </th>
            <th
              class="primary--text"
              scope="col"
            >
              Description
            </th>
            <th
              class="primary--text text--right"
              scope="col"
            >
              ETA
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
            <td>{{ task.user }}</td>
            <td>{{ task.description }}</td>
            <td>{{ task.eta }}</td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>

<script>
  export default {
    name: 'Tasks',
    components: {},
    data () {
      return {
        running_tasks: [
          {
            id: 1,
            name: 'Map Reduce',
            user: 'Tony Zhou',
            description: 'Map Reducing',
            eta: '70min',
          },
        ],
      }
    },
  }
</script>
