import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/monitor',
    name: 'Monitor',
    component: () => import(/* webpackChunkName: "about" */ '../views/Monitor.vue')
  },
  {
    path: '/stat',
    name: 'Stat',
    component: () => import(/* webpackChunkName: "about" */ '../views/Stat.vue')
  },
  {
    path: '/task',
    name: 'Tasks',
    component: () => import(/* webpackChunkName: "about" */ '../views/Tasks.vue')
  },
  {
    path: '/log',
    name: 'Log',
    component: () => import(/* webpackChunkName: "about" */ '../views/Log.vue')
  },
  {
    path: '/app',
    name: 'App',
    component: () => import(/* webpackChunkName: "about" */ '../views/Application.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
