<template>
<div>
                <h1>All Roles</h1>
                <ul>
                  <li v-for="role in roles" :key="role.Role_ID">
                    {{ role.Role_ID }}
                    
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
            this.roles = data;
            console.log(data)
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      },
    },
  };
  </script>

  