<template>

  <div class="staffinfo">
      <h1>Staff Information</h1>
      <input type="text" placeholder="Enter an ID to search" id="user_staff_id_search" v-model="user_staff_id_search" @keydown.enter="sendUserStaffIDSearch"/>
      <!-- keydown enter means I can search using the Enter Key. -->
      <button type="button" v-on:click="sendUserStaffIDSearch()">Search</button>
      <!-- But this button is also for better user clarity in case they dont use enter key. -->
      <ul v-if="staff">
        <li><strong>Staff First Name:</strong> {{ staff.Staff_FName }}</li>
        <li><strong>Staff Last Name:</strong> {{ staff.Staff_LName }}</li>
        <li><strong>Department ID:</strong> {{ staff.Department_ID }}</li>
        <li><strong>Country ID:</strong> {{ staff.Country_ID }}</li>
        <li><strong>Email:</strong> {{ staff.Email }}</li>
        <li><strong>Access Rights:</strong> {{ staff.Access_Rights }}</li>
      </ul>
</div>
    
</template>

<script>
export default {
  data() {
    return {
      staff: [],
      user_staff_id_search: null, //can change from null to any number if you want to show a person's detail first before searching
    };
  },
  methods: {
    sendUserStaffIDSearch() {
      console.log("value:", this.user_staff_id_search)
      fetch(`http://localhost:5000/api/get-staff-info/` + this.user_staff_id_search)
        .then((response) => {
        if (!response.ok) {
          throw new Error('Network response failed');
        }
        console.log(this.data);
        return response.json();
      })
      .then((data) => {
        this.staff = data;
        console.log(this.staff);
      })
      .catch((error) => {
        console.error('There was a problem with the fetch operation:', error);
      });
    }
  },
  created() {

    this.sendUserStaffIDSearch();

    // fetch(`http://localhost:5000/api/get-staff-info/` + this.user_staff_id_search)
    // // fetch('http://localhost:5000/api/get-staff-info/1')
    // .then((response) => {
    //   if (!response.ok) {
    //     throw new Error('Network response failed');
    //   }
    //   console.log(this.data);
    //   return response.json();
    // })
    // .then((data) => {
    //   this.staff = data;
    //   console.log(this.staff);
    // })
    // .catch((error) => {
    //   console.error('There was a problem with the fetch operation:', error);
    // });
  },
};
</script>

<style scoped>
@media (min-width: 1024px) {
  .staffinfo {
    min-height: 100vh;
    align-items: top;
  }
}
</style>