import Vue from 'vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'

import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from 'vue-router';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Customerpage from './components/Customerpage.vue';
import Company from './components/Company.vue';
import Reservationpage from './components/Reservationpage.vue'
import ProgramTour from './components/ProgramTour.vue'
import Guide from './components/Guide.vue'
import Booking from './components/Booking.vue'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VueAxios, axios)
Vue.use(VueRouter);
const routes = [
  {
    name: "Customerpage",
    path: "/Customerpage",
    component: Customerpage
  },
  {
    name: "Company",
    path: "/Company",
    component: Company
  },
  {
    name: "Reservationpage",
    path: "/Reservationpage",
    component: Reservationpage
  },
  {
    name: "ProgramTour",
    path: "/ProgramTour",
    component: ProgramTour
  },
  {
    name: "Guide",
    path: "/Guide",
    component: Guide
  },
  {
    name: "Booking",
    path: "/Booking",
    component: Booking
  }
  
];

const router = new VueRouter({ mode: "history", routes: routes });

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')

