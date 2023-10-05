<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container-flex">
      <h1>Role Listings</h1>
      <table class="table table-bordered table-responsive w-100 d-block d-md-table">
        <thead>
          <tr>
            <th>Role Listing ID</th>
            <th>Role Name</th>
            <th>Department</th>
            <th>Description</th>
            <th>Skills</th>
            <th>Applicants</th>
            <th>Expiry Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="role in roles" :key="role.Role_Listing_ID">
            <td>{{ role.Role_Listing_ID }}</td>
            <td>
              <router-link :to="'/role/' + role.Role_Listing_ID">{{ role.Role_Name }}</router-link>
            </td>
            <td>{{ role.Department_Name }}</td>
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
  </main>
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
  