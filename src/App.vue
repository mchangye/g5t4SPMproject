<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="wholepage">
    <!-- Include Navbar Component -->
    <Navbar v-if="showNavbar()" />

    <div class="content">
      <!-- Place the router view here to render the current page -->

      <router-view />
    </div>

  </div>
</template>


<script>
import eventBus from '@/event-bus';

export default {
  data() {
    return {
      staff_id: null,
    };
  },
  components: {
    Navbar, // Register Sidebar component
  },

  methods: {
    showNavbar() {
      return this.$route.path !== '/';
    },
  },
  created() {
    // Use the event bus to access the staff_id
    this.staff_id = eventBus.getStaffId();
  }
}

</script>



