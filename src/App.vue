<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <!-- Include Navbar Component -->
    <Navbar />
    
    <div class="content">
      <!-- Place the router view here to render the current page -->
      
      <router-view />
    </div>

  </div>
</template>


<script>
  export default {
    components: {
      Navbar, // Register Sidebar component
    },
  };
</script>



