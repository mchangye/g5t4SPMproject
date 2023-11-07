import unittest
from app import app, db  # Import your Flask app and necessary modules

class TestYourAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app = app.test_client()

        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    # Write test cases here
    def test_get_all_roles_filtered(self):
        response = self.app.get('/api/rolesFiltered')
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the expected response

    def test_get_specific_role(self):
        response = self.app.get('/api/roles/1')
        self.assertEqual(response.status_code, 200)

    def test_get_filtered_role(self):
         response = self.app.get("/api/roles")
         self.assertEqual(response.status_code, 200)

    def test_get_landing(self):
        response = self.app.get("/api/landing")
        self.assertEqual(response.status_code, 200)

    def test_get_staff_info(self):
        response = self.app.get("/api/get-staff-info")
        self.assertEqual(response.status_code, 200)

    def test_get_specific_staff(self):
        response = self.app.get("/api/get-staff-info/140004")
        self.assertEqual(response.status_code, 200)
    
    def test_update_specific_role_listing(self):
        data = {
            "Expiry_Date": "2028-12-12",
        }
        response = self.app.put("/api/roles/1", json=data)
        self.assertEqual(response.status_code, 200)
         #error 500

    # def test_create_role(self):
    #      data = {
    #           'Role_Listing_ID': '80',
    #         'Role_ID': '90',
    #         'Role_Listing_Desc': 'test',
    #         'Role_department_ID': '55',
    #         'Role_Country_ID': '68',
    #         'Available': '1',
    #         'Expiry_Date': '2028-12-12',
    #         'role_skills': [
    #             {'Skill_ID': 1},
    #             {'Skill_ID': 2}
    #         ],
    #         'Proficienct_Listing': [1, 2]
    #      }

        # response = self.app.post("/api/createrole", json=data)
         #self.assertEqual(response.status_code, 201)
         #error 415

    def test_get_staff_all_skill_id(self):
         response = self.app.get("/api/get-staff-all-skill-id/140004")
         self.assertEqual(response.status_code, 200)

    def test_get_skill_info(self):
         response = self.app.get("/api/get-skill-info/1")
         self.assertEqual(response.status_code, 200)

    #def test_update_staff_skill_proficiency(self):
     #    data = {
      #      "Staff_ID": "140003",
       #     "Skill_ID": "25",
        #    "Proficiency_Level": "3"
         #}
         #response = self.app.put("/api/update-skill-proficiency/140004", json=data)
         #self.assertEqual(response.status_code, 200)
         #error 415

    def test_get_role_info(self):
         response = self.app.get("/api/get-roles-info/")
         self.assertEqual(response.status_code, 200)

    def test_get_specific_role_info(self):
         response = self.app.get("/api/get-roles-info/1")
         self.assertEqual(response.status_code, 200)

    def test_get_specific_dept_info(self):
         response = self.app.get("/api/get-dept-info/1")
         self.assertEqual(response.status_code, 200)

    def test_get_applications(self):
         response = self.app.get("/api/applications/")
         self.assertEqual(response.status_code, 200)

    def test_get_app_by_role_listing(self):
         response = self.app.get("api/applications/rolelisting/1")
         self.assertEqual(response.status_code, 200)

    def test_get_app_per_staff(self):
         response = self.app.get("/api/applications/staff/140004/")
         self.assertEqual(response.status_code, 200)

    #def test_apply_role(self):
        #response = self.app.post("/api/apply-role")
        #self.assertEqual(response.status_code, 200)
        #error415

    def test_get_all_skills(self):
         response = self.app.get("/api/allskills")
         self.assertEqual(response.status_code, 200)

    def test_get_all_countries(self):
         response = self.app.get("/api/allcountries")
         self.assertEqual(response.status_code, 200)

    def test_get_all_departments(self):
         response = self.app.get("/api/alldepartments")
         self.assertEqual(response.status_code, 200)

    def test_get_rsm(self):
         response = self.app.get("/api/calc_rsm/1/140004/")
         self.assertEqual(response.status_code, 200)

    

    

    # Add more test methods for other endpoints and scenarios

if __name__ == '__main__':
    unittest.main()

