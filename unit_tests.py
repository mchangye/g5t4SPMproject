from app import app

import unittest
import json
import requests


class TestRoleListing(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    # ALL ROLES
    def test_getRoleListings(self):
        response = self.app.get("/api/roles")
        expected = 200
        self.assertEqual(response.status_code, expected)

        # Check if the response contains JSON data
        data = response.get_json()
        self.assertIsNotNone(data)

        # Verify the structure of the JSON response
        self.assertIn("code", data)
        self.assertIn("data", data)
        self.assertIn("roles", data["data"])

    # READ SPECIFIC ROLE
    def test_read_specific_role(self):
        response = self.app.get("/api/roles/1")
        expected = {
            "code": 200,
            "data": {
                "Available": 1,
                "Expiry_Date": "Sun, 31 Dec 2023 00:00:00 GMT",
                "Role_Country_ID": 3,
                "Role_ID": 1,
                "Role_Listing_Desc": "The account manager acts as a ....",
                "Role_Listing_ID": 1,
                "Role_department_ID": 5,
                "department_name": "Engineering",
                "role_skills": [
                    "Account Management",
                    "Budgeting",
                    "Business Development",
                    "Business Needs Analysis",
                    "Business Negotiation",
                    "Collaboration",
                    "Communication",
                    "Data Analytics",
                    "Pricing Strategy",
                    "Problem Solving",
                    "Product Management",
                    "Sales Strategy",
                    "Stakeholder Management",
                ],
            },
        }

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)


class TestCountryFilter(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    # FILTER BY COUNTRY
    def test_filtered_country(self):
        # Test the "Filtered Roles" API
        response = self.app.get("/api/rolesFiltered?countries=1&countries=3")
        expected = {
            "code": 200,
            "data": {
                "roles": [
                    {
                        "Available": 1,
                        "Country": "Singapore",
                        "Department_Name": "Engineering",
                        "Expiry_Date": "Mon, 25 Dec 2023 00:00:00 GMT",
                        "Role_Country_ID": 1,
                        "Role_ID": 5,
                        "Role_Listing_Desc": "Consultant will be xxxx",
                        "Role_Listing_ID": 3,
                        "Role_Name": "Consultant",
                        "Role_department_ID": 5,
                        "role_skills": [
                            "Account Management",
                            "Business Development",
                            "Business Needs Analysis",
                            "Collaboration",
                            "Communication",
                            "Data Analytics",
                            "Problem Management",
                            "Problem Solving",
                            "Product Management",
                            "Project Management",
                            "Stakeholder Management",
                        ],
                    },
                    {
                        "Available": 1,
                        "Country": "Singapore",
                        "Department_Name": "IT",
                        "Expiry_Date": "Thu, 05 Oct 2023 00:00:00 GMT",
                        "Role_Country_ID": 1,
                        "Role_ID": 6,
                        "Role_Listing_Desc": "The developer in this team will be involved in ....",
                        "Role_Listing_ID": 4,
                        "Role_Name": "Developer",
                        "Role_department_ID": 9,
                        "role_skills": [
                            "Applications Development",
                            "Applications Integration",
                            "Applications Support and Enhancement",
                            "Business Environment Analysis",
                            "Business Needs Analysis",
                            "Business Requirements Mapping",
                            "Business Risk Management",
                            "Collaboration",
                            "Communication",
                            "Configuration Tracking",
                            "Database Administration",
                            "Problem Management",
                            "Problem Solving",
                            "Product Management",
                            "Project Management",
                            "Software Configuration",
                            "Software Design",
                            "Software Testing",
                            "Solution Architecture",
                            "Stakeholder Management",
                            "System Integration",
                            "User Interface Design",
                        ],
                    },
                    {
                        "Available": 1,
                        "Country": "Indonesia ",
                        "Department_Name": "Engineering",
                        "Expiry_Date": "Sun, 31 Dec 2023 00:00:00 GMT",
                        "Role_Country_ID": 3,
                        "Role_ID": 1,
                        "Role_Listing_Desc": "The account manager acts as a ....",
                        "Role_Listing_ID": 1,
                        "Role_Name": "Account Manager",
                        "Role_department_ID": 5,
                        "role_skills": [
                            "Account Management",
                            "Budgeting",
                            "Business Development",
                            "Business Needs Analysis",
                            "Business Negotiation",
                            "Collaboration",
                            "Communication",
                            "Data Analytics",
                            "Pricing Strategy",
                            "Problem Solving",
                            "Product Management",
                            "Sales Strategy",
                            "Stakeholder Management",
                        ],
                    },
                ]
            },
        }

        response_data = response.get_json()  # Extract the JSON data from the response
        # Compare individual parts of the nested dictionaries
        self.assertEqual(response_data["code"], expected["code"])
        self.assertEqual(response_data["data"]["roles"], expected["data"]["roles"])

    def test_filtered_country_invalid(self):
        response = self.app.get("/api/rolesFiltered?countries=-1")
        expected = {"code": 404, "message": "There are no roles."}

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)


