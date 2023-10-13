<template>
  <!--Main layout-->
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
          <input type="date" class="form-control" id="datepick">
        </section>

        <section class="box">
          <button type="button" class="btn btn-primary">Filter</button>
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
            <!-- <th>Applicants</th> -->
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
            <!-- <td>TBC NEXT SPRINT</td> -->
            <!-- For the percentage (Skill  Match) below, link up with <unassigned> to do SCRUM-29 Role Skill Match Percentage -->
            <td>Placeholder 69% (need to do! SCRUM-29)</td>
            <td>{{ role.Expiry_Date }}</td>
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
      selectedDepartments: null,
      selectedSkills: null,
      departments: [],
      skills: []
    };
  },
  mounted() {
    this.dt = $(this.$refs.rolesTable).DataTable();
    this.fetchRolesData();
    this.fetchDeptData();
    this.fetchSkillsData();


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
    fetchRolesData() {
      fetch('http://localhost:5000/api/roles') // Use the Flask route you defined
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.roles = data.data.roles;
          console.log(data)
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    fetchDeptData() {
      fetch('http://localhost:5000/api/alldepartments') // Use the Flask route you defined
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          // Transform the data to the desired format
          this.departments = data.map((dept) => ({
            value: dept.Department_ID,
            text: dept.Department_Name,
          }));
          console.log(this.departments);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    fetchSkillsData() {
      fetch('http://localhost:5000/api/allskills') // Use the Flask route you defined
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          // Transform the data to the desired format
          this.skills = data.map((skill) => ({
            value: skill.Skill_ID,
            text: skill.Skill_Name,
          }));
          console.log(this.skills);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    
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
  