<template>
    <div class="ProfileInfo">
        <h1>Profile</h1>
        <ul>
            <li>{{ user.Access_Rights }}</li>
            <li>{{ user.Country_ID }}</li>
            <li>{{ user.Department_ID }}</li>
            <li>{{ user.Email }}</li>
            <li>{{ user.Staff_FName }}</li>
            <li>{{ user.Staff_LName }}</li>
        </ul>
    </div>
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
                        this.getSkillInfo(skill.Skill_ID);
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