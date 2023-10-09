<template>
  <div>
    <h2>Update Skill Proficiency</h2>
    <form @submit.prevent="updateSkillProficiency">
      <div class="form-group">
        <label for="staffId">Staff ID:</label>
        <input type="text" id="staffId" v-model="staffId" />
      </div>
      <br>
      <div class="form-group">
        <label for="skillId">Skill ID:</label>
        <input type="text" id="skillId" v-model="skillId" />
      </div>
      <br>
      <div class="form-group">
        <label for="proficiency">Proficiency:</label>
        <select id="proficiency" v-model="proficiency">
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
export default {
  data() {
    return {
      staffId: "",
      skillId: "",
      proficiency: "",
    };
  },
  methods: {
    updateSkillProficiency() {
      const data = {
        Staff_ID: this.staffId,
        Skill_ID: this.skillId,
        Proficiency: this.proficiency,
      };

      fetch(`/api/update-skill-proficiency/${this.staffId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response failed");
          }
          return response.json();
        })
        .then((responseJson) => {
          // Handle success, e.g., show a success message
          console.log("Skill proficiency updated successfully!");
        })
        .catch((error) => {
          // Handle error, e.g., show an error message
          console.error("Error updating skill proficiency:", error);
        });
    },
  },
};
</script>

<!-- <style scoped>
/* Add CSS styling here */
</style> -->

