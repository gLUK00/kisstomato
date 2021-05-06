import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import router from './router'
import store from './store'

import 'jquery/dist/jquery.js'
//import 'popper.js/dist/popper.js'
//import 'bootstrap/dist/css/bootstrap.css'
//import 'bootstrap/dist/js/bootstrap.bundle.js'

//import 'bootstrap-vue/dist/bootstrap-vue.css'
//import 'bootstrap-vue/dist/bootstrap-vue.js'


createApp(App).use(PrimeVue)
	.use(store).use(router).mount('#app');
