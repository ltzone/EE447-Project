<template>
  <v-container>
    <v-row class="px-16 py-3">
      <v-col>
        <codemirror
          v-model="mapper_code"
          :options="cmOptions"
        />
      </v-col>
    </v-row>
    <v-row class="px-16">
      <v-col>
        <codemirror
          v-model="reducer_code"
          :options="cmOptions"
        />
      </v-col>
    </v-row>
    <v-row class="px-16 py-3">
      <v-row>
        <v-file-input
          v-model="file"
          show-size
          truncate-length="15"
        />
        <v-col>
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
  import vm from '@/main.js'
  import 'codemirror/mode/python/python.js'
  import 'codemirror/theme/solarized.css'
  import codes from '@/assets/codes.js'

  export default {
    name: 'MapReduce',
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
        mapper_code: codes.mapper_code,
        reducer_code: codes.reducer_code,
        cmOptions: {
          tabSize: 4,
          mode: 'python',
          theme: 'solarized',
          lineNumbers: true,
          line: true,
          // more CodeMirror options...
        },
        file: null,
        res: null,
      }
    },

    methods: {
      submit_code () {
        var formData = new FormData()
        formData.append('mapper_code', this.mapper_code)
        formData.append('reducer_code', this.reducer_code)
        formData.append('file', this.file)
        formData.append('mapper_num', 3)
        server.post('/mapreduce', formData).then(res => {
          this.res = res
          vm.$toasted.global.alert_success('Task Submitted, id: ' + res.data.task_id)
        }, error => {
          console.log(error)
          vm.$toasted.global.alert_failure('Task Submit Fails')
        })
      },
    },
  }
</script>

<style scoped>
.CodeMirror {
  /* border: 1px solid #eee; */
  height: auto;
  width: 50%;
}
</style>
