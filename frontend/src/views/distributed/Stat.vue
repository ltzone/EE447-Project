<template>
  <v-container>
    <v-row
      v-for="tasks, i in taskML"
      :key="i"
      class="align-center"
    >
      <v-col
        v-for="task, j in tasks"
        :key="j"
      >
        <div v-if="task.type === 'mapper'">
          <map-comp
            v-bind="task"
            @dialogData="changeTask(i,j, $event)"
          />
        </div>
        <div v-if="task.type === 'reducer'">
          <reduce-comp
            v-bind="task"
            @dialogData="changeTask(i,j, $event)"
          />
        </div>
        <div v-if="task.type === 'sort'">
          <sort-comp
            v-bind="task"
            @dialogData="changeTask(i,j, $event)"
          />
        </div>
        <div v-if="task.type === 'group'">
          <group-comp
            v-bind="task"
            @dialogData="changeTask(i,j, $event)"
          />
        </div>
      </v-col>
      <v-col
        cols="2"
      >
        <div
          class="text-center"
          cols="1"
        >
          <v-menu
            v-model="colmenu[i]"
            :close-on-content-click="false"
            :nudge-width="200"
            offset-x
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="secondary"
                dark
                fab
                v-bind="attrs"
                v-on="on"
              >
                <v-icon dark>
                  mdi-plus
                </v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item
                v-for="(item, idx) in additems"
                :key="idx"
              >
                <v-list-item-action>
                  <v-btn
                    color="primary"
                    @click="addcol(i, item)"
                  >
                    {{ item }}
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
      </v-col>
    </v-row>
    <div class="text-center">
      <v-menu
        v-model="menu"
        :close-on-content-click="false"
        :nudge-width="200"
        offset-x
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="indigo"
            dark
            v-bind="attrs"
            v-on="on"
          >
            Add a new row
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, idx) in additems"
            :key="idx"
          >
            <v-list-item-action>
              <v-btn
                color="primary"
                @click="addrow(item)"
              >
                {{ item }}
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </v-container>
</template>

<script>
  // import server from '@/server.js'
  // import RddComp from '../../components/rdd/RddComp.vue'
  import MapComp from '../../components/rdd/MapComp.vue'
  import ReduceComp from '../../components/rdd/ReducerComp.vue'
  import SortComp from '../../components/rdd/SortComp.vue'
  import codes from '@/assets/codes.js'
  import GroupComp from '../../components/rdd/GroupComp.vue'
  import lodash from 'lodash'

  export default {
    name: 'Stat',

    components: {
      // RddComp,
      MapComp,
      ReduceComp,
      SortComp,
      GroupComp,
    },

    data () {
      return {
        taskML: [],
        additems: ['mapper', 'reducer', 'sort', 'group'],
        menu: false,
        colmenu: [],
      }
    },

    methods: {
      addrow (tasktype) {
        var newTask = {
          type: tasktype,
          name: 'default ' + tasktype,
          numWorker: tasktype === 'mapper' ? 3 : 1,
          input: null,
          action: tasktype === 'reducer',
          code: '',
        }
        if (tasktype === 'reducer') {
          newTask.code = codes.reducer_code
        } else if (tasktype === 'mapper') {
          newTask.code = codes.mapper_code
        }
        this.taskML.push([newTask])
        this.colmenu.push(false)
        this.menu = false
      },

      addcol (i, tasktype) {
        var newTask = {
          type: tasktype,
          name: 'default ' + tasktype,
          numWorker: tasktype === 'mapper' ? 3 : 1,
          input: null,
          action: tasktype === 'reducer',
          code: '',
        }
        if (tasktype === 'reducer') {
          newTask.code = codes.reducer_code
        } else if (tasktype === 'mapper') {
          newTask.code = codes.mapper_code
        }
        this.taskML[i].push(newTask)
        this.colmenu[i] = false
      },

      changeTask (i, j, value) {
        console.log(i, j, value)
        this.taskML[i][j] = lodash.extend(this.taskML[i][j], value)
        console.log(this.taskML[i][j])
      },
    },

    mounted () {
    },
  }
</script>
