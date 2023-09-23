<template>
<div>
                <h1>Roles Information</h1>
                <ul>
                    {% for role in roles %}
                    <li>{{ role }}</li>
                    {% endfor %}
                </ul>
            </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        roles: {},
      };
    },
    mounted() {
      this.fetchRolesData();
    },
    methods: {
      fetchRolesData() {
        fetch('/api/roles') // Use the Flask route you defined
          .then((response) => response.json())
          .then((data) => {
            this.roles = data; // Update the staff data in the component
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      },
    },
  };
  </script>

  