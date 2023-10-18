<template>
  <!--Main layout-->
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

      <span v-if="role">
        <p><span class="fw-bold">Department:</span> {{ role.department_name }}</p>
        <p><span class="fw-bold">Expiry Date:</span> {{ role.Expiry_Date }}</p>
        <span class="fw-bold">Role Description:</span>
        <p> {{ role.Role_Listing_Desc }} </p>
        <!-- INSERT NUMBER OF AVAILABLE SLOTS FOR THE ROLE HERE -->
        <p><span class="fw-bold">Skills Required:</span> </p>
        <ul>
          <li v-for="skill in role.role_skills">{{ skill }}</li>
        </ul>
        <p><span class="fw-bold">Skills match:</span> Placeholder for which skills match OR skill match percentage.</p>
      </span>

    </div>
  </main>
</template>
  
<script>
import eventBus from '@/event-bus';

export default {
  data() {
    return {
      role: null,
      info: {}
    };
  },
  created() {
    // Access the staff_id from the event bus
    this.staffId = eventBus.getStaffId();
    console.log("current staff id:" + this.staffId)
  },
  props: ['Role_Listing_ID'],
  mounted() {
    this.fetchRoleData();
    this.getRoleName();
  },
  methods: {
    fetchRoleData() {
      if (!this.Role_Listing_ID) {
      console.error('Role_Listing_ID is not defined or valid');
      return;
  }
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
          console.error('Error 62:', error);
        });
    },
    getRoleName() {
      fetch('http://localhost:5000/api/get-roles-info/' + this.Role_ID) // use the Role_ID of current Role_Listing_ID
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.info = data;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    submitApplication() {
        const formData = {
          Staff_ID: this.staffId,
          Role_Listing_ID: this.Role_Listing_ID,
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
            
          })
          .catch((error) => {
            console.error("Error applying for the role:", error);
          });
      }
  },

};
</script>

