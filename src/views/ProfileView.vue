<template>
    <div class="ProfileInfo">
        <img src="../assets/avatar-pic.jpg" class="rounded-circle" height="200" alt="" loading="lazy" />
        <h1>Profile</h1>
        <ul>
            <li>Access Rights: {{ user.Access_Rights }}</li>
            <li>Country: {{ user.Country_ID }}</li>
            <li>Department: {{ user.Department_ID }}</li>
            <li>Email: {{ user.Email }}</li>
            <li>First Name: {{ user.Staff_FName }}</li>
            <li>Last Name: {{ user.Staff_LName }}</li>
        </ul>
    </div>
    <h2>My Skills</h2>

    <table v-if="skills && skillNames">
        <tr>
            <th>Skill ID</th>
            <th>Skill Name</th>
        </tr>
        <tr v-for="(skills, index) in skills" v-bind:key="index">
            <td>{{ skills.Skill_ID }}</td>
            <td>{{ skillNames[skills.Skill_ID] }}</td>
        </tr>
    </table>
    
    <ul v-if="skills && skillNames">
        <li v-for="(skills, index) in skills" v-bind:key="index">
            
            Skill_ID: {{ skills.Skill_ID }} <br>
            Skill_Name: {{ skillNames[skills.Skill_ID] }} <br>
        </li>
    
    </ul>
</template>

<script>
    export default {
        data() {
            return {
                user: [],
                skills: [],
                skillNames: {},
            };
        },
        mounted() {
            this.getUserInfo();
        },
    methods: {
        getUserInfo() {
            fetch(`http://localhost:5000/api/get-staff-info/1`)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Network response failed');
                    }
                    return response.json();
                })
                .then((data) => {
                    this.user = data;
                    console.log('Data from getStaffInfoAPI:' + this.staff);
                    this.getUserSkills();
                })
                .catch((error) => {
                    console.error('There was a problem with the getStaffInfoAPI fetch operation:', error);
                });
        },
        getUserSkills() {
            fetch(`http://localhost:5000/api/get-staff-all-skill-id/1`)
                .then((response) => {
                    if (!response.ok) {
                        throw new Error('Network response failed');
                    }
                    return response.json();
                })
                .then((data) => {
                    this.skills = data;
                    console.log('Data from getStaffAllSkillIDAPI:' + this.skills);
                    this.skills.forEach(skill => {
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
    }
    };

</script>