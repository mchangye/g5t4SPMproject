<template>
  <div>
    <h2>Update Skill Proficiency</h2>
    <form @submit.prevent="updateSkillProficiency">
      <div class="form-group">
        <label for="Staff_ID">Staff ID:</label>
        <input type="text" id="Staff_ID" v-model="Staff_ID" />
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
export default {
  data() {
    return {
      Staff_ID: "",
      Skill_ID: "",
      Proficiency: "",
    };
  },
  methods: {
    updateSkillProficiency() {
      const data = {
        Staff_ID: this.Staff_ID,
        Skill_ID: this.Skill_ID,
        Proficiency: this.Proficiency,
      };

      fetch(`/api/update-skill-proficiency/${this.Staff_ID}`, {
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

