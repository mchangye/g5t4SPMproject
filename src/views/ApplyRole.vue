<template>
    <div>
      <h2>Apply for Role</h2>
      <form @submit.prevent="submitApplication">
        <label for="staffId">Staff ID:</label>
        <input type="text" id="staffId" v-model="staffId" required>
        <br>
        <br>
        <label for="roleListingId">Role Listing ID:</label>
        <input type="text" id="roleListingId" v-model="roleListingId" required>
        <br>
        <br>
        <button type="submit">Apply</button>
      </form>
    </div>
</template>


<script>
import axios from 'axios';
import eventBus from '@/event-bus';

  export default {
    data() {
      return {
        staffId: "",
        roleListingId: "",
      };
    },
    methods: {
      submitApplication() {
      console.log(this.staffId)
      console.log(this.roleListingId)
      axios.post('http://localhost:5000/api/apply-role',{
        Staff_ID: this.staffId,
        Role_Listing_ID: this.roleListingId,
      })
          .then(response => {
              console.log(response.data);
          })
          .catch( error => {
              console.log(error.message);
          });
      },
    },
  };
</script>
  