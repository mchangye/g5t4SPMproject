<template>
  <!--Main layout-->
  <main>
    <div class="container-flex">
      <h1>{{ info.Role_Name }}</h1>
      <button type="button" class="btn btn-info">Apply Job</button>
      <table class="table table-bordered table-responsive w-100 d-block d-md-table">
        <thead>
          <tr>
            <th>Role Listing ID</th>
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
            <td>{{ role.department_name }}</td>
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
      role: null,
      info: []
    };
  },
  props: ['Role_Listing_ID'],
  mounted() {
    this.fetchRoleData();
    this.getRoleName();
  },
  methods: {
    fetchRoleData() {
      fetch('http://localhost:5000/api/roles/' + this.Role_Listing_ID) // Use the Flask route you defined
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
    getRoleName() {
      fetch('http://localhost:5000/api/get-roles-info/' + this.Role_Listing_ID) // should be using corresponding Role_ID instead
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.info = data;
          console.log(data)
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
  },
};
</script>

  