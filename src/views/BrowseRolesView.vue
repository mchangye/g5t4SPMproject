<template>
  <div>
    <h1>Role Listings</h1>
    <table class="table table-bordered">
      <thead>
        <tr>
          <th><b>Role Listing ID</b></th>
          <th><b>Role Name</b></th>
          <th><b>Department</b></th>
          <th><b>Description</b></th>
          <th><b>Skills</b></th>
          <th><b>Applicants</b></th>
          <th><b>Expiry Date</b></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="role in roles" :key="role.Role_Listing_ID">
          <td>{{ role.Role_Listing_ID }}</td>
          <td>
            <router-link :to="'/role/' + role.Role_Listing_ID">{{ role.Role_Name }}</router-link>
          </td>
          <td>{{ role.Role_department_ID }}</td>
          <td>{{ role.Role_Desc }}</td>
          <td>
            <ul>
              <li v-for="skill in role.role_skills">{{ skill }}</li>
            </ul>
          </td>
          <td>TBC NEXT SPRINT</td>
          <td>{{ role.Expiry_Date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
  
  <script>
  export default {
    data() {
      return {
        roles: [],
      };
    },
    mounted() {
      this.fetchRolesData();
    },
    methods: {
      fetchRolesData() {
        fetch('http://localhost:5000/api/roles') // Use the Flask route you defined
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            this.roles = data.data.roles;
            console.log(data)
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      },
    },
  };
  </script>

<style scoped>
  div {
    margin: auto auto;
    
  }

</style>
  