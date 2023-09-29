<template>
  <div>
    <h1>Role</h1>
    <table class="table table-bordered">
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
        <tr v-if="role">
          <td>{{ role.Role_Listing_ID }}</td>
          <td>{{ role.Role_Name }}</td>
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
        role: null,
      };
    },
    props: ['Role_Listing_ID'],
    mounted() {
      this.fetchRoleData();
      this.getRoleName();
    },
    methods: {
      fetchRoleData() {
        fetch('http://localhost:5000/api/roles/' + this.Role_Listing_ID ) // Use the Flask route you defined
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            this.role = data.data;
            console.log(data)
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      },
      getRoleName(){
        fetch('http://localhost:5000/api/get-roles-info/1' ) // Use the Flask route you defined
          .then((response) => {
            return response.text();
          })
          .then((data) => {
            this.role = data.data;
            console.log(data)
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      },
    },
  };
  </script>

  