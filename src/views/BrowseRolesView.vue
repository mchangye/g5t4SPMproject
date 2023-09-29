<template>
<div class="browseroles">
                <h1>All Roles</h1>
                <ul>
                  <li v-for="role in roles" :key="role.Role_Listing_ID">
                    <p>Role Listing ID: {{ role.Role_Listing_ID }}</p>
                    <p>Department: {{ role.Role_department_ID }}</p>
                    <p>Description: {{ role.Role_Desc }}</p>
                    <p>Skills: 
                      <ul>
                        <li v-for="skill in role.role_skills">{{ skill }}</li>
                      </ul>
                    </p>
                    <p>Applicants: TO BE DONE</p>
                    <p>Expiry: {{ role.Expiry_Date }}</p>
                  </li>
                </ul>
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
  