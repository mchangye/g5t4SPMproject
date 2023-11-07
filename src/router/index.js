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
      path: '/about/:user_id_search',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
      props: true
    },
    {
      path: '/staffinfo',
      name: 'staffinfo',
      component: () => import('../views/StaffInfoView.vue')
    },
    {
      path: '/browserolesstaff',
      name: 'browserolesstaff',
      component: () => import('../views/BrowseRolesStaffView.vue'),
      meta: {
        key: 'browse-roles-staff'
      }
    },
    {
      path: '/browseroleshr',
      name: 'browseroleshr',
      component: () => import('../views/BrowseRolesHRView.vue'),
      meta: {
        key: 'browse-roles-hr'
      }
    },
    {
      path: '/rolesinfo',
      name: 'rolesinfo',
      component: () => import('../views/RolesInfoView.vue')
    },
    {
      path: '/rolestaff/:Role_Listing_ID',
      name: 'roleinfostaff',
      component: () => import('../views/RoleInfoStaffView.vue'),
      props: true
    },
    {
      path: '/rolehr/:Role_Listing_ID',
      name: 'roleinfohr',
      component: () => import('../views/RoleInfoHRView.vue'),
      props: true
    },
    {
      path: '/profile/:user_id',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
      props: true
    },
    {
      path: '/myapplications/',
      name: 'myapplications',
      component: () => import('../views/MyApplicationsView.vue')
    },
    {
      path: '/updateskill/',
      name: 'updateskill',
      component: () => import('../views/UpdateSkill.vue')
    },
    {
      path: '/applyrole/',
      name: 'applyrole',
      component: () => import('../views/ApplyRole.vue')
    },
    {
      path: '/newrole/',
      name: 'newrole',
      component: () => import('../views/CreateRoleListing.vue')
    },
    {
      path: '/updaterolelisting/:Role_Listing_ID',
      name: 'updaterolelisting',
      component: () => import('../views/UpdateRoleListing.vue'),
      props: true
    }
  ]
})

export default router
