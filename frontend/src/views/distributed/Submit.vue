<template>
  <v-container>
    <v-row class="px-16 py-3 align-items">
      <v-row>
        <v-col>
          <v-textarea
            name="input-7-1"
            label="Default style"
            v-model="code"
            hint="Hint text"
          ></v-textarea>
        </v-col>
      </v-row>
      <v-row>
        <v-actions>
          <v-btn
            text
          >Clear</v-btn>
          <v-spacer></v-spacer>
          <v-btn
            class="white--text"
            color="deep-purple accent-4"
            depressed
            @click="submit_code"
          >
            Submit
          </v-btn>
        </v-actions>
      </v-row>
    </v-row>
  </v-container>
</template>

<script>
  import server from '@/server.js'

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
        code: 'def main():\n\treturn "Hello World!"\n',
        res: null,
      }
    },

    methods: {
      submit_code () {
        console.log(this.code)
        server.post('/submit', {
          code: this.code,
        }).then(res => {
          this.res = res
          console.log(res)
          console.log('yes')
        }, error => {
          console.log(error)
        })
      },
    },
  }
</script>
