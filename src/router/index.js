import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/staffinfo',
      name: 'staffinfo',
      component: () => import('../views/StaffInfoView.vue')
    },
    {
      path: '/browseroles',
      name: 'browseroles',
      component: () => import('../views/BrowseRolesView.vue'),
      meta: {
        key: 'browse-roles'
      }
    },
    {
      path: '/rolesinfo',
      name: 'rolesinfo',
      component: () => import('../views/RolesInfoView.vue')
    },
    {
      path: '/role/:Role_Listing_ID',
      name: 'roleinfo',
      component: () => import('../views/RoleInfoView.vue'),
      props: true
    },
    {
      path: '/profile/',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    }
  ]
})

export default router
