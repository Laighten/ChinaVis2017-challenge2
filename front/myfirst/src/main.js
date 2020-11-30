import Vue from 'vue'
import App from './App'

import router from './router'
//引入bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/css/application.css'
//引入element-Ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import Bus from './Bus'


import 'font-awesome/css/font-awesome.min.css'


Vue.config.productionTip = false
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  data: {
    Bus
  }
  
})
