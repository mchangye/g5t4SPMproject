##### WHAT IS THE PURPOSE OF THIS FILE? #####
# This file is to declare the database variables from your MySQL and for all the Flask functions.

from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/sbrp'
db = SQLAlchemy(app)
CORS(app)

class Staff(db.Model):
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Department_ID = db.Column(db.Integer, nullable=False)
    Country_ID = db.Column(db.Integer, nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Access_Rights = db.Column(db.Integer, nullable=False)  # Updated column name


# class Skills(db.Model): # testing skills table
#     Skill_ID = db.Column(db.Integer, primary_key=True)
#     Skill_Name = db.Column(db.String(50), nullable=False)

class Staff_Skill(db.Model):
    __tablename__ = 'staff_skill'
    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'), primary_key=True)
    Skill_ID = db.Column(db.Integer, db.ForeignKey('Skills.Skill_ID'), primary_key=True)
    Proficiency = db.Column(db.Integer, nullable=False)

class Roles(db.Model): # testing skills table
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(50), nullable=False)

# class Role_Skill(db.Model): #test role skill table
#     Role_Name = db.Column(db.String(50), primary_key=True)
#     Skill_Name = db.Column(db.String(50), primary_key=True) #how to account for foreign keys?



class RoleListing(db.Model):
    __tablename__ = 'role_listing'

    Role_Listing_ID = db.Column(db.Integer, primary_key=True)
    #Role_Name = db.Column(db.Integer, db.ForeignKey('skill.Skill_Name'), nullable=False, index=True)
    Role_ID = db.Column(db.Integer, nullable=False)
    Role_Desc = db.Column(db.String(1000), nullable=False)
    Role_department_ID = db.Column(db.Integer, nullable=False)
    Role_Function_ID = db.Column(db.Integer, nullable=False)
    Role_Country_ID = db.Column(db.Integer, nullable=False)
    Available = db.Column(db.SmallInteger(), nullable=False)
    Expiry_Date = db.Column(db.Date(), nullable=False)

    #customer = db.relationship('Customer', primaryjoin='Order.customerID == Customer.customerID', backref='orders')

    def json(self):
        dto = {
            'Role_Listing_ID': self.Role_Listing_ID,
            'Role_ID': self.Role_ID,
            'Role_Desc': self.Role_Desc,
            'Role_department_ID': self.Role_department_ID,
            'Role_Function_ID': self.Role_Function_ID,
            'Role_Country_ID': self.Role_Country_ID,
            'Available': self.Available,
            'Expiry_Date': self.Expiry_Date
        }

        return dto


class Skills(db.Model):
    __tablename__ = 'skills'

    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(50))


    def json(self):
        dto = {
            'Skill_ID': self.Skill_ID,
            'Skill_Name': self.Skill_Name
        }

        return dto


class RoleSkills(db.Model):
    __tablename__ = 'role_skill'

    Role_ID = db.Column(db.Integer, primary_key=True)
    Skill_ID = db.Column(db.Integer, primary_key=True)


    def json(self):
        dto = {
            'Role_ID': self.Role_ID,
            'Skill_ID': self.Skill_ID,
        }

        return dto


# READ ALL ROLES
@app.route("/api/roles")
def get_all():
    roleList = RoleListing.query.all()
    roles_with_skills = []

    for role in roleList:
        skills_data = RoleSkills.query.filter_by(Role_ID=role.Role_ID).with_entities(RoleSkills.Skill_ID).all()
        skills = [skill.Skill_ID for skill in skills_data]
        skill_names = []  # List to store skill names

        for skill_id in skills:
            skill = Skills.query.get(skill_id)  # Query the Skills table to get skill names
            if skill:
                skill_names.append(skill.Skill_Name)

        role_data = role.json()
        role_data['role_skills'] = skill_names
        roles_with_skills.append(role_data)

    if len(roles_with_skills):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles": roles_with_skills
                }
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no roles."
            }
        ), 404


# READ SPECIFIC ROLE
@app.route("/api/roles/<int:listingID>")
def find_by_listingID(listingID):

    role = RoleListing.query.filter_by(Role_Listing_ID=listingID).first()
    skills = RoleSkills.query.filter_by(Role_ID=role.Role_ID).with_entities(RoleSkills.Skill_ID).all()

    if role:

        response_data = {
            'Role_ID': role.Role_ID,
            'Role_Listing_ID': role.Role_Listing_ID,
            'Role_Desc': role.Role_Desc,
            'Role_department_ID': role.Role_department_ID,
            'Role_Function_ID': role.Role_Function_ID,
            'Role_Country_ID': role.Role_Country_ID,
            'Available': role.Available,
            'Expiry_Date': role.Expiry_Date,
            'role_skills': [skill.Skill_ID for skill in skills]
            # "role_skills": [skill.json() for skill in skills]
        }

        return jsonify(
            {
                "code": 200,
                "data": response_data
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "Role_Listing_ID": listingID
            },
            "message": "Role not found."
        }
    ), 404


#To check whether it can connect
@app.route('/api/landing')
def get_landing_message():
    landing_message = "Landing for Flask"
    return jsonify(landing_message=landing_message)

@app.route('/api/get-staff-info')
def staff_info_landing():
    return 'This is the landing page for Get Staff Info'

@app.route('/api/get-staff-info/<staff_id>')
def get_staff_data(staff_id):
    staff_record = Staff.query.get(staff_id)
    staff_data = {
        'Staff_FName': staff_record.Staff_FName if staff_record else None,
        'Staff_LName': staff_record.Staff_LName if staff_record else None,
        'Department_ID': staff_record.Department_ID if staff_record else None,
        'Country_ID': staff_record.Country_ID if staff_record else None,
        'Email': staff_record.Email if staff_record else None,
        'Access_Rights': staff_record.Access_Rights if staff_record else None
    }
    return jsonify(staff_data)

#This app.route is to fetch the Staff ID and display all the skills that the staff has
@app.route('/api/get-staff-all-skill-id/<staff_id>')
def get_staff_skill_id(staff_id):
    staff_skills = Staff_Skill.query.filter_by(Staff_ID=staff_id).all()
    skill_data = []
    for record in staff_skills:
        skill_data.append({
            'Skill_ID': record.Skill_ID,
            'Proficiency': record.Proficiency
        })
    return jsonify(skill_data)

#This app.route can work alone but is intended to work with the above /get-staff-all-skill-id to then fetch the names of the skills that the staff has
@app.route('/api/get-skill-info/<skill_id>')
def get_skill_info(skill_id):
    skill_info = Skills.query.get(skill_id)
    skill_data = {
        'Skill_ID': skill_info.Skill_ID if skill_info else None,
        'Skill_Name': skill_info.Skill_Name if skill_info else None
    }
    return jsonify(skill_data)

@app.route('/api/get-roles-info/')
def get_roles_all():
    role_record = Roles.query.all()
    role_data = []
    for role in role_record:
        role_data.append({
            'Role_ID': role.Role_ID,
            'Role_Name': role.Role_Name,
        })

    return jsonify(role_data)

@app.route('/api/get-roles-info/<role_id>')
def get_roles_data(role_id):
    role_record = Roles.query.get(role_id)
    role_data = {
        'Role_ID': role_record.Role_ID if role_record else None,
        'Role_Name': role_record.Role_Name if role_record else None,
    }
    return jsonify(role_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
