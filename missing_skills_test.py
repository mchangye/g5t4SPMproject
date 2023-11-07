from app import app

import unittest


class TestMissingSkills(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_missing_skills(self):
        staffskill = self.app.get("/api/get-staff-all-skill-id/140004")
        staffskill = staffskill.get_json()
        staffskill1 = []
        for s_skill in staffskill:
            staffskill1.append(s_skill['Skill_ID'])
        # staffskill1 contains list with skill IDs 
        roleskill = self.app.get("/api/roles/1")
        roleskill =  roleskill.get_json()
        roleskill = roleskill['data']
        roleskill = roleskill['skills_proficiency']
        roleskill1 = []
        for skill in roleskill:
            roleskill1.append(skill['Skill_ID'])
        # roleskill contains list with skill id
        missingskillid = []
        for skill in roleskill1:
            if skill not in staffskill1:
                missingskillid.append(skill)
        
        expected = missingskillid
        self.assertEqual(expected, [10,12,14,20,21,25,51,53,61,72])



if __name__ == "__main__":
    unittest.main()
