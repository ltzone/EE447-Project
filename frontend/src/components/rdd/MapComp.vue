<template>
  <div class="text-center">
    <base-material-card
      color="pink"
      class="px-5 py-3"
    >
      <template v-slot:heading>
        <div class="text-h3 font-weight-light">
          Mapper
        </div>

        <div class="text-subtitle-1 font-weight-light">
          {{ nameLocal }}
        </div>
      </template>
      <v-card-text>
        <v-row>
          <v-file-input
            label="Upload a file if there is an input, otherwise the transformation will take the output of the last layer as input."
            v-model="inputLocal"
            show-size
            truncate-length="15"
          />
        </v-row>
        <v-row>
          <v-col style="text-align:left;">
            <codemirror
              v-model="codeLocal"
              :options="cmOptions"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-checkbox
            v-model="actionLocal"
            label="Activate Output"
            class="mx-3"
          />
          <v-text-field
            v-model="nameLocal"
            class="mx-3"
            label="Mapper name"
          />
          <v-text-field
            v-model="numWorkerLocal"
            class="mx-3"
            label="Number of Mappers"
          />
          <v-btn
            color="pink lighten-2"
            dark
            @click="close"
          >
            Confirm
          </v-btn>
        </v-row>
      </v-card-text>
    </base-material-card>
    <!-- <v-dialog
      v-model="dialog"
      width="80%"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-card
          class="pa-6"
          elevation="2"
          shaped
        >
          <h4> Mapper [{{ nameLocal }}] </h4>
          <strong> {{ numWorkerLocal }} workers </strong>
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
          Mapper Configuration
        </v-card-title>

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
    </v-dialog> -->
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
        default: codes.mapper_code,
      },
      name: {
        type: String,
        default: 'mapper',
      },
      numWorker: {
        type: Number,
        default: 3,
      },
      input: {
        type: File,
        default: null,
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

      inputLocal: {
        get: function () {
          return this.input
        },
        set: function (value) {
          this.curTask.input = value
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
