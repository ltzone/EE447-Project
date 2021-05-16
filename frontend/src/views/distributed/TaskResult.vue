<template>
  <v-container
    id="regular-tables"
    fluid
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title=""
      class="px-5 py-3"
    >
      <v-data-table
        :headers="headers"
        :items="results"
        :items-per-page="5"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <span>{{ getdetail }}</span>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  close
                </v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </template>
        <template v-slot:[`item.actions`]="{ item }">
          <v-icon
            small
            class="mr-2"
            @click="editItem(item)"
          >
            mdi-clipboard-text
          </v-icon>
        </template>
        <template v-slot:no-data>
          <v-btn
            color="primary"
            @click="initialize"
          >
            Reset
          </v-btn>
        </template>
      </v-data-table>
    </base-material-card>
  </v-container>
</template>

<script>
  import server from '@/server.js'
  export default {
    name: 'Tasks',
    components: {},
    data () {
      return {
        try: 'sdsd',
        dialog: false,
        headers: [
          {
            text: 'Task_ID',
            align: 'start',
            sortable: false,
            value: 'id',
          },
          { text: 'Task_Name', value: 'task_name' },
          { text: 'State', value: 'status' },
          { text: 'Worker', value: 'worker' },
          { text: 'Finished_Time ', value: 'date_done' },
          { text: 'Result', value: 'actions' },
        ],
        results: [],
        detail: [],
        status: [],
        running_tasks: [
          {
            id: 1,
            name: 'Map Reduce',
            state: 'Tony Zhou',
            when: 'Map Reducing',
            worker: '70min',
          },
        ],
        editedIndex: -1,
        editedItem: {
          name: '',
          calories: 0,
          fat: 0,
          carbs: 0,
          protein: 0,
        },
        defaultItem: {
          name: '',
          calories: 0,
          fat: 0,
          carbs: 0,
          protein: 0,
        },
      }
    },

    computed: {
      formTitle () {
        return this.status[this.editedIndex] === 'SUCCESS' ? 'Result Details' : 'Traceback'
      },
      getdetail () {
        return this.detail[this.editedIndex]
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
    },

    mounted () {
      server.get('/get').then(
        res => {
          var ta = []
          var de = []
          var st = []
          for (var i = 0; i < res.data.length; i++) {
            var ob = { id: '', task_name: '', status: '', worker: '', date_done: '', actions: null }
            if (res.data[i].status) {
              ob.id = res.data[i].task_id
              ob.task_name = res.data[i].task_name
              ob.status = res.data[i].status
              ob.worker = res.data[i].worker
              ob.date_done = res.data[i].date_done
              if (res.data[i].status === 'SUCCESS') {
                de.push(res.data[i].result)
              } else {
                de.push(res.data[i].traceback)
              }
              ta.push(ob)
              st.push(res.data[i].status)
            }
          }

          this.results = ta
          this.detail = de
          this.status = st
        },
        error => {
          this.results = error
          this.detail = error
          this.status = error
        })
    },

    methods: {
      editItem (item) {
        this.editedIndex = this.results.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },
      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },
    },
  }
</script>
