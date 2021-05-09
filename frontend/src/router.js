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
          path: 'distributed/monitor',
          name: 'Monitor',
          component: () => import('@/views/distributed/Monitor'),
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
          path: 'distributed/log',
          name: 'Log',
          component: () => import('@/views/distributed/Log'),
        },
        {
          path: 'distributed/app',
          name: 'App',
          component: () => import('@/views/distributed/Application'),
        },
        // Dashboard
        {
          name: 'Dashboard',
          path: '',
          component: () => import('@/views/dashboard/Dashboard'),
        },
        // Pages
        {
          name: 'User Profile',
          path: 'pages/user',
          component: () => import('@/views/dashboard/pages/UserProfile'),
        },
        {
          name: 'Notifications',
          path: 'components/notifications',
          component: () => import('@/views/dashboard/component/Notifications'),
        },
        {
          name: 'Icons',
          path: 'components/icons',
          component: () => import('@/views/dashboard/component/Icons'),
        },
        {
          name: 'Typography',
          path: 'components/typography',
          component: () => import('@/views/dashboard/component/Typography'),
        },
        // Tables
        {
          name: 'Regular Tables',
          path: 'tables/regular-tables',
          component: () => import('@/views/dashboard/tables/RegularTables'),
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
