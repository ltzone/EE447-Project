<template>
  <v-container>
    <h1>This is monitor page</h1>

    <v-textarea
      name="input-7-1"
      label="Default style"
      :value="running_tasks[0].name"
      hint="Hint text"
    />

    <v-col
      cols="12"
      md="6"
    >
      <v-textarea
        solo
        name="input-7-4"
        label="Solo t"
      />
    </v-col>

    <input
      v-model="message"
      placeholder="edit me"
    >
    <p>Message is: {{ message }}</p>
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
