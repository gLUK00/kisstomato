import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import PageRoot from '@/components/pages/root.vue'
import PageProject from '@/components/pages/project.vue'
import PageCollections from '@/components/pages/collections.vue'
import PageData from '@/components/pages/data.vue'
import PageTemplates from '@/components/pages/templates.vue'
import PageMerges from '@/components/pages/merges.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: PageRoot
    },
    {
      path: '/project',
      component: PageProject
    },
    {
      path: '/collections',
      component: PageCollections
    },
    {
      path: '/data',
      component: PageData
    },
    {
      path: '/templates',
      component: PageTemplates
    },
    {
      path: '/merges',
      component: PageMerges
    },
    {
      path: '*',
      component: PageRoot
    }
  ]
})
