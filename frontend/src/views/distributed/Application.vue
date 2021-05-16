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
        mapper_code: 'def mapper(input):\n    """\n    Write your mapper code here, \n    the mapper should take in a list of strings as input \n    and return a list of strings as output\n    """\n    output = []\n    for line in input:\n        line=line.strip()\n        words=line.split()\n        for word in words:\n            output.append(f"{word}\\t1")\n    return output',
        reducer_code: 'def reducer(input):\n    """\n    Write your reducer code here,\n    the reducer should tak in a list of strings as input\n    and return a list of strings as output\n    """\n    current_word = None\n    current_count = 0\n    word = None\n    output = []\n\n    for line in input:\n        # remove leading and trailing whitespace\n        line = line.strip()\n\n        # parse the input we got from mapper.py\n        word, count = line.split("\\t", 1)\n\n        # convert count (currently a string) to int\n        try:\n            count = int(count)\n        except ValueError:\n            # count was not a number, so silently\n            # ignore/discard this line\n            continue\n\n        # this IF-switch only works because the framework sorts map output\n        # by key (here: word) before it is passed to the reducer\n        if current_word == word:\n            current_count += count\n        else:\n            if current_word:\n                # write result to STDOUT\n                output.append(f"{current_word}\\t{current_count}")\n            current_count = count\n            current_word = word\n\n    # do not forget to output the last word if needed!\n    if current_word == word:\n        output.append(f"{current_word}\\t{current_count}")\n    \n    return output',
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
