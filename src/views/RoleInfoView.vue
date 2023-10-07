<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container-flex">
      <div class="row role-header mb-5">
        <div class="col">
          <h2>{{ info.Role_Name }}</h2>
        </div>
        

        <div class="col">
          <button type="button" class="btn btn-primary me-2">Edit Details</button>
          <button type="button" class="btn btn-primary">View Applicants</button>
        </div>  
      </div>

      <span v-if="role">
        <p><span class="fw-bold">Department:</span> {{ role.department_name }}</p>
        <p><span class="fw-bold">Expiry Date:</span> {{ role.Expiry_Date }}</p>
        <span class="fw-bold">Role Description:</span>
        <p> {{ role.Role_Desc }} </p>
        <p><span class="fw-bold">Skills Required:</span> </p>
        <ul>
          <li v-for="skill in role.role_skills">{{ skill }}</li>
        </ul>
      </span>

    </div>
  </main>
</template>
  
<script>
export default {
  data() {
    return {
      role: null,
      info: {}
    };
  },
  props: ['Role_Listing_ID'],
  mounted() {
    this.fetchRoleData();
    this.getRoleName();
  },
  methods: {
    fetchRoleData() {
      fetch('http://localhost:5000/api/roles/' + this.Role_Listing_ID)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.role = data.data;

          // Set Role_ID to a data property for later use
          this.Role_ID = data.data.Role_ID;

          console.log("role id for current role listing id:" + this.Role_ID)
          console.log(data);

          this.getRoleName(); // Call getRoleName after setting Role_ID
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    getRoleName() {
      fetch('http://localhost:5000/api/get-roles-info/' + this.Role_ID) // use the Role_ID of current Role_Listing_ID
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.info = data;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
  },

};
</script>

