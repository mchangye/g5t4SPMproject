<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container-flex">
      <div class="row role-header mb-5">
        <div class="col">
          <h2>New Role Listing</h2>
        </div>

        <label for="department">Department:</label>
        <input type="text" id="department" name="department" required v-model="Department"><br><br>

        <label for="role_description">Role Description:</label><br>
        <textarea id="role_description" name="role_description" rows="4" cols="50" required v-model="Role_Description"></textarea><br><br>

        <select id="skills_required" name="skills_required[]" v-model="Skills_Required" multiple required>
            <option value=1>1</option>
            <option value=2>2</option>
            <option value=3>3</option>
            <option value=4>4</option>
            <option value=5>5</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="Available">Available:</label><br>

        <input type="number" name="" id="" v-model="Available">

        <label for="Role_country_ID">Role_country_ID:</label><br>

        <select v-model="Role_country_ID" required>
            <option value="1">Sg</option>
            <option value="2">My</option>
            <option value="3">Id</option>
            <option value="4">China</option>
            <option value="5">Japan</option>
            <option value="6">Hong Kong</option>
            <option value="7">India</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="Role_Function_ID">Role_Function_ID:</label><br>
        <select v-model="Role_Function_ID" required>
            <option value="1">IT</option>
            <option value="2">Bp</option>
            <option value="3">S</option>
            <option value="4">M</option>
            <option value="5">O</option>
            <!-- Add more skills as needed -->
        </select><br><br>

        <label for="Role_Department_ID">Role Description:</label><br>

        <select v-model="Role_Department_ID" required>
          <option value="1">c</option>
            <option value="2">t</option>
            <option value="3">h</option>
            <option value="4">a</option>
            <option value="5">m</option>
            <option value="6">f</option>
            <option value="7">o</option>
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
export default {
  data() {
    return {
      Name: '',
      Department: '',
      Role_Description: '',
      Skills_Required: [],
      Expiry_Date: '',
      Available: 0,
      Role_country_ID: 0,
      Role_Function_ID: 0,
      Role_Department_ID: 0,
    };
  },
  props: ['Role_Listing_ID'],
  mounted() {
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

          console.log("role id for current role listing id:" + this.Role_ID)
          console.log(data);

          this.getRoleName(); // Call getRoleName after setting Role_ID
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    postListing() {
      console.log(this.Department);
      console.log(this.Role_Description);
      console.log(this.Skills_Required);
      console.log(this.Expiry_Date);
      console.log(this.Available);
      console.log(this.Role_country_ID);
      console.log(this.Role_Function_ID);
      console.log(this.Role_Department_ID);
      // axios.post('localhost:5000/api/createrole', {
      //     key:  value
      // })
      //     .then(response => {
      //         console.log(response.data);
      //     })
      //     .catch( error => {
      //         console.log(error.message);
      //     });
    }
  },

};
</script>

