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
        }
    },
    mounted() {
        this.fetchStaff();
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
    }
});
