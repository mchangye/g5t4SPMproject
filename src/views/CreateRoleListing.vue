
<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container-flex">
      <div class="row role-header mb-5">
        <div class="col">
          <h2>New Role Listing</h2>
        </div>

        <label for="Role_ID">Role:</label><br>

        <select v-model="Role_ID" required v-on:change="role_desc()">
          <option v-for="role in get_roles" :value="role.Role_ID">{{ role.Role_Name }}</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="role_description">Role Description:</label><br>
        <textarea id="role_description" name="role_description" rows="4" cols="50" required v-model="Role_Description"></textarea><br><br>

        <label for="skills_required">Skills Required:</label><br>

        <select id="skills_required" name="skills_required[]" v-model="Skills_Required" multiple required>
            <option v-for="skill in get_skills" :value="skill.Skill_ID">{{ skill.Skill_Name }}</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <div v-for="i in Skills_Required">
          The proficency level for skill {{ get_skills[i-1].Skill_Name }} is: <input v-bind:id=i type="number" name=""> <br>
        </div>

        <label for="Available">Available:</label><br>

        <input type="number" name="" id="" v-model="Available">

        <label for="Role_country_ID">Role Country:</label><br>

        <select v-model="Role_country_ID" required>
            <option v-for="country in get_countries" :value="country.Country_ID">{{ country.Country_Name }}</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="Role_Department_ID">Role Department:</label><br>

        <select v-model="Role_Department_ID" required>
          <option v-for="department in get_departments" :value="department.Department_ID">{{ department.Department_Name }}</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="expiry_date">Expiry Date:</label>
        <input type="date" id="expiry_date" name="expiry_date" v-model="Expiry_Date" required><br><br>

        <button v-on:click="postListing()" v-bind:class="[button, theme, type, center, 'm-2']">Submit</button>

        
      </div>



    </div>
  </main>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      Name: '',
      Role_Description: '',
      Skills_Required: [],
      Expiry_Date: '',
      Available: 0,
      Role_country_ID: 0,
      Role_Department_ID: 0,
      Role_ID: 0,
      get_roles: [],
      get_skills: [],
      get_countries: [],
      get_departments: []
    };
  },
  props: ['Role_Listing_ID'],
  mounted() {
    axios.get('http://localhost:5000/api/get-roles-info')
      .then(response => {
        this.get_roles = response.data;
        console.log(this.get_roles);
        console.log(this.get_roles[1].Role_Name)
      })
      .catch(error => {
        console.log(error.message);
      });

    axios.get('http://localhost:5000/api/allskills')
      .then(response => {
          this.get_skills = response.data;
          console.log(this.get_skills);
        })
        .catch(error => {
          console.log(error.message);
        });

    axios.get('http://localhost:5000/api/allcountries')
      .then(response => {
          this.get_countries = response.data;
          console.log(this.get_countries);
        })
        .catch(error => {
          console.log(error.message);
        });

    axios.get('http://localhost:5000/api/alldepartments')
      .then(response => {
          this.get_departments = response.data;
          console.log(this.get_departments);
        })
        .catch(error => {
          console.log(error.message);
        });

  },
  methods: {
    postListing() {
      
      let skill_pro = []
      console.log(this.Role_Description);
      console.log(this.Skills_Required);
      console.log(this.Expiry_Date);
      console.log(this.Available);
      console.log(this.Role_country_ID);
      console.log(this.Role_Department_ID);
      for (let i = 0; i < this.Skills_Required.length; i++) {
        console.log("Hi" + typeof(this.Skills_Required[i]))
        skill_pro.push(document.getElementById(this.Skills_Required[i]).value)
      }
      console.log(skill_pro)
      axios.post('http://localhost:5000/api/createrole', {
          Available: this.Available,
          Expiry_Date: this.Expiry_Date,
          Role_Country_ID: this.Role_country_ID,
          Role_Listing_Desc: this.Role_Description,
          Role_ID: this.Role_ID,
          Role_department_ID: this.Role_Department_ID,
          Skills_Required: this.Skills_Required,
          skill_pro: skill_pro
      })
          .then(response => {
              console.log(response.data);
          })
          .catch( error => {
              console.log(error.message);
          });
    },
    role_desc() {
      console.log(this.Role_ID)
      this.Role_Description = this.get_roles[this.Role_ID - 1].Role_Desc
    }
  },

};
</script>