class TestFilterSkills(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_filtered_skills(self):
        response = self.app.get("/api/rolesFiltered?skills=4")
        expected = {
            "code": 200,
            "data": {
                "roles": [
                    {
                        "Available": 1,
                        "Country": "Singapore",
                        "Department_Name": "IT",
                        "Expiry_Date": "Thu, 05 Oct 2023 00:00:00 GMT",
                        "Role_Country_ID": 1,
                        "Role_ID": 6,
                        "Role_Listing_Desc": "The developer in this team will be involved in ....",
                        "Role_Listing_ID": 4,
                        "Role_Name": "Developer",
                        "Role_department_ID": 9,
                        "role_skills": [
                            "Applications Development",
                            "Applications Integration",
                            "Applications Support and Enhancement",
                            "Business Environment Analysis",
                            "Business Needs Analysis",
                            "Business Requirements Mapping",
                            "Business Risk Management",
                            "Collaboration",
                            "Communication",
                            "Configuration Tracking",
                            "Database Administration",
                            "Problem Management",
                            "Problem Solving",
                            "Product Management",
                            "Project Management",
                            "Software Configuration",
                            "Software Design",
                            "Software Testing",
                            "Solution Architecture",
                            "Stakeholder Management",
                            "System Integration",
                            "User Interface Design",
                        ],
                    }
                ]
            },
        }

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)


    def test_filtered_skill_invalid(self):
        response = self.app.get("/api/rolesFiltered?skills=-1")
        expected = {"code": 404, "message": "There are no roles."}

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)



class TestFilterDepartment(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_filtered_department(self):
        response = self.app.get("/api/rolesFiltered?departments=9")
        expected = {
            "code": 200,
            "data": {
                "roles": [
                    {
                        "Available": 1,
                        "Country": "Singapore",
                        "Department_Name": "IT",
                        "Expiry_Date": "Thu, 05 Oct 2023 00:00:00 GMT",
                        "Role_Country_ID": 1,
                        "Role_ID": 6,
                        "Role_Listing_Desc": "The developer in this team will be involved in ....",
                        "Role_Listing_ID": 4,
                        "Role_Name": "Developer",
                        "Role_department_ID": 9,
                        "role_skills": [
                            "Applications Development",
                            "Applications Integration",
                            "Applications Support and Enhancement",
                            "Business Environment Analysis",
                            "Business Needs Analysis",
                            "Business Requirements Mapping",
                            "Business Risk Management",
                            "Collaboration",
                            "Communication",
                            "Configuration Tracking",
                            "Database Administration",
                            "Problem Management",
                            "Problem Solving",
                            "Product Management",
                            "Project Management",
                            "Software Configuration",
                            "Software Design",
                            "Software Testing",
                            "Solution Architecture",
                            "Stakeholder Management",
                            "System Integration",
                            "User Interface Design",
                        ],
                    }
                ]
            },
        }

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)

    def test_filtered_department_invalid(self):
        response = self.app.get("/api/rolesFiltered?departments=-1")
        expected = {"code": 404, "message": "There are no roles."}

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)


class TestApplicants(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_applicants(self):
        response = self.app.get("/api/applications/rolelisting/1")
        expected = {
            "code": 200,
            "data": {
                "applications": [
                    {
                        "Application_ID": 3,
                        "Apply": 1,
                        "Email": "Mary.Teo@allinone.com.sg",
                        "Role_Listing_ID": 1,
                        "Staff_ID": 140004,
                        "Staff_Name": "Mary",
                        "Time_Stamp": "Tue, 10 Oct 2023 18:42:25 GMT",
                    },
                    {
                        "Application_ID": 6,
                        "Apply": 1,
                        "Email": "Phuong.Dinh@allinone.com.sg",
                        "Role_Listing_ID": 1,
                        "Staff_ID": 151410,
                        "Staff_Name": "Phuong",
                        "Time_Stamp": "Tue, 10 Oct 2023 18:42:25 GMT",
                    },
                    {
                        "Application_ID": 7,
                        "Apply": 1,
                        "Email": "Phuong.Dinh@allinone.com.sg",
                        "Role_Listing_ID": 1,
                        "Staff_ID": 151410,
                        "Staff_Name": "Phuong",
                        "Time_Stamp": "Tue, 10 Oct 2023 18:42:25 GMT",
                    },
                    {
                        "Application_ID": 9,
                        "Apply": 1,
                        "Email": "Soma.San@allinone.com.sg",
                        "Role_Listing_ID": 1,
                        "Staff_ID": 151533,
                        "Staff_Name": "Soma",
                        "Time_Stamp": "Tue, 10 Oct 2023 18:42:25 GMT",
                    },
                    {
                        "Application_ID": 10,
                        "Apply": 1,
                        "Email": "Siv.Savuth@allinone.com.vn",
                        "Role_Listing_ID": 1,
                        "Staff_ID": 151534,
                        "Staff_Name": "Siv",
                        "Time_Stamp": "Tue, 10 Oct 2023 18:42:25 GMT",
                    },
                ]
            },
        }

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)

    # Applicants for non-existing rolelisting
    def test_get_applicant_invalid_role(self):
        response = self.app.get("/api/applications/rolelisting/9999")
        expected = {
            "code": 404,
            "message": "No applications found for Role_Listing_ID 9999.",
        }

        response_data = response.get_json()  # Extract the JSON data from the response
        self.assertEqual(response_data, expected)





# class TestCalcRSM(unittest.TestCase):
#     def setUp(self):
#         # Create a test client
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_rsm_staff_rolelisting(self):
#         response = self.app.get("/api/calc_rsm/1/140004")
#         expected = {"role_skill_match_percentage": 23}

#         response_data = response.get_json()  # Extract the JSON data from the response
#         print(response_data)
#         self.assertEqual(response_data, expected)


if __name__ == "__main__":
    unittest.main()
