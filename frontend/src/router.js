import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/views/dashboard/Index'),
      children: [
        // Distributed Platform
        {
          path: 'distributed/information',
          name: 'About',
          component: () => import('@/views/distributed/About'),
        },
        {
          path: 'distributed/submit',
          name: 'Submit',
          component: () => import('@/views/distributed/Submit'),
        },
        {
          path: 'distributed/stat',
          name: 'Stat',
          component: () => import('@/views/distributed/Stat'),
        },
        {
          path: 'distributed/task',
          name: 'Tasks',
          component: () => import('@/views/distributed/Tasks'),
        },
        {
          path: 'distributed/workers',
          name: 'Workers',
          component: () => import('@/views/distributed/Workers'),
        },
        {
          path: 'distributed/taskresult',
          name: 'TaskResult',
          component: () => import('@/views/distributed/TaskResult'),
        },
        {
          path: 'distributed/log',
          name: 'Log',
          component: () => import('@/views/distributed/Log'),
        },
        {
          path: 'distributed/app',
          name: 'App',
          component: () => import('@/views/distributed/Application'),
        },
        // Upgrade
        {
          name: 'Upgrade',
          path: 'upgrade',
          component: () => import('@/views/dashboard/Upgrade'),
        },
      ],
    },
  ],
})
