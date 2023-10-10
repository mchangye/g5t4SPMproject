
<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container-flex">
      <div class="row role-header mb-5">
        <div class="col">
          <h2>New Role Listing</h2>
        </div>

        <label for="role_description">Role Description:</label><br>
        <textarea id="role_description" name="role_description" rows="4" cols="50" required v-model="Role_Description"></textarea><br><br>

        <label for="skills_required">skills_required:</label><br>

        <select id="skills_required" name="skills_required[]" v-model="Skills_Required" multiple required>
            <option value=1>1</option>
            <option value=2>2</option>
            <option value=3>3</option>
            <option value=4>4</option>
            <option value=5>5</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <div v-for="i in Skills_Required">
          The proficency level for skill {{ i }} is: <input v-bind:id=i type="number" name=""> <br>
        </div>

        <label for="Available">Available:</label><br>

        <input type="number" name="" id="" v-model="Available">

        <label for="Role_country_ID">Role_country_ID:</label><br>

        <select v-model="Role_country_ID" required>
            <option value=1>Sg</option>
            <option value=2>My</option>
            <option value=3>Id</option>
            <option value=4>China</option>
            <option value=5>Japan</option>
            <option value=6>Hong Kong</option>
            <option value=7>India</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="Role_Function_ID">Role_Function_ID:</label><br>
        <select v-model="Role_Function_ID" required>
            <option value=1>IT</option>
            <option value=2>Bp</option>
            <option value=3>S</option>
            <option value=4>M</option>
            <option value=5>O</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="Role_ID">Role:</label><br>

        <select v-model="Role_ID" required>
          <option value=1>a</option>
            <option value=2>ae</option>
            <option value=3>cc</option>
            <option value=4>cd</option>
            <option value=5>c</option>
            <option value=6>d</option>
            <option value=7>ed</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="Role_Department_ID">Role Department:</label><br>

        <select v-model="Role_Department_ID" required>
          <option value=1>c</option>
            <option value=2>t</option>
            <option value=3>h</option>
            <option value=4>a</option>
            <option value=5>m</option>
            <option value=6>f</option>
            <option value=7>o</option>
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
      Role_Function_ID: 0,
      Role_Department_ID: 0,
      Role_ID: 0
    };
  },
  props: ['Role_Listing_ID'],
  mounted() {
  },
  methods: {
    postListing() {
      
      let skill_pro = []
      console.log(this.Role_Description);
      console.log(this.Skills_Required);
      console.log(this.Expiry_Date);
      console.log(this.Available);
      console.log(this.Role_country_ID);
      console.log(this.Role_Function_ID);
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
          Role_Function_ID: this.Role_Function_ID,
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
    }
  },

};
</script>

