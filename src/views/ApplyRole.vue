<template>
    <div>
      <h2>Apply for Role</h2>
      <form @submit.prevent="submitApplication">
        <label for="staffId">Staff ID:</label>
        <input type="text" id="staffId" v-model="staffId" required>
        <br>
        <br>
        <label for="roleListingId">Role Listing ID:</label>
        <input type="text" id="roleListingId" v-model="roleListingId" required>
        <br>
        <br>
        <button type="submit">Apply</button>
      </form>
    </div>
</template>


<script>
  export default {
    data() {
      return {
        staffId: "",
        roleListingId: "",
      };
    },
    methods: {
      submitApplication() {
        const formData = {
          Staff_ID: this.staffId,
          Role_Listing_ID: this.roleListingId,
        };
  
        fetch("http://localhost:5173/api/apply-role", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        })
          .then((response) => {
            if (response.ok) {
              return response.json();
            } else {
              throw new Error("Failed to apply for the role");
            }
          })
          .then((data) => {
            console.log("Role applied successfully:", data);
            // Reset the form fields if needed
            this.staffId = "";
            this.roleListingId = "";
          })
          .catch((error) => {
            console.error("Error applying for the role:", error);
          });
      },
    },
  };
</script>
  