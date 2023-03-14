// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
<<<<<<< HEAD
import VueResource from 'vue-resource'

=======
import VueLogger from 'vuejs-logger'
import VueResource from 'vue-resource'


>>>>>>> ffb9697e69e3fe2d16935fc8a8535647447fb395
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VueResource)

Vue.config.productionTip = false

<<<<<<< HEAD
=======
const isProduction = process.env.NODE_ENV === 'production'
 
const options = {
    isEnabled: true,
    logLevel : isProduction ? 'error' : 'debug',
    stringifyArguments : false,
    showLogLevel : true,
    showMethodName : true,
    separator: '|',
    showConsoleColors: true
}
 
Vue.use(VueLogger, options)

>>>>>>> ffb9697e69e3fe2d16935fc8a8535647447fb395
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
