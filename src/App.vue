<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <!-- Include Sidebar Component -->
    <Navbar />
    
    <div class="content">
      <!-- Place the router view here to render the current page -->
      
      <router-view />
    </div>
    <div class="icons">
    <RouterLink to="/profile"><button class="btn btn-primary">Profile</button></RouterLink>
  
    <button class="btn btn-primary">Notifications</button>
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



