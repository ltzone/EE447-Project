<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="80%"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-card
          class="pa-6"
          elevation="2"
          shaped
        >
          <h4> Sorter [{{ nameLocal }}] </h4>
          <strong> 1 worker, merge all outputs of the above layer </strong>
          <v-btn
            color="red lighten-2"
            dark
            v-bind="attrs"
            v-on="on"
          >
            Edit
          </v-btn>
        </v-card>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Reducer Configuration
        </v-card-title>

        <v-row>
          <v-checkbox
            v-model="actionLocal"
            label="Activate Output"
            class="mx-3"
          />
        </v-row>

        <v-divider />

        <v-card-actions>
          <v-spacer />
          <v-btn
            color="primary"
            text
            @click="close"
          >
            Close
          </v-btn>
          <v-spacer />
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  import codes from '@/assets/codes.js'
  import 'codemirror/mode/python/python.js'
  import 'codemirror/theme/solarized.css'

  export default {
    name: 'MapComp',

    props: {
      code: {
        type: String,
        default: codes.reducer_code,
      },
      name: {
        type: String,
        default: 'reducer',
      },
      numWorker: {
        type: Number,
        default: 1,
      },
      action: {
        type: Boolean,
        default: false,
      },
    },

    data () {
      return {
        dialog: false,
        cmOptions: {
          tabSize: 4,
          mode: 'python',
          theme: 'solarized',
          lineNumbers: true,
          line: true,
          // more CodeMirror options...
        },
        curTask: {},
      }
    },

    computed: {
      codeLocal: {
        get: function () {
          return this.code
        },
        set: function (value) {
          this.curTask.code = value
        },
      },

      nameLocal: {
        get: function () {
          return this.name
        },
        set: function (value) {
          this.curTask.name = value
        },
      },

      numWorkerLocal: {
        get: function () {
          return this.numWorker
        },
        set: function (value) {
          this.curTask.numWorker = Number(value)
        },
      },

      actionLocal: {
        get: function () {
          return this.action
        },
        set: function (value) {
          this.curTask.action = value
        },
      },
    },

    watch: {

    },

    methods: {
      close () {
        this.dialog = false
        this.$emit('dialogData', this.curTask)
      },
    },
  }
</script>
