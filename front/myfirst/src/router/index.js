import Vue from 'vue'
import Router from 'vue-router'
import Test from '@/pages/Test'
import page2 from '@/pages/page2'
import PageThree from '@/pages/PageThree'
import pageFour from '@/pages/pageFour'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Test',
      component: Test
    },
    {
      path: '/Test',
      name: 'Test',
      component: Test
    },
    {
      path: '/page2',
      name: 'page2',
      component: page2
    },
    {
      path: '/PageThree',
      name: 'PageThree',
      component: PageThree
    },
    {
      path: '/pageFour',
      name: 'pageFour',
      component: pageFour
    }
  ]
})
