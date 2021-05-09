// =========================================================
// * Vuetify Material Dashboard - v2.1.0
// =========================================================
//
// * Product Page: https://www.creative-tim.com/product/vuetify-material-dashboard
// * Copyright 2019 Creative Tim (https://www.creative-tim.com)
//
// * Coded by Creative Tim
//
// =========================================================
//
// * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import './plugins/chartist'
import './plugins/vee-validate'
import vuetify from './plugins/vuetify'
import i18n from './i18n'

import vueDebounce from 'vue-debounce'
import VueToasted from 'vue-toasted'

import VueLodash from 'vue-lodash'
import lodash from 'lodash'

import VueCodemirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'

Vue.use(VueLodash, { lodash: lodash })
Vue.use(VueToasted, {
  iconPack: 'material',
  duration: 2500,
  action: {
    text: 'close',
    onClick: (e, toastObject) => { toastObject.goAway(0) },
  },
})

// register custom toasts
Vue.toasted.register('alert_success',
  payload => payload, { type: 'success', icon: 'check', duration: null },
)

Vue.toasted.register('alert_info',
  payload => payload, { type: 'info', icon: 'info', duration: null },
)

Vue.toasted.register('alert_error',
  payload => payload, { type: 'error', icon: 'warning', duration: null },
)

Vue.toasted.register('alert_error_detailed',
  ({ header, message }) => {
    return `${header}<br>${message}`
  },
  {
    type: 'error',
    icon: 'warning',
    duration: null,
    closeOnSwipe: false,
    action: [{
      icon: 'assignment',
      onClick: (e, toastObject) => {
        const dummy = document.createElement('textarea')
        dummy.textContent = toastObject.el.textContent.slice(7, -15)
        document.body.appendChild(dummy)

        const selection = document.getSelection()
        const range = document.createRange()
        range.selectNode(dummy)
        selection.removeAllRanges()
        selection.addRange(range)
        document.execCommand('copy')
        selection.removeAllRanges()
        document.body.removeChild(dummy)

        alert('Error details copied to clipboard.')
      },
    },
    {
      text: 'close',
      onClick: (e, toastObject) => {
        toastObject.goAway(0)
      },
    }],
  },
)

// format date MM/DD/YYYY, hh:mm:ss a
Vue.filter('formatDate', function (value) {
  if (value) {
    const date = new Date(String(value))
    return date.toLocaleString()
  }
})

Vue.use(vueDebounce)

Vue.use(VueCodemirror, /* {
  options: { theme: 'base16-dark', ... },
  events: ['scroll', ...]
} */)

Vue.config.productionTip = false

const vm = new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App),
}).$mount('#app')

export default vm
