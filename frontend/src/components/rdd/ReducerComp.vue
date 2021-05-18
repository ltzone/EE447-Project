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
          <h4> Reducer [{{ name }}] </h4>
          <strong> {{ numWorker }} workers </strong>
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
          <v-col>
            <codemirror
              v-model="code"
              :options="cmOptions"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-checkbox
            v-model="action"
            label="Activate Output"
            class="mx-3"
          />
          <v-text-field
            v-model="name"
            class="mx-3"
            label="Reducer name"
          />
          <v-text-field
            v-model="numWorker"
            class="mx-3"
            label="Number of Reducers"
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
    name: 'ReducerComp',

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
