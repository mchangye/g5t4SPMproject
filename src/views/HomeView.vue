

<template>
  <div class="background">
    <div class="login-box">

      <h1>Welcome</h1>
      <img src="../assets/sbrplogo.png" height="200" alt="" loading="lazy" />

      <div id=logindeets style="display: flex; flex-direction: column; align-items: center;">
        <input class="form-control" type="text" id="userid" placeholder="Insert Staff ID" v-model="staff_id" style="width: 220px; text-align: center; margin: 20px; margin-bottom: 10px;">
        <button type="button" class="btn btn-primary" v-on:click="storeStaffID" style="width: 220px;">submit</button>
      </div>

      
    </div>
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

          let route = this.isManagement ? '/browseroleshr' : '/browserolesstaff';

          this.$router.push(route);
        })
        .catch((error) => {
          console.error('There was a problem with the getStaffInfoAPI fetch operation:', error);
        });
    }
  },
  computed: {
    getRoleBasedRoute() {
      if (this.isManagement) {
        return '/browseroleshr';
      } else {
        return '/browserolesstaff';
      }
    },
  }
}
</script>

<style>
.background {
  margin-right: 230px;
  margin-top: -40px;
}
.login-box {
  /* position: absolute; */
  height: 100%;
  width: 100%;
  border: 1px solid #cecece;
  border-radius: 10px;
  padding: 20px;
  padding-top:40px;
  padding-bottom: 50px;
  margin-right: 50px;
  /* width: 400px; */
  text-align: center;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
  background-color: white;
  overflow-y: hidden;
}
</style>