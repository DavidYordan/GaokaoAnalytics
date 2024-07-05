import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home.vue';
import SpecialScore from '@/views/SpecialScore.vue';
import SpecialPlan from '@/views/SpecialPlan.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/special-score',
      name: 'SpecialScore',
      component: SpecialScore
    },
    {
      path: '/special-plan',
      name: 'SpecialPlan',
      component: SpecialPlan
    }
  ]
});
