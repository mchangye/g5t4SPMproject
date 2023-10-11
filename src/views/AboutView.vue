<template>
  <div class="about">
    <!--<h1>This is a default about page</h1>-->
    
    <h1>{{ user.Staff_FName }}</h1>
    <h1>{{ user.Staff_LName }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: '',
    };
  },
props: ['user_id_search'],
mounted() {
    this.fetchUserData();
},
methods: {
    fetchUserData() {
      if (!this.user_id_search) {
      console.error('user id is not defined or valid');
      return;
  }
    fetch(`http://localhost:5000/api/get-staff-info/` + this.user_id_search)

                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Network response failed');
                    }
                    return response.json();
                })
                .then((data) => {
                    this.user = data;
                    console.log(user);
                })
                .catch((error) => {
                    console.error('There was a problem with the getStaffInfoAPI fetch operation:', error);
                });
    }
  }
}
</script>
<style scoped>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: top;
  }
}
</style>
