<template>
  <!--Main layout-->
  <main class="pt-3">
    <div class="container ms-1">
      <div class="mb-5">
        <div class="row">
          <div class="col-5">
            <h2>Update Role Listing</h2>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <label for="Role_ID"
              ><p id="role" class="fw-bold mb-0 mt-3">Role</p></label
            ><br />

            <select v-model="Role_ID" v-on:change="role_desc()" required>
              <option v-for="role in get_roles" :value="role.Role_ID">
                {{ role.Role_Name }}
              </option>
              <!-- Add more skills as needed -->
            </select>
          </div>
          <div v-if="role_check == 1">
            <p style="color: red">Please select a role</p>
          </div>
        </div>

        <div class="row">
          <label for="role_description"
            ><p id="description" class="fw-bold mb-0 mt-3">
              Role Description
            </p></label
          ><br />
          <textarea
            id="role_description"
            name="role_description"
            rows="4"
            cols="50"
            required
            v-model="Role_Description"
          >
          </textarea>
          <div v-if="decription_check == 1">
            <p style="color: red">Please enter a description</p>
          </div>
        </div>

        <!-- <label for="skills_required">Skills Required:</label><br /> -->

        <!-- <select id="skills_required" name="skills_required[]" v-model="Skills_Required" multiple required>
            <option v-for="skill in get_skills" :value="skill.Skill_ID">{{ skill.Skill_Name }}</option> -->
        <!-- Add more skills as needed -->
        <!-- </select><br><br> -->

        <div class="row">
          <div class="col">
            <section class="box">
              <p id="skills" class="fw-bold mb-0 mt-3">Skills</p>
              <vue-multiselect
                v-model="Skills_Required"
                :options="get_skills"
                :multiple="true"
                :max="8"
                :close-on-select="false"
                placeholder="Select Skill(s)"
                label="Skill_Name"
                track-by="Skill_ID"
              ></vue-multiselect>
            </section>
            <div v-if="skills_check == 1">
              <p style="color: red">Please select skill(s) for the role</p>
            </div>
          </div>

          <div class="col">
            <div v-for="(i, index) in Skills_Required">
              <p :id="index + 't'" class="fw-bold mb-0 mt-3">
                The proficiency level for skill
                {{ get_skills[i.Skill_ID - 1].Skill_Name }} is:
              </p>
              <input
                min="1"
                max="4"
                v-bind:id="i.Skill_ID"
                type="number"
                name=""
              />
              <br />
            </div>
            <br /><br />
            <div v-if="required_check == 1">
              <p style="color: red">
                Please enter all the skills' proficiency level
              </p>
            </div>
            <div v-if="required_check == 2">
              <p style="color: red">
                Skills' proficiency level should be between 1 and 4
              </p>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <label for="Available"
              ><p id="available" class="fw-bold mb-0 mt-3">
                Available position(s)
              </p></label
            ><br />
            <input min="1" type="number" name="" id="" v-model="Available" />
            <div v-if="available_check == 1">
              <p style="color: red">
                Please enter the number of available positions
              </p>
            </div>
            <div v-if="available_check == 2">
              <p style="color: red">
                Available number of available positions should not be less than
                1
              </p>
            </div>
          </div>

          <div class="col">
            <label for="Role_country_ID"
              ><p id="country" class="fw-bold mb-0 mt-3">Role Country</p></label
            ><br />

            <select v-model="Role_country_ID" required>
              <option
                v-for="country in get_countries"
                :value="country.Country_ID"
              >
                {{ country.Country_Name }}
              </option>
              <!-- Add more skills as needed -->
            </select>
            <div v-if="country_check == 1">
              <p style="color: red">Please select a country</p>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <label for="Role_Department_ID"
              ><p id="department" class="fw-bold mb-0 mt-3">
                Role Department
              </p></label
            ><br />
            <select v-model="Role_Department_ID" required>
              <option
                v-for="department in get_departments"
                :value="department.Department_ID"
              >
                {{ department.Department_Name }}
              </option>
              <!-- Add more skills as needed -->
            </select>
            <div v-if="department_check == 1">
              <p style="color: red">Please select a department</p>
            </div>
          </div>

          <div class="col">
            <label for="expiry_date"
              ><p id="date" class="fw-bold mb-0 mt-3">Expiry Date</p></label
            ><br />
            <input
              type="date"
              id="expiry_date"
              name="expiry_date"
              v-model="Expiry_Date"
              required
            />
            <div v-if="date_check == 1">
              <p style="color: red">Please enter a valid expiry date.</p>
            </div>
            <div v-if="date_check == 2">
              <p style="color: red">
                Please check if the expiry date is before today's date.
              </p>
            </div>
          </div>
        </div>

        <!-- <button
          v-on:click="postListing()"
          v-bind:class="['m-2']"
        >
          Submit
        </button> -->

        <button
          type="button"
          v-on:click="postListing()"
          class="btn btn-primary"
        >
          Update
        </button>
      </div>
    </div>
  </main>
