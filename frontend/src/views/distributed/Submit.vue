<template>
  <v-container>
    <v-row class="px-16 py-3 justify-items">
      <v-row>
        <v-col>
          <codemirror
            v-model="code"
            :options="cmOptions"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            text
          >
            Clear
          </v-btn>
          <v-spacer />
          <v-btn
            class="white--text"
            color="deep-purple accent-4"
            depressed
            @click="submit_code"
          >
            Submit
          </v-btn>
        </v-col>
      </v-row>
    </v-row>
  </v-container>
</template>

<script>
  import server from '@/server.js'
  import 'codemirror/mode/python/python.js'
  import 'codemirror/theme/solarized.css'
  export default {
    name: 'Submit',
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
        code: 'def main():\n    """\n    Write anything in anywhere!\n    As long as your result is returned in this function\n    """\n    return "Hello World!"\n',
        cmOptions: {
          tabSize: 4,
          mode: 'python',
          theme: 'solarized',
          lineNumbers: true,
          line: true,
          // more CodeMirror options...
        },
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

<style scoped>
.CodeMirror {
  /* border: 1px solid #eee; */
  height: auto;
  width: 80%;
}
</style>
