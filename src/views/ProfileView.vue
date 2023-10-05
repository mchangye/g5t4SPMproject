<template>
    <div class="ProfileInfo">
        <h1>Profile</h1>
        <ul>
            <li>{{ user.Access_Rights }}</li>
            <li>{{ user.Country_ID }}</li>
            <li>{{ user.Department_ID }}</li>
            <li>{{ user.Email }}</li>
            <li>{{ user.Staff_FName }}</li>
            <li>{{ user.Staff_LName }}</li>
        </ul>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                user: [],
            };
        },
        mounted() {
            this.getUserInfo();
        },
    methods: {
        getUserInfo() {
            fetch(`http://localhost:5000/api/get-staff-info/1`)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Network response failed');
                    }
                    return response.json();
                })
                .then((data) => {
                    this.user = data;
                    console.log('Data from getStaffInfoAPI:' + this.staff);
                })
                .catch((error) => {
                    console.error('There was a problem with the getStaffInfoAPI fetch operation:', error);
                });
        }
    }
    };

</script>