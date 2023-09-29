<template>

  <div class="staffinfo">
      <h1>Staff Information</h1>
      <input type="text" placeholder="Enter an ID to search" id="user_staff_id_search" v-model="user_staff_id_search" @keydown.enter="sendUserStaffIDSearch"/>
      <!-- keydown enter means I can search using the Enter Key. -->
      <button type="button" v-on:click="sendUserStaffIDSearch()">Search</button>
      <!-- But this button is also for better user clarity in case they dont use enter key. -->
      <ul v-if="staff">
        <li><strong>Staff First Name:</strong> {{ staff.Staff_FName }}</li>
        <li><strong>Staff Last Name:</strong> {{ staff.Staff_LName }}</li>
        <li><strong>Department ID:</strong> {{ staff.Department_ID }}</li>
        <li><strong>Country ID:</strong> {{ staff.Country_ID }}</li>
        <li><strong>Email:</strong> {{ staff.Email }}</li>
        <li><strong>Access Rights:</strong> {{ staff.Access_Rights }}</li>
      </ul>
    
      <ul v-if="skills && skills.length">
        <li v-for="(skill,index) in skills" :key="index">
          <strong>Skill ID:</strong> {{ skill.Skill_ID }} <br>
          <strong>Skill Name:</strong>
            <span v-if="skillNames[skill.Skill_ID]">{{ skillNames[skill.Skill_ID] }}</span>
            <span v-else>Loading Skill Name...</span> <br>
            <!-- <br> -->
          <strong>Proficiency:</strong> {{ skill.Proficiency }}
        </li>
      </ul>
      </div>
    
</template>

<script>
export default {
  data() {
    return {
      staff: null,
      skills: null,
      skillNames: {},
      user_staff_id_search: null, //can change from null to any number if you want to show a person's detail first before searching
    };
  },
  methods: {
    sendUserStaffIDSearch() {
      console.log("value:", this.user_staff_id_search)
      this.getStaffInfoAPI();
      // this.getStaffAllSkillIDAPI();
      // this.getSkillInfoAPI();
    },
    getStaffInfoAPI() {
      fetch(`http://localhost:5000/api/get-staff-info/` + this.user_staff_id_search)
        .then((response) => {
        if (!response.ok) {
          throw new Error('Network response failed');
        }
        // console.log(this.data);
        return response.json();
      })
      .then((data) => {
        this.staff = data;
        console.log('Data from getStaffInfoAPI:' + this.staff);
        this.getStaffAllSkillIDAPI();
      })
      .catch((error) => {
        console.error('There was a problem with the getStaffInfoAPI fetch operation:', error);
      });
    },
    getStaffAllSkillIDAPI() {
      fetch(`http://localhost:5000/api/get-staff-all-skill-id/` + this.user_staff_id_search)
        .then((response) => {
        if (!response.ok) {
          throw new Error('Network response failed');
        }
        // console.log(this.data);
        return response.json();
      })
      .then((data) => {
        this.skills = data;
        console.log('Data from getStaffAllSkillIDAPI:' + this.skills);
        this.skills.forEach((skill) => {
          this.getSkillName(skill.Skill_ID);
        });
      })
      .catch((error) => {
        console.error('There was a problem with the getStaffAllSkillIDAPI fetch operation:', error);
      });
    },
    getSkillName(skill_id) {
      if (this.skillNames[skill_id]) {
        return this.skillNames[skill_id];
      } else {
        return fetch(`http://localhost:5000/api/get-skill-info/${skill_id}`)
        .then((response) => {
        if (!response.ok) {
          throw new Error('Network response failed');
        }
        console.log(this.data);
        return response.json();
      })
      .then((data) => {
        this.skillNames[skill_id] = data.Skill_Name;
        console.log('Data from getSkillName:' + data.Skill_Name);
        return data.Skill_Name;
      })
      .catch((error) => {
        console.error(`There was a problem fetching skill name using getSkillName function for Skill_ID ${skill_id}:`, error);
        return "No Skill Name Found";
      });
      }
    },
    // getSkillNamesByIDs(skill_ids) {
    //   fetch('http://localhost:5000/api/get-skill-info/', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify(skill_ids),
    //   })
    //     .then((response) => {
    //       if (!response.ok) {
    //         throw new Error('Network response failed');
    //       }
    //       return response.json();
    //     })
    //     .then((data) => {
    //       this.skillNames = data;
    //     })
    //     .catch((error) => {
    //       console.error('There was a problem with the getSkillNamesByIDs fetch operation:', error);
    //     });
    //   },
    },

  created() {

    this.sendUserStaffIDSearch();

    // fetch(`http://localhost:5000/api/get-staff-info/` + this.user_staff_id_search)
    // // fetch('http://localhost:5000/api/get-staff-info/1')
    // .then((response) => {
    //   if (!response.ok) {
    //     throw new Error('Network response failed');
    //   }
    //   console.log(this.data);
    //   return response.json();
    // })
    // .then((data) => {
    //   this.staff = data;
    //   console.log(this.staff);
    // })
    // .catch((error) => {
    //   console.error('There was a problem with the fetch operation:', error);
    // });
  },
};
</script>

<style scoped>
@media (min-width: 1024px) {
  .staffinfo {
    min-height: 100vh;
    align-items: top;
  }
}
</style>
