<template>
  <main>
    <h1>This is the login page.</h1> <br><br>
    <!-- <h2>The Roles Info page has not been added yet.</h2> <br><br> -->
    <!-- I don't want the page to have half of it be navbar and half of it be function, it was just the preset. Can change to
    bootstrap as per usual. -Dex -->
  </main>

  <div>
    <!-- test feasibility of user login page-->
    <!-- <div><img src="../assets/identify.png" height="200" alt="" loading="lazy" /></div> -->
    <div id=logindeets>
      <input id="userid" placeholder="insert staff id" v-model="staff_id">

        <button v-on:click="storeStaffID">submit</button>

    </div>
    <!--:class="{ 'active-link': $route.path === '/about' }-->
  </div>
</template>

<script>
import eventBus from '@/event-bus';

export default {
  data() {
    return {
      staff_id: null,
      isManagement: false,
      isStaff: false
    };
  },
  methods: {
    storeStaffID() {
      // Set the staff_id using the event bus
      eventBus.setStaffId(this.staff_id);
      console.log("value:", this.staff_id)

      this.getAccessLevel();
    },
    getAccessLevel() {
      fetch(`http://localhost:5000/api/get-staff-info/` + this.staff_id)
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response failed');
          }
          return response.json();
        })
        .then((data) => {
          this.userAccessLevel = data.Access_ID;
          this.isManagement = ["Manager", "HR", "Admin"].includes(data.Access_ID);
          this.isStaff = ["User"].includes(data.Access_ID);

          // Determine the route based on the access level
          let route = this.isManagement ? '/browseroleshr' : '/browserolesstaff';

          // Use Vue Router to navigate the user
          this.$router.push(route);
        })
        .catch((error) => {
          console.error('There was a problem with the getStaffInfoAPI fetch operation:', error);
        });
    }
  },
  computed: {
    getRoleBasedRoute() {
      // Replace these conditions with your actual logic
      if (this.isManagement) {
        return '/browseroleshr';
      } else {
        return '/browserolesstaff';
      }
    },
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
