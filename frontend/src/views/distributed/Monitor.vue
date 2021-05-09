<template>
  <v-container>
    <h1>This is monitor page</h1>

    <v-textarea
      name="input-7-1"
      label="Default style"
      :value="running_tasks[0].name"
      hint="Hint text"
    ></v-textarea>
  </v-container>
</template>

<script>
  export default {
    name: 'Application',
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