</template>
<script>
import axios from "axios";
import VueMultiselect from "vue-multiselect";
export default {
  components: {
    VueMultiselect,
  },
  data() {
    return {
      Name: "",
      Role_Description: "",
      Skills_Required: [],
      Expiry_Date: "",
      Available: 0,
      Role_country_ID: 0,
      Role_Department_ID: 0,
      Role_ID: 0,
      get_roles: [
        { Role_ID: 0, Role_Name: "Select a role", Role_Desc: "rherherhj" },
      ],
      get_skills: [],
      get_countries: [],
      get_departments: [],
      role_check: 0,
      decription_check: 0,
      skills_check: 0,
      required_check: 0,
      available_check: 0,
      country_check: 0,
      department_check: 0,
      date_check: 0,
      id: this.Role_Listing_ID,
      keep_orginal_skills: [],
      check_finish: 0,
    };
  },
  props: ["Role_Listing_ID"],
  mounted() {
    axios
      .get("http://localhost:5000/api/get-roles-info")
      .then((response) => {
        this.get_roles = response.data;
        console.log(this.get_roles);
        console.log(this.get_roles[1].Role_Name);
      })
      .catch((error) => {
        console.log(error.message);
      });

    axios
      .get("http://localhost:5000/api/allskills")
      .then((response) => {
        this.get_skills = response.data;
        console.log(this.get_skills);
      })
      .catch((error) => {
        console.log(error.message);
      });

    axios
      .get("http://localhost:5000/api/allcountries")
      .then((response) => {
        this.get_countries = response.data;
        console.log(this.get_countries);
      })
      .catch((error) => {
        console.log(error.message);
      });

    axios
      .get("http://localhost:5000/api/alldepartments")
      .then((response) => {
        this.get_departments = response.data;
        console.log(this.get_departments);
      })
      .catch((error) => {
        console.log(error.message);
      });

    axios
      .get("http://localhost:5000/api/roles/" + this.Role_Listing_ID)
      .then((response1) => {
        console.log(response1.data);
        let con_date = {
          Jan: "01",
          Feb: "02",
          Mar: "03",
          Apr: "04",
          May: "05",
          Jun: "06",
          Jul: "07",
          Aug: "08",
          Sep: "09",
          Oct: "10",
          Nov: "11",
          Dec: "12",
        };
        this.Role_ID = response1.data.data.Role_ID;
        this.Role_Description = response1.data.data.Role_Listing_Desc;

        for (let i = 0; i < response1.data.data.role_skills.length; i++) {
          for (let j = 0; j < this.get_skills.length; j++) {
            if (
              response1.data.data.role_skills[i] ==
              this.get_skills[j].Skill_Name
            ) {
              this.Skills_Required.push(this.get_skills[j]);
            }
          }
        }

        this.keep_orginal_skills = response1.data.data.skills_proficiency;

        console.log(this.Skills_Required);
        //this.Skills_Required = response1.data.data.role_skills;
        let res_date_full = response1.data.data.Expiry_Date.split(" ");
        this.Expiry_Date =
          res_date_full[3] +
          "-" +
          con_date[res_date_full[2]] +
          "-" +
          res_date_full[1];
        this.Available = response1.data.data.Available;
        this.Role_country_ID = response1.data.data.Role_Country_ID;
        this.Role_Department_ID = response1.data.data.Role_department_ID;

        console.log(response1.data.data.skills_proficiency);

        // while(document.getElementById(1) == null) {
        //   console.log("hi")
        // }

        setTimeout(function () {
          for (
            let i = 0;
            i < response1.data.data.skills_proficiency.length;
            i++
          ) {
            document.getElementById(response1.data.data.skills_proficiency[i].Skill_ID).value =
              response1.data.data.skills_proficiency[i].Proficienct_Listing;
          }
        }, 2000);
      })
      .catch((error) => {
        console.log(error.message);
      });
  },
  methods: {
    postListing() {
      // this.role_check = 0;
      // this.decription_check = 0;
      // this.skills_check = 0;
      this.required_check = 0;
      // this.available_check = 0;
      // this.country_check = 0;
      // this.department_check = 0;
      // this.date_check = 0;
      // document.getElementById('role').style = "";
      // document.getElementById('description').style = "";
      // document.getElementById('skills').style = "";
      // document.getElementById('date').style = "";
      // document.getElementById('available').style = "";
      // document.getElementById('country').style = "";
      // document.getElementById('department').style = "";
      // for (let i = 0; i < skill_pro.length; i++) {
      //     document.getElementById(i + "t").style = "";
      //   }

      let check = 0;
      let skill_pro = [];
      console.log(this.Role_Description);
      console.log(this.Skills_Required);
      console.log(this.Expiry_Date);
      console.log(this.Available);
      console.log(this.Role_country_ID);
      console.log(this.Role_Department_ID);
      for (let i = 0; i < this.Skills_Required.length; i++) {
        console.log("Hi" + typeof this.Skills_Required[i]);
        skill_pro.push(
          document.getElementById(this.Skills_Required[i].Skill_ID).value
        );
      }
      console.log(skill_pro);

      if (this.Role_ID == 0) {
        document.getElementById("role").style = "color: red";
        this.role_check = 1;
        check = 1;
      } else {
        document.getElementById("role").style = "";
        this.role_check = 0;
      }

      if (this.Role_Description == "") {
        document.getElementById("description").style = "color: red";
        check = 1;
        this.decription_check = 1;
      } else {
        document.getElementById("description").style = "";
        this.decription_check = 0;
      }

      if (this.Skills_Required.length == 0) {
        document.getElementById("skills").style = "color: red";
        check = 1;
        this.skills_check = 1;
      } else {
        document.getElementById("skills").style = "";
        this.skills_check = 0;
      }

      if (this.Expiry_Date == "") {
        document.getElementById("date").style = "color: red";
        check = 1;
        this.date_check = 1;
      } else {
        if (this.Expiry_Date < new Date().toISOString().slice(0, 10)) {
          document.getElementById("date").style = "color: red";
          check = 1;
          this.date_check = 2;
        } else {
          document.getElementById("date").style = "";
          this.date_check = 0;
        }
      }

      if (this.Available == 0) {
        document.getElementById("available").style = "color: red";
        check = 1;
        this.available_check = 1;
      } else {
        if (this.Available < 0) {
          document.getElementById("available").style = "color: red";
          check = 1;
          this.available_check = 2;
        } else {
          document.getElementById("available").style = "";
          this.available_check = 0;
        }
      }

      if (this.Role_country_ID == 0) {
        document.getElementById("country").style = "color: red";
        check = 1;
        this.country_check = 1;
      } else {
        document.getElementById("country").style = "";
        this.country_check = 0;
      }

      if (this.Role_Department_ID == 0) {
        document.getElementById("department").style = "color: red";
        check = 1;
        this.department_check = 1;
      } else {
        document.getElementById("department").style = "";
        this.department_check = 0;
      }

      for (let i = 0; i < skill_pro.length; i++) {
        if (skill_pro[i] == 0 || skill_pro[i] == "") {
          document.getElementById(i + "t").style = "color: red";
          check = 1;
          this.required_check = 1;
        } else {
          if (skill_pro[i] > 4 || skill_pro[i] < 1) {
            document.getElementById(i + "t").style = "color: red";
            check = 1;
            this.required_check = 2;
          } else {
            document.getElementById(i + "t").style = "";
          }
        }
      }

      if (check == 1) {
        return;
      }
      let err_check = 0;
      axios
        .put("http://localhost:5000/api/roles/" + this.id, {
          Available: this.Available,
          Expiry_Date: this.Expiry_Date,
          Role_Country_ID: this.Role_country_ID,
          Role_Listing_Desc: this.Role_Description,
          Role_ID: this.Role_ID,
          Role_department_ID: this.Role_Department_ID,
        })
        .then((response) => {
          console.log(response.data);

          if (response.data.code == 200) {

            for (let i = 0; i < this.keep_orginal_skills.length; i++) {
              console.log(this.keep_orginal_skills[i].Skill_ID)
              axios
                .delete(
                  "http://localhost:5000/api/delete-skill-proficiency/" + this.id,
                  {
                    data: {
                      Skill_ID: this.keep_orginal_skills[i].Skill_ID,
                      },
                  })
                .then((response) => {
                  console.log(response.data);

                  if (response.data.code == 200) {
                  } else {
                    err_check = 1;
                  }
                })
                .catch((error) => {
                  console.log(error.message);
                  err_check = 1;
                });
            }
            let loop_check = 0;
            for (let i = 0; i < skill_pro.length; i++) {
              axios.post(
                "http://localhost:5000/api/add-skill-proficiency/" + this.id,
                {
                  Skill_ID: this.Skills_Required[i].Skill_ID,
                  Role_ID: this.Role_ID,
                  Proficiency: skill_pro[i],
                }
              )
                .then((response) => {
                  console.log(response.data);
                  if (response.data.code == 200) {
                    this.check_finish += 1;
                    console.log(this.check_finish)
                    console.log(skill_pro.length)
                    if (this.check_finish == skill_pro.length) {
                      if (err_check == 0) {
                        alert("Update Success!");
                        window.location.href = "../browseroleshr";
                      } else {
                        alert("Role Listing Update Failed, please contact admin");
                      }
                    }

                  } else {
                    err_check = 1;
                  }
                })
                .catch((error) => {
                  console.log(error.message);
                  if (loop_check == 0) {
                  alert("Role Listing Update Failed, please contact admin");
                  loop_check = 1;
                  }
                });
                
            }

            
          }
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
    role_desc() {
      console.log(this.Role_ID);
      this.Role_Description = this.get_roles[this.Role_ID - 1].Role_Desc;
    },
    printout() {
      console.log(this.Skills_Required);
    },
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style scoped>
div {
  margin: auto auto;
}

.box {
  display: inline-block;
  /* Display divs side by side */
  /* width: 50%; Set the width of each div (50% for two divs) */
  padding: 10px;
  /* Optional: Add padding for spacing */
  width: 500px;
}
</style>
