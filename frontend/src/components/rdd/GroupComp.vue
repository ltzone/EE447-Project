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
          <h4> Grouper [{{ name }}] </h4>
          <strong> 1 worker, group all outputs of the above layer by keys </strong>
          <v-btn
            color="red lighten-2"
            dark
            v-bind="attrs"
            v-on="on"
          >
            Config
          </v-btn>
        </v-card>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Grouper Configuration
        </v-card-title>

        <v-row>
          <v-checkbox
            v-model="action"
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
            @click="dialog = false"
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
    name: 'GroupComp',

    props: {
      code: {
        type: String,
        default: codes.mapper_code,
      },
      name: {
        type: String,
        default: 'grouper',
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
      }
    },

    computed: {
    },

    methods: {
      close () {
        this.dialog = false
      },
    },
  }
</script>
