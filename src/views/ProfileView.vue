<template>
    <div class="row align-items-start">
        <div class="ProfileInfo col">
            <img src="../assets/avatar-pic.jpg" class="rounded-circle" height="200" alt="" loading="lazy" />
            <h1>Profile</h1>

            <div class="mt-4 mb-4 col-sm-4"> 
            
            <table class="table">
                <tr>
                    <td class="fw-bold">Name: </td>
                    <td class="mt-4 mb-4">{{ user.Staff_FName }} {{ user.Staff_LName }}</td>
                </tr>
                <tr>
                    <td class="fw-bold">Email: </td>
                    <td class="mt-4 mb-4">{{ user.Email }}</td>
                </tr>
                <tr>
                    <td class="fw-bold">Country: </td>
                    <td class="mt-4 mb-4">{{ user.Country_ID }}</td>
                </tr>
                <tr>
                    <td class="fw-bold">Department: </td>
                    <td class="mt-4 mb-4">{{ user.Department_ID }}</td>
                </tr>
                <!-- We're not displaying access rights -->
                <!-- <tr>
                    <td class="fw-bold">Access Rights: </td>
                    <td class="mt-4 mb-4">{{ user.Access_Rights }}</td>
                </tr> -->

            </table>
            </div>
        </div>
    
    <div class="row">
    <h3>My Skills</h3>

    <div class="mt-2 mb-4 mx-auto">
    <table class="table table-bordered" style="width: 900px;" v-if="skills && skillNames">
        <thead class="table-primary thead-light">
            <tr>
                <th class="fw-bold">Skill ID</th>
                <th class="fw-bold">Skill Name</th>
                <!-- <th class="fw-bold">Skill Proficiency</th> -->
            </tr>
        </thead>
        <tbody>
        <tr class="my-4 py-4" v-for="(skills, index) in skills" v-bind:key="index">
            <td class="my-4 py-4">{{ skills.Skill_ID }}</td>
            <td class="my-4 py-4"> {{ skillNames[skills.Skill_ID] }}</td>
            <!-- <td class="my-4 py-4"> {{ skills.Proficiency }}</td> -->
        </tr>
        </tbody>
    </table>
    </div>
    </div>
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
        props: ['user_id'],
        mounted() {
            this.getUserInfo();
        },
    methods: {
        getUserInfo() {
            fetch(`http://localhost:5000/api/get-staff-info/` + this.user_id)
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
            fetch(`http://localhost:5000/api/get-staff-all-skill-id/`+ this.user_id)
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