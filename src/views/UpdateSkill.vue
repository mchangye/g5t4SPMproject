<template>
  <div>
    <h2>Update Skill Proficiency</h2>
    <form @submit.prevent="updateSkillProficiency">
      <div class="form-group">
        <label for="Staff_ID">Staff ID: {{staffId}}</label>
      </div>
      <br>
      <div class="form-group">
        <label for="Skill_ID">Skill ID:</label>
        <input type="text" id="Skill_ID" v-model="Skill_ID" />
      </div>
      <br>
      <div class="form-group">
        <label for="Proficiency">Proficiency:</label>
        <select id="Proficiency" v-model="Proficiency">
          <option value="1">Beginner</option>
          <option value="2">Intermediate</option>
          <option value="3">Advanced</option>
          <option value="4">Expert</option>
        </select>
      </div>
      <br>
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import eventBus from '@/event-bus';
import axios from 'axios';
export default {
  data() {
    return {
      Staff_ID: "",
      Skill_ID: "",
      Proficiency: "",
    };
  },
  created() {
    // Access the staff_id from the event bus
    this.staffId = eventBus.getStaffId();
    console.log("current staff id:" + this.staffId)
  },
  methods: {
    updateSkillProficiency() {
      console.log(this.staffId)
      const data = {
        Staff_ID: this.Staff_ID,
        Skill_ID: this.Skill_ID,
        Proficiency: this.Proficiency,
      };
      console.log(this.Skill_ID)
      console.log(this.Proficiency)
      axios.put('http://localhost:5000/api/update-skill-proficiency/'+ this.staffId,{
          Staff_ID: this.staffId,
          Skill_ID: this.Skill_ID,
          Proficiency:this.Proficiency
      })
          .then(response => {
              console.log(response.data);
              alert("Skill Update is successful")

          })
          .catch( error => {
              // console.log(error.response.data.message);
              // alert(error.response.data.message);
              console.log(error);
              // alert(error.response.data.message);
          });
    },
  },
};
</script>

<!-- <style scoped>
/* Add CSS styling here */
</style> -->

