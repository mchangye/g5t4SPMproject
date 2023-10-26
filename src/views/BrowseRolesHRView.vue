<template>
  <!--Main layout-->
  <main class="pt-3 centered-content">
    <div class="container-flex">
      <h2>Browse Roles (HR)</h2>

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
          <p class="fw-bold">Countries</p>
          <vue-multiselect v-model="selectedCountries" :options="countries" :multiple="true" :close-on-select="false"
            placeholder="Select Country(s)" label="text" track-by="value"></vue-multiselect>
        </section>

        <section class="box">
          <p class="fw-bold">Expiry Date</p>
          <input ref="expiryDate" type="date" class="form-control" id="datepick">
        </section>

        <section class="box mt-3">
          <button type="button" class="btn btn-primary" @click="applyFilters">Filter</button>
        </section>


      </div>

      <table id="rolesTable" class="table table-striped" style="width:100%">
        <thead>
          <tr>
            <th>Role Listing ID</th>
            <th>Role Name</th>
            <th>Department</th>
            <th>Country</th>
            <th>Description</th>
            <th>Skills</th>
            <th>Applicants</th>
            <th>Expiry Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="role in roles" :key="role.Role_Listing_ID">
            <td>{{ role.Role_Listing_ID }}</td>
            <td>
              <router-link :to="'/rolehr/' + role.Role_Listing_ID">{{ role.Role_Name }}</router-link>
            </td>
            <td>{{ role.Department_Name }}</td>
            <td>{{ role.Country }}</td>
            <td>{{ role.Role_Listing_Desc }}</td>
            <td>
              <ul>
                <li v-for="skill in role.role_skills">{{ skill }}</li>
              </ul>
            </td>
            <td>TBC NEXT SPRINT</td>
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
      selectedCountries: [],
      departments: [],
      skills: [],
      countries: []
    };
  },
  mounted() {
    this.dt = $(this.$refs.rolesTable).DataTable();
    this.fetchRolesData();
    this.fetchDeptData();
    this.fetchSkillsData();
    this.fetchCountriesData();


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
    fetchCountriesData() {
      fetch('http://localhost:5000/api/allcountries') // Use the Flask route you defined
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          // Transform the data to the desired format
          this.countries = data.map((country) => ({
            value: country.Country_ID,
            text: country.Country_Name,
          }));
          console.log(this.countries);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    applyFilters() {
      const selectedDepartments = this.selectedDepartments.map((dept) => dept.value);
      const selectedSkills = this.selectedSkills.map((skill) => skill.value);
      const selectedCountries = this.selectedCountries.map((country) => country.value);
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

      // Include countries if there are selections
      if (selectedCountries.length > 0) {
        selectedCountries.forEach((country) => {
          params.append('countries', country);
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
          console.log(data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });

      console.log("Selected Departments:", selectedDepartments)
      console.log("Seleceted Skills:", selectedSkills)
      console.log("Seleceted Expiry:", selectedDateISO)
      console.log("the params:", params.toString())
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
  padding: 5px;
  /* Optional: Add padding for spacing */
  width: 50%;
}
</style>
  