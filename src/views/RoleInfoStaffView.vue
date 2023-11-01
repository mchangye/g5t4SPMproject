<template>
  <main class="pt-3">
    <div class="container-flex">
      <div class="row role-header mb-5">
        <div class="col">
          <h2>{{ info.Role_Name }}</h2>
        </div>
        <div class="col">
          <button @click="submitApplication" type="button" class="btn btn-primary me-2">Apply</button>
        </div>  
      </div>
      <div v-if="role">
        <div class="row">
          <div class="col">
            <p><span class="fw-bold">Department:</span> {{ role.department_name }}</p>
            <p><span class="fw-bold">Expiry Date:</span> {{ formatExpiryDate(role.Expiry_Date) }}</p>
          </div>
          <div class="col">
            <p><span class="fw-bold">RSM%:</span> {{ RSMPercentage }} </p>
          </div>
        </div>
        <div class="row">
          <span class="fw-bold">Role Description:</span>
            <p> {{ role.Role_Listing_Desc }} </p>
        </div>
        <div class="row">
          <div class="col">
            <p><span class="fw-bold">Skills Required:</span> </p>
              <li v-for="skill in role.role_skills">{{ skill }}</li>
          </div>
          <div class="col">
            <p><span class="fw-bold">Skills you are missing:</span> </p>
            <li v-for="missingSkill in missingSkills">{{ missingSkill }}</li>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
  
<script>
import eventBus from '@/event-bus';
import axios from 'axios';
export default {
  data() {
    return {
      role: null,
      info: {},
      skills: [],
      skillNames: {},
      missingSkills: [],
      RSMPercentage: null,
    };
  },
  created() {
    // Access the staff_id from the event bus
    this.staffId = eventBus.getStaffId();
    console.log("current staff id:" + this.staffId)
  },
  props: ['Role_Listing_ID'],
  async mounted() {
    await this.fetchRoleData();
    this.getRoleName();
    this.getUserSkills();
    this.findMissingSkills();
    this.calculateMatchPercentage();
  },
  methods: {
    async fetchRoleData() {
      if (!this.Role_Listing_ID) {
        console.error('Role_Listing_ID is not defined or valid');
        return;
      }
      try {
        const response = await fetch('http://localhost:5000/api/roles/' + this.Role_Listing_ID);
        const data = await response.json();
        this.role = data.data;
        this.Role_ID = data.data.Role_ID;
        this.role_skills = data.data.role_skills;
        console.log("role id for current role listing id:" + this.Role_ID)
        await this.getRoleName(); // Call getRoleName after setting Role_ID
      } catch (error) {
        console.error('Error fetchRoleData():', error);
      }
    },
    async getRoleName() {
      try {
        const response = await fetch('http://localhost:5000/api/get-roles-info/' + this.Role_ID);
        const data = await response.json();
        this.info = data;
      } catch (error) {
        console.error('Error getRoleName():', error);
      }
    },
    async getUserSkills() {
      try {
        const response = await fetch(`http://localhost:5000/api/get-staff-all-skill-id/`+ this.staffId);
        if (!response.ok) {
          throw new Error('Network response failed');
        }
        const data = await response.json();
        this.skills = data;
        console.log('initialised getUserSkills()');
        for (const skill of this.skills) {
          await this.getSkillName(skill.Skill_ID);
        }
        this.findMissingSkills();
      } catch (error) {
        console.error('There was a problem with the getStaffAllSkillIDAPI fetch operation:', error);
      }
    },
    async getSkillName(skill_id) {
      if (this.skillNames[skill_id]) {
        return this.skillNames[skill_id];
      } else {
        try {
          const response = await fetch(`http://localhost:5000/api/get-skill-info/${skill_id}`);
          if (!response.ok) {
            throw new Error('Network response failed');
          }
          const data = await response.json();
          this.skillNames[skill_id] = data.Skill_Name;
          console.log('Data from getSkillName:' + data.Skill_Name);
          return data.Skill_Name;
        } catch (error) {
          console.error(`There was a problem fetching skill name using getSkillName function for Skill_ID ${skill_id}:`, error);
          return "No Skill Name Found";
        }
      }
    },
    async findMissingSkills() {
      console.log('findMissingSkills initialized');
      if (this.role && this.role.role_skills && this.skills) {
        const roleSkills = this.role.role_skills;
        const staffSkills = this.skills.map(skill => this.skillNames[skill.Skill_ID]); // Get skill names from skill IDs using this.skillNames
        console.log('Role Skills:', roleSkills);
        console.log('Staff Skills:', staffSkills);

        // Use filter to find the skills that the user doesn't have
        const missingSkills = roleSkills.filter(roleSkill => !staffSkills.includes(roleSkill));

        // Update your data property with missing skills
        this.missingSkills = missingSkills;
        console.log('findMissingSkills missingSkills', missingSkills);
      }
    },
    async getRoleSkillMatchPercentage() {
      try {
        console.log('testtesttestroleID',this.Role_ID);
        console.log('testtestteststaffID',this.staffId);
        const response = await fetch('http://localhost:5000/api/calc_rsm/' + this.Role_ID + '/' + this.staffId);
        const data = await response.json();
        console.log('testtesttestroleID',this.Role_ID);
        console.log('testtestteststaffID',this.staffId);
        console.log(data.role_skill_match_percentage);
        return data.role_skill_match_percentage;
      } catch (error) {
        console.error('Error fetching RSM%:', error);
      }
    },
    async calculateMatchPercentage() {
      try {
        const percentage = await this.getRoleSkillMatchPercentage();
        this.RSMPercentage = percentage;
        console.log('RSMPercentage:', this.RSMPercentage);
      } catch (error) {
        console.error('Error calculating RSM percentage:', error);
      }
    },
    async submitApplication() {
      console.log(this.staffId)
      console.log(this.Role_Listing_ID)
      try {
        const response = await axios.post('http://localhost:5000/api/apply-role', {
          Staff_ID: this.staffId,
          Role_Listing_ID: this.Role_Listing_ID,
        });
        console.log(response.data);
        alert("Role application is successful");
      } catch (error) {
        console.log(error.response.data.message);
        alert(error.response.data.message);
      }
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