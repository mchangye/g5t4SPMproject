<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container-flex">
      <h2>Browse Roles</h2>

      <div class="filters-container mt-4 mb-4">
        <section class="box">
          <p class="fw-bold">Department</p>
          <select id="department-filter" multiple="multiple">
            <option value="department1">Department 1</option>
            <option value="department2">Department 2</option>
            <option value="marketing">Marketing</option>
            <option value="operations">Operations</option>
          </select>
        </section>

        <section class="box">
          <p class="fw-bold">Skills</p>
          <select id="skill-filter" multiple="multiple">
            <option value="skill1">Skill 1</option>
            <option value="skill2">Skill 2</option>
            <option value="cleaning">Cleaning</option>
            <option value="stakeholder management">Stakeholder Management</option>
            <option value="business management">Business Management</option>
            <option value="brand management">Brand Management</option>
          </select>
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
            <th>Applicants</th>
            <th>Expiry Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="role in roles" :key="role.Role_Listing_ID">
            <td>{{ role.Role_Listing_ID }}</td>
            <td>
              <router-link :to="'/role/' + role.Role_Listing_ID">{{ role.Role_Name }}</router-link>
            </td>
            <td>{{ role.Department_Name }}</td>
            <td>{{ role.Role_Desc }}</td>
            <td>
              <ul>
                <li v-for="skill in role.role_skills">{{ skill }}</li>
              </ul>
            </td>
            <td>TBC NEXT SPRINT</td>
            <td>{{ role.Expiry_Date }}</td>
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
      roles: [],
      dt: null,
      deptfilter: null,
      skillsfilter: null
    };
  },
  mounted() {
    this.dt = $(this.$refs.rolesTable).DataTable();
    this.fetchRolesData();

    //Department Filter Multiselect Dropdown
    this.deptfilter = $('#department-filter').multiselect({
      buttonText: function (options, select) {
        if (options.length == 0) {
          return 'Select Department(s)';
        } else if (options.length > 3) {
          return 'More than 3 departments selected!';
        }
        else {
          var labels = [];
          options.each(function () {
            if ($(this).attr('label') !== undefined) {
              labels.push($(this).attr('label'));
            }
            else {
              labels.push($(this).html());
            }
          });
          return labels.join(', ') + '';
        }
      },
      includeSelectAllOption: true,
      enableFiltering: true,
      buttonWidth: '400px'
    });


    //Skills Multiselect Dropdown
    this.skillsfilter = $('#skill-filter').multiselect({
      buttonText: function (options, select) {
        if (options.length == 0) {
          return 'Select Skill(s)';
        } else if (options.length > 3) {
          return 'More than 3 skills selected!';
        }
        else {
          var labels = [];
          options.each(function () {
            if ($(this).attr('label') !== undefined) {
              labels.push($(this).attr('label'));
            }
            else {
              labels.push($(this).html());
            }
          });
          return labels.join(', ') + '';
        }
      },
      includeSelectAllOption: true,
      enableFiltering: true,
      buttonWidth: '400px'
    });


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
    // Add a watch on the route object and the "key" attribute.
    '$route'() {
      // Handle route changes or key changes here.
      this.reloadComponent();
    }
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
    reloadComponent() {
      // This method will be called when the route changes.
      // Reset component state or perform any necessary actions.
      this.dt.destroy();

      if (this.skillsfilter) {
        this.skillsfilter.multiselect('destroy');
      }
      if (this.deptfilter) {
        this.deptfilter.multiselect('destroy');
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
  