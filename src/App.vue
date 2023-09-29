<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header class="header">
    <div class="logocontainer">
    <img alt="Vue logo" class="logo" src="@/assets/sbrplogo.png" width="125" height="125" />
    </div>
    <div class="websitetitle"><h2>Job Search</h2></div>
    <!-- <div class="wrapper"> -->
      <!-- <HelloWorld msg="You did it!" /> -->
      <div class="navigation bar">
      <nav>
        <ul>
        <li><RouterLink to="/">Landing</RouterLink></li>

        <li><RouterLink to="/about">About (Default)</RouterLink></li>
        <li><RouterLink to="/staffinfo">Staff Info</RouterLink></li>
        <li><RouterLink to="/rolesinfo">Roles Info</RouterLink></li>
        <li><RouterLink to="/browseroles">Browse Roles</RouterLink></li>
      </ul>
      </nav>
      </div>
    <!-- </div> -->
  </header>

  <RouterView />
</template>

<style scoped>
header {
  display : flex;
  flex-direction: column;
  width: 100%;
  line-height: 1.5;
  max-height: 100vh;
  float: left;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 200px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 3rem 0;
    margin-top: 1rem;
  }
}
</style>
