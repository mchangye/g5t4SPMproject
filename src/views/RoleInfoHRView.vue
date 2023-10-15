<!-- AKA Browse Roles (HR) in App -->
<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container-flex">
      <div class="row role-header mb-5">
        <div class="col">
          <h2>{{ info.Role_Name }}</h2>
        </div>
        

        <div class="col">
          <button type="button" class="btn btn-primary me-2">Edit Details</button>
        </div>  
      </div>

      <span v-if="role">
        <p><span class="fw-bold">Department:</span> {{ role.department_name }}</p>
        <p><span class="fw-bold">Expiry Date:</span> {{ role.Expiry_Date }}</p>
        <span class="fw-bold">Role Description:</span>
        <p> {{ role.Role_Listing_Desc }} </p>
        <p><span class="fw-bold">Skills Required:</span> </p>
        <ul>
          <li v-for="skill in role.role_skills">{{ skill }}</li>
        </ul>
        <p><span class="fw-bold">Applicants: </span>{{ applicantCount }}</p>

        <h1>{{ roleSkillMatchPercentage }}</h1>

        <table id="applicantsTable" class="table table-striped" style="width:100%">
        <thead>
          <tr>
            <th>Application ID</th>
            <th>Staff ID</th>
            <th>Staff Name</th>
            <th>Email</th>
            <th>RSM %</th>
            <th>Application Time</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="application in applicants">
            <td>{{ application.Application_ID }}</td>
            <td>
              <router-link :to="'/profile/' + application.Staff_ID">{{ application.Staff_ID }}</router-link>
            </td>
            <td>{{ application.Staff_Name }}</td>
            <td>{{ application.Email }}</td>
            <td>{{ roleSkillMatchPercentage[applicants.indexOf(application)] }}</td>
            <td>{{ application.Time_Stamp }}</td>
          </tr>
        </tbody>

      </table>
        <!-- <ul>
          <li v-for="application in applicants">{{ application.Staff_Name }}</li>
        </ul> -->
      </span>

    </div>
  </main>
</template>
  
<script>
export default {
  data() {
    return {
      role: null,
      applicants: [],
      info: {},
      dt: null,
      applicantCount: 0,
      roleSkillMatchPercentage: [],
    };
  },
  props: ['Role_Listing_ID'],
  async mounted() {
    this.dt = $(this.$refs.rolesTable).DataTable();
    await this.fetchRoleData();
    this.getRoleName();
    this.getApplicants();
    this.getRoleSkillMatchPercentage();
  },
  watch: {
    applicants() {
      if (this.dt) {
        this.dt.destroy();
      }
      this.$nextTick(() => {
        new DataTable('#applicantsTable')
      });
    },
  },
  methods: {
    fetchRoleData() {
      fetch('http://localhost:5000/api/roles/' + this.Role_Listing_ID)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.role = data.data;

          // Set Role_ID to a data property for later use
          this.Role_ID = data.data.Role_ID;

          // console.log("role id for current role listing id:" + this.Role_ID)
          // console.log(data);

          this.getRoleName(); // Call getRoleName after setting Role_ID
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    getRoleName() {
      fetch('http://localhost:5000/api/get-roles-info/' + this.Role_ID) // use the Role_ID of current Role_Listing_ID
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.info = data;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    getApplicants(){
      fetch('http://localhost:5000/api/applications/rolelisting/' + this.Role_Listing_ID)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.applicants = data.data.applications;
          this.applicantCount = this.applicants.length;

          // console.log("All Applicants for this role")
          // console.log(data);
          this.getRoleSkillMatchPercentage();
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },

    async getRoleSkillMatchPercentage() {
  if (this.applicants && this.applicants.length > 0) {
    this.roleSkillMatchPercentage = []; // Initialize the array

    for (const application of this.applicants) {
      const roleID = this.Role_ID;
      const staffID = application.Staff_ID;

      try {
        const response = await fetch('http://localhost:5000/api/calc_rsm/' + roleID + '/' + staffID);
        if (response.status === 200) {
          const data = await response.json();
          this.roleSkillMatchPercentage.push(data.role_skill_match_percentage);
        } else {
          console.error('Error with RSM%:', response.status);
          this.roleSkillMatchPercentage.push(0); // Handle the error
        }
      } catch (error) {
        console.error('Error with RSM%:', error);
        this.roleSkillMatchPercentage.push(0); // Handle the error
      }
    }
  }
}
  },
};
</script>

