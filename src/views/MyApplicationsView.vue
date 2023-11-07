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
                            <router-link :to="'/rolestaff/' + application.Role_Listing_ID"> {{ application.Role_Name }}
                            </router-link>
                        </td>
                        <td>{{ application.Department_Name }}</td>
                        <td>{{ application.Role_Listing_Desc }}</td>
                        <td> {{ application.role_skill_match_percentage }} </td>
                        <td> TBC </td>
                        <td>{{ application.Time_Stamp }}</td>
                    </tr>
                </tbody>

            </table>

        </div>
    </main>
</template>
    
<script>
import eventBus from '@/event-bus';

export default {
    data() {
        return {
            applications: [],
            dt: null,
            staffId: null,
        };
    },
    mounted() {
        this.dt = $(this.$refs.applicationsTable).DataTable();
        this.getApplications();
    },
    created() {
        // Access the staff_id from the event bus
        this.staffId = eventBus.getStaffId();
        console.log("app page current staff id:" + this.staffId)
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
            fetch('http://localhost:5000/api/applications/staff/' + this.staffId) // NEED TO USE CURRENT STAFF'S ID
                .then((response) => {
                    return response.json();
                })
                .then(async (data) => {
                    this.applications = data.data.applications;

                    await this.getRoleSkillMatchPercentageForApplications();

                    console.log("All applications for this staff")
                    console.log(data);

                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        },
        async getRoleSkillMatchPercentage(roleID) {
            try {
                const response = await fetch('http://localhost:5000/api/calc_rsm/' + roleID + '/' + this.staffId);
                const data = await response.json();
                return data.role_skill_match_percentage;
            } catch(error) {
                console.error('Error fetching RSM%:', error);
            }
        },
        async getRoleSkillMatchPercentageForApplications() {
            console.log('Applications:', this.applications);
            for (const application of this.applications) {
                application.role_skill_match_percentage = await this.getRoleSkillMatchPercentage(application.Role_ID);
                console.log(`Application ID ${application.Application_ID} - Role ID ${application.Role_ID} - RSM%: ${application.role_skill_match_percentage}`);
            }
        },
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