<template>
<div>
                <h1>Roles Information</h1>
                <ul v-if="roles">
                    <li v-for="role in roles" :key="role.ID">
                      {{ role.Role_Name }}
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
        fetch(`http://localhost:5000/api/get-roles-info/`) // Use the Flask route you defined
          .then((response) => {
            if (!response.ok) {
          throw new Error('Network response failed');
            }
          console.log(this.data)
          return response.json()})
          .then((data) => {
            console.log('Fetched data:', data);
            this.roles = data; // Update the roles data in the component
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      },
    },
  };
  </script>

  