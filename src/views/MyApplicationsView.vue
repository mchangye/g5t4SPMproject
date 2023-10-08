<template>
    <!--Main layout-->
    <main class="pt-3">
        <div class="container-flex">
            <h2 class="mb-5">My Applications</h2>

            <table id="applicationsTable" class="table table-striped" style="width:100%">
                <thead>
                    <tr>
                        <th>Application ID</th>
                        <th>Role Listing ID</th>
                        <th>Department ID</th>
                        <th>Description</th>
                        <th>Role Skill Match</th>
                        <th>Status</th>
                        <th>Applied Date</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="application in applications" :key="application.Application_ID">
                        <td>{{ application.Application_ID }}</td>
                        <td>
                            <router-link :to="'/role/' + application.Role_Listing_ID"> {{ application.Role_Name }} </router-link>
                        </td>
                        <td>{{ application.Department_Name }}</td>
                        <td>{{ application.Description }}</td>
                        <td> TBC </td>
                        <td> TBC </td>
                        <td>{{ application.Time_Stamp }}</td>
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
            applications: [],
            dt: null
        };
    },
    mounted() {
        this.dt = $(this.$refs.applicationsTable).DataTable();
        this.getApplications();
    },
    watch: {
        applications() {
            if (this.dt) {
                this.dt.destroy();
            }
            this.$nextTick(() => {
                new DataTable('#applicationsTable')
            });
        },
    },
    methods: {
        getApplications() {
            fetch('http://localhost:5000/api/applications/staff/2')
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    this.applications = data.data.applications;

                    console.log("All applications for this staff")
                    console.log(data);

                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        }
    },

};
</script>
  
<style scoped>
div {
    margin: auto auto;

}

.box {
    display: inline-block;
    /* Display divs side by side */
    /* width: 50%; Set the width of each div (50% for two divs) */
    padding: 10px;
    /* Optional: Add padding for spacing */
}
</style>