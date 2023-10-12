<template>
  <main>
    <h1>This is the landing page.</h1> <br><br>
    <h2>The Roles Info page has not been added yet.</h2> <br><br>
    I don't want the page to have half of it be navbar and half of it be function, it was just the preset. Can change to bootstrap as per usual. -Dex
  </main>

  <div>
    <!-- test feasibility of user login page-->
    <diV><img src="../assets/identify.png" height="200" alt="" loading="lazy" /></div>
    <div id=logindeets><input id="userid" placeholder="insert user id" v-model="user_id_search">
    <router-link :to="'/about/' + user_id_search" class="list-group-item list-group-item-action py-2 ripple">
                        <button v-on:click="sendUserId">submit</button>
                    </router-link> 
                  </div>
                    <!--:class="{ 'active-link': $route.path === '/about' }-->
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_id_search: null,
    };
  },
  methods : {
    sendUserId() {
      console.log("value:", this.user_id_search)
    }
  }
}
</script>
<!-- 
<script>
export default {
  data() {
    return {
      flaskData: '',
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch('')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network response failed');
      }
      return response.text();
    })
    .then((data) => {
      this.flaskData = data;
    })
    .catch((error) => {
      console.error('There was a problem with the fetch operation:', error);
    });
    }
  },
};
</script> -->



<!-- 

<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <TheWelcome />
  </main>
</template> -->
