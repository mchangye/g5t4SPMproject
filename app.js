new Vue({
    el: '#app',
    data: {
        staff: {
            Staff_FName: '',
            Staff_LName: '',
            Dept: '',
            Country: '',
            Email: '',
            Access_Rights: '',
        },
        roles: {
            Role_Name: '',
        }
    },
    mounted() {
        this.fetchStaff();
        this.fetchRoles();
    },
    methods: {
        fetchStaff() {
            fetch('/get-staff')
            .then(response => response.json())
            .then(data => {
                this.staff = data;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        },
        fetchRoles() {
            fetch('/get-roles')
            .then(response => response.json())
            .then(data => {
                this.roles = data;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        },
    }
});
