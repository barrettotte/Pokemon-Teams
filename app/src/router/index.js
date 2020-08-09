import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: 'Home'
    }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/About.vue'),
    meta: {
      title: 'About'
    }
  },
  {
    path: '/teams',
    name: 'teams',
    component: () => import('../views/Teams.vue'),
    meta: {
      title: 'Teams'
    }
  },
  {
    path: '/pokedex',
    name: 'pokedex',
    component: () => import('../views/Pokedex.vue'),
    meta: {
      title: 'Pokedex'
    }
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

// nav guard => change document title to match route
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Pokemon Teams';
  next();
});

export default router;
