<template>
  <main class="pt-3">
    <div class="container-flex">
      <h2>Browse Roles (Staff)</h2>

      <div class="filters-container mt-4 mb-4">
        <section class="box">
          <p class="fw-bold">Department</p>
          <vue-multiselect v-model="selectedDepartments" :options="departments" :multiple="true" :close-on-select="false"
            placeholder="Select Department(s)" label="text" track-by="value"></vue-multiselect>
        </section>

        <section class="box">
          <p class="fw-bold">Skills</p>
          <vue-multiselect v-model="selectedSkills" :options="skills" :multiple="true" :close-on-select="false"
            placeholder="Select Skill(s)" label="text" track-by="value"></vue-multiselect>
        </section>

        <section class="box">
          <p class="fw-bold">Expiry Date</p>
          <input ref="expiryDate" type="date" class="form-control" id="datepick">
        </section>

        <section class="box">
          <button type="button" class="btn btn-primary" @click="applyFilters">Filter</button>
        </section>

      </div>

      <table id="rolesTable" class="table table-striped" style="width:100%">
        <thead>
          <tr>
            <th>Role Listing ID</th>
            <th>Role Name</th>
            <th>Department</th>
            <th>Description</th>
            <th>Skills</th>
            <th>Role Skill Match Percentage</th>
            <th>Expiry Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="role in roles" :key="role.Role_Listing_ID">
            <td>{{ role.Role_Listing_ID }}</td>
            <td>
              <router-link :to="'/rolestaff/' + role.Role_Listing_ID">{{ role.Role_Name }}</router-link>
            </td>
            <td>{{ role.Department_Name }}</td>
            <td>{{ role.Role_Listing_Desc }}</td>
            <td>
              <ul>
                <li v-for="skill in role.role_skills">{{ skill }}</li>
              </ul>
            </td>
            <td>{{ role.role_skill_match_percentage }}</td>
            <td>{{ formatExpiryDate(role.Expiry_Date) }}</td>
          </tr>
        </tbody>

      </table>
    </div>
  </main>
</template>
  
<script>
import eventBus from '@/event-bus';
import VueMultiselect from 'vue-multiselect'

export default {
  components: { 
    VueMultiselect 
  },
  data() {
    return {
      roles: [],
      dt: null,
      selectedDepartments: [],
      selectedSkills: [],
      departments: [],
      skills: [],
    };
  },
  mounted() {
    this.dt = $(this.$refs.rolesTable).DataTable();
    this.fetchRolesData();
    this.fetchDeptData();
    this.fetchSkillsData();
    this.getRoleSkillMatchPercentageForRoles();
    // this.getRoleSkillMatchPercentage(1);
  },
  created() {
    // Access the staff_id from the event bus
    this.staffId = eventBus.getStaffId();
    console.log("current staff id:" + this.staffId)
  },
  watch: {
    roles() {
      if (this.dt) {
        this.dt.destroy();
      }
      this.$nextTick(() => {
        new DataTable('#rolesTable')
      });
    },
  },
  methods: {
    // fetchRolesData() {
    //   fetch('http://localhost:5000/api/roles')
    //     .then((response) => {
    //       return response.json();
    //     })
    //     .then((data) => {
    //       // Only fetches Roles that have not expired
    //       const currentDate = new Date();
    //       this.roles = data.data.roles.filter((role) => {
    //         const expiryDate = new Date(role.Expiry_Date);
    //         return expiryDate > currentDate;
    //       });
    //       // console.log("Role Listings fetched: (fetchRolesData)",data)
    //     })
    //     .catch((error) => {
    //       console.error('Error:', error);
    //     });
    // 
    async fetchRolesData() {
      try {
        const response = await fetch('http://localhost:5000/api/roles');
        const data = await response.json();
        const currentDate = new Date();
        this.roles = data.data.roles.filter((role) => {
          const expiryDate = new Date(role.Expiry_Date);
          return expiryDate > currentDate;
        });
        console.log("Role Listings fetched: (fetchRolesData)",data)
        await this.getRoleSkillMatchPercentageForRoles();
      } catch (error) {
        console.error('Error fetching roles:', error);
    }
    },
    fetchDeptData() {
      fetch('http://localhost:5000/api/alldepartments')
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          // Transform the data to the desired format
          this.departments = data.map((dept) => ({
            value: dept.Department_ID,
            text: dept.Department_Name,
          }));
          // console.log(this.departments);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    fetchSkillsData() {
      fetch('http://localhost:5000/api/allskills')
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          // Transform the data to the desired format
          this.skills = data.map((skill) => ({
            value: skill.Skill_ID,
            text: skill.Skill_Name,
          }));
          // console.log(this.skills);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    applyFilters() {
      const selectedDepartments = this.selectedDepartments.map((dept) => dept.value);
      const selectedSkills = this.selectedSkills.map((skill) => skill.value);
      const selectedExpiryDate = this.$refs.expiryDate.value;

      // Convert the selected expiry date to ISO format
      let selectedDateISO = null;
      if (selectedExpiryDate) {
        const selectedDate = new Date(selectedExpiryDate);
        selectedDateISO = selectedDate.toISOString();
      }

      // Construct the query parameters
      const params = new URLSearchParams();

      // Include departments if there are selections
      if (selectedDepartments.length > 0) {
        selectedDepartments.forEach((dept) => {
          params.append('departments', dept);
        });
      }

      // Include skills if there are selections
      if (selectedSkills.length > 0) {
        selectedSkills.forEach((skill) => {
          params.append('skills', skill);
        });
      }

      // Include the expiry_date if a date is selected
      if (selectedDateISO) {
        params.append('expiry_date', selectedDateISO);
      }


      // Make the API request
      fetch(`http://localhost:5000/api/rolesFiltered?${params.toString()}`)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          if (data.message && data.message === "There are no roles.") {
            this.roles = []; // Set roles to an empty array

          } else {
            this.roles = data.data.roles;
          }
          // console.log(data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });

      // console.log("Selected Departments:", selectedDepartments)
      // console.log("Seleceted Skills:", selectedSkills)
      // console.log("Seleceted Expiry:", selectedDateISO)
      
    },
    formatExpiryDate(dateString) {
      if (!dateString) return'';
      const options = {
        weekday: 'short',
        year: 'numeric',
        month: 'short',
        day: '2-digit',
      };
      const formattedDate = new Date(dateString).toLocaleDateString('en-US',options);
      return formattedDate;
    },
    // GET RSM WORKS FOR NORMAL PAGE, NOT YET IMPLEMENTED FOR FILTERS. PROBABLY WITH HOW FILTERS ARE NOT ASYNC.
    async getRoleSkillMatchPercentage(roleID) {
      try {
        // console.log("roleID", roleID);
        // console.log("staffId", this.staffId);
        const response = await fetch('http://localhost:5000/api/calc_rsm/' + roleID + '/' + this.staffId);
        const data = await response.json();
        // console.log(data.role_skill_match_percentage);
        return data.role_skill_match_percentage;
      } catch (error) {
        console.error('Error fetching RSM%:', error);
      }
    },
    async getRoleSkillMatchPercentageForRoles() {
      for (const role of this.roles) {
        role.role_skill_match_percentage = await this.getRoleSkillMatchPercentage(role.Role_ID);
        console.log(`Role ${role.Role_Name}, ID ${role.Role_ID} - RSM%: ${role.role_skill_match_percentage}`)
      }
    }
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

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
  width: 500px;
}
</style>
  