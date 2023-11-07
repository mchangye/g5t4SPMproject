##### WHAT IS THE PURPOSE OF THIS FILE? #####
# This file is to declare the database variables from your MySQL and for all the Flask functions.

from datetime import datetime
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.orm import aliased

app = Flask(__name__)

# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/sbrp' 
# ^ For Windows
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/sbrp'
# ^ For Mac
db = SQLAlchemy(app)
CORS(app)


class Staff(db.Model):
    __tablename__ = 'staff'
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Department_ID = db.Column(db.Integer, nullable=False)
    Country_ID = db.Column(db.Integer, nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Access_ID = db.Column(db.Integer, nullable=False)  # Updated column name


# class Skills(db.Model): # testing skills table
#     Skill_ID = db.Column(db.Integer, primary_key=True)
#     Skill_Name = db.Column(db.String(50), nullable=False)

    

class Roles(db.Model): # testing skills table
    __tablename__ = 'roles'

    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(50), nullable=False)
    Role_Desc = db.Column(db.String(1000), nullable=False)

    def json(self):
        dto = {
            'Role_ID': self.Role_ID,
            'Role_Name': self.Role_Name,
            'Role_Desc': self.Role_Desc
        }

        return dto

# class Role_Skill(db.Model): #test role skill table
#     Role_Name = db.Column(db.String(50), primary_key=True)
#     Skill_Name = db.Column(db.String(50), primary_key=True) #how to account for foreign keys?


class Department(db.Model):
    __tablename__ = 'department'

    Department_ID = db.Column(db.Integer, primary_key=True)
    Department_Name = db.Column(db.String(50), nullable=False)

    def json(self):
        dto = {
            'Department_ID': self.Department_ID,
            'Department_Name': self.Department_Name
        }

        return dto
    
# class Function(db.Model):
#     __tablename__ = 'job_function'

#     Job_Function_ID = db.Column(db.Integer, primary_key=True)
#     Job_Function_Name = db.Column(db.String(50), nullable=False)

#     def json(self):
#         dto = {
#             'Job_Function_ID': self.Job_Function_ID,
#             'Job_Function_Name': self.Job_Function_Name
#         }

#         return dto


class RoleListing(db.Model):
    __tablename__ = 'role_listing'

    Role_Listing_ID = db.Column(db.Integer, primary_key=True)
    Role_ID = db.Column(db.Integer, db.ForeignKey('roles.Role_ID'), nullable=False, index=True)
    #Role_ID = db.Column(db.Integer, nullable=False)
    Role_Listing_Desc = db.Column(db.String(1000), nullable=False)
    Role_department_ID = db.Column(db.Integer, db.ForeignKey('department.Department_ID'), nullable=False, index=True)
    #Role_department_ID = db.Column(db.Integer, nullable=False)
    Role_Country_ID = db.Column(db.Integer, db.ForeignKey('country.Country_ID'), nullable=False, index=True)
    #Role_Country_ID = db.Column(db.Integer, nullable=False)
    Available = db.Column(db.SmallInteger(), nullable=False)
    Expiry_Date = db.Column(db.Date(), nullable=False)

    role = db.relationship('Roles', primaryjoin='RoleListing.Role_ID == Roles.Role_ID', backref='role_listing')
    department = db.relationship('Department', primaryjoin='RoleListing.Role_department_ID == Department.Department_ID', backref='role_listing')
    Country = db.relationship('Country', primaryjoin='RoleListing.Role_Country_ID == Country.Country_ID', backref='role_listing')

    def json(self):
        dto = {
            'Role_Listing_ID': self.Role_Listing_ID,
            'Role_ID': self.Role_ID,
            'Role_Listing_Desc': self.Role_Listing_Desc,
            'Role_department_ID': self.Role_department_ID,
            'Role_Country_ID': self.Role_Country_ID,
            'Available': self.Available,
            'Expiry_Date': self.Expiry_Date
        }

        return dto

class roleListingSkillProficiency(db.Model):
    __tablename__ = 'role_listing_skill_proficiency'

    Role_Listing_ID = db.Column(db.Integer, primary_key=True)
    Role_ID = db.Column(db.Integer, db.ForeignKey('roles.Role_ID'), primary_key=True)
    Skill_ID = db.Column(db.Integer, db.ForeignKey('skills.Skill_ID'), primary_key=True)
    Proficienct_Listing = db.Column(db.Integer)

    department = db.relationship('Roles', primaryjoin='roleListingSkillProficiency.Role_ID == Roles.Role_ID', backref='role_listing_skill_proficiency')
    Country = db.relationship('Skills', primaryjoin='roleListingSkillProficiency.Skill_ID == Skills.Skill_ID', backref='role_listing_skill_proficiency')


    def json(self):
        dto = {
            'Role_Listing_ID': self.Role_Listing_ID,
            'Role_ID': self.Role_ID,
            'Skill_ID': self.Skill_ID,
            'Proficienct_Listing': self.Proficienct_Listing
        }

        return dto


class Skills(db.Model):
    __tablename__ = 'skills'

    Skill_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(50))
    Skill_Desc = db.Column(db.String(1000))


    def json(self):
        dto = {
            'Skill_ID': self.Skill_ID,
            'Skill_Name': self.Skill_Name,
            'Skill_Desc': self.Skill_Desc
        }

        return dto

class Staff_Skill(db.Model):
    __tablename__ = 'staff_skill'
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Skill_ID = db.Column(db.Integer, db.ForeignKey('skills.Skill_ID'), primary_key=True)
    Proficiency = db.Column(db.Integer, nullable=False)
 
    skills = db.relationship('Skills', primaryjoin='Staff_Skill.Skill_ID == Skills.Skill_ID', backref='staff_skill')

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

class Application(db.Model):
    __tablename__ = 'application'

    Application_ID = db.Column(db.Integer, primary_key=True)
    Staff_ID = db.Column(db.Integer, db.ForeignKey('staff.Staff_ID'), nullable=False)
    Role_Listing_ID = db.Column(db.Integer, db.ForeignKey('role_listing.Role_Listing_ID'), nullable=False)
    Apply = db.Column(db.SmallInteger(), nullable=False)
    Time_Stamp = db.Column(db.DateTime(), nullable=False)
    # created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
 
    staff = db.relationship('Staff', primaryjoin='Application.Staff_ID == Staff.Staff_ID', backref='application')
    role_listing = db.relationship('RoleListing', primaryjoin='Application.Role_Listing_ID == RoleListing.Role_Listing_ID', backref='application')

    def json(self):
        dto = {
            'Application_ID': self.Application_ID,
            'Staff_ID': self.Staff_ID,
            'Role_Listing_ID': self.Role_Listing_ID,
            'Apply': self.Apply,
            'Time_Stamp': self.Time_Stamp
        }
        return dto
    
# class Staff_HR(db.Model):
#     __tablename__ = 'staff_hr'

#     Staff_ID = db.Column(db.Integer, primary_key=True)
#     Access_Key = db.Column(db.String(20), nullable=False)

#     def json(self):
#         dto = {

#             'Staff_ID': self.Staff_ID,
#             'Access_Key': self.Access_Key
#         }
#         return dto
    
class Country(db.Model):
    __tablename__ = 'country'

    Country_ID = db.Column(db.Integer, primary_key=True)
    Country_Name = db.Column(db.String(50), nullable=False)

    def json(self):
        dto = { 
            'Country_ID': self.Country_ID,
            'Country_Name': self.Country_Name
        }
        return dto
    
class Access_Rights(db.Model):
    __tablename__ = 'access_rights'

    Access_ID = db.Column(db.Integer, primary_key=True)
    Access_Control_Name = db.Column(db.String(50), nullable=False)

    def json(self):
        dto = {
            'Access_ID': self.Access_ID,
            'Access_Control_Name': self.Access_Control_Name
        }
        return dto
    

# READ ALL ROLES
@app.route("/api/roles")
def get_all():
    roleList = RoleListing.query.all()
    roles_with_skills = []

    for role in roleList:
        skills_data = roleListingSkillProficiency.query.filter_by(Role_Listing_ID=role.Role_Listing_ID).with_entities(roleListingSkillProficiency.Skill_ID).all()
        skills = [skill.Skill_ID for skill in skills_data]
        skill_names = []  # List to store skill names

        for skill_id in skills:
            skill = Skills.query.get(skill_id)  # Query the Skills table to get skill names
            if skill:
                skill_names.append(skill.Skill_Name)

        role_data = role.json()

        # # Add Department_Name to role_data
        department = Department.query.filter_by(Department_ID=role.Role_department_ID).first()
        if department:
            role_data['Department_Name'] = department.Department_Name

        # Add Role_Name to role_data
        role_info = Roles.query.filter_by(Role_ID=role.Role_ID).first()
        if role_info:
            role_data['Role_Name'] = role_info.Role_Name

        # Add Country to role_data
        country_info = Country.query.filter_by(Country_ID=role.Role_Country_ID).first()
        if country_info:
            role_data['Country'] = country_info.Country_Name
        

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
    skills_data = RoleSkills.query.filter_by(Role_ID=role.Role_ID).with_entities(RoleSkills.Skill_ID).all()
    skills_data_pro = roleListingSkillProficiency.query.filter_by(Role_Listing_ID=listingID).all()

    # for skill in skills_proficiency_data:
    #     print(skill)
    # print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

    return_skills_pro = []
    skills = [skill.Skill_ID for skill in skills_data]

    skills_ID_pro = [skill.Skill_ID  for skill in skills_data_pro]
    skills_pro = [skill.Proficienct_Listing for skill in skills_data_pro]

    for i in range(len(skills_ID_pro)):
        return_skills_pro.append({'Skill_ID': skills_ID_pro[i], 'Proficienct_Listing': skills_pro[i]})

    skill_names = []  # List to store skill names

    for skill_id in skills_ID_pro:
        skill = Skills.query.get(skill_id)  # Query the Skills table to get skill names
        if skill:
            skill_names.append(skill.Skill_Name)
    

    department = Department.query.get(role.Role_department_ID)
    department_name = department.Department_Name if department else None


    role_data = role.json()
    role_data['role_skills'] = skill_names
    role_data['Department_Name'] = department_name

    if role:

        response_data = {
            'Role_ID': role.Role_ID,
            'Role_Listing_ID': role.Role_Listing_ID,
            'Role_Listing_Desc': role.Role_Listing_Desc,
            'Role_department_ID': role.Role_department_ID,
            #'Role_Function_ID': role.Role_Function_ID,
            'Role_Country_ID': role.Role_Country_ID,
            'Available': role.Available,
            'Expiry_Date': role.Expiry_Date,
            'role_skills': skill_names,
            'department_name': department_name,
            'skills_proficiency': return_skills_pro
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


#Filtered Roles
@app.route("/api/rolesFiltered")
def get_all_filtered():
    selected_departments = request.args.getlist('departments')
    selected_skills = request.args.getlist('skills')
    selected_countries = request.args.getlist('countries')
    selected_expiry_date = request.args.get('expiry_date')


    # Create a base query
    query = RoleListing.query

    # Apply filters if provided
    if selected_departments:
        query = query.filter(RoleListing.Role_department_ID.in_(selected_departments))
    if selected_skills:
        # Create aliases for RoleListing and RoleSkills
        rl_alias = aliased(RoleListing)
        rs_alias = aliased(RoleSkills)

        # Join RoleListing and RoleSkills using aliases and filter by skills
        query = query.join(rs_alias, RoleListing.Role_ID == rs_alias.Role_ID)
        query = query.filter(rs_alias.Skill_ID.in_(selected_skills))

    if selected_countries:
        query = query.filter(RoleListing.Role_Country_ID.in_(selected_countries))

    if selected_expiry_date:
        query = query.filter(RoleListing.Expiry_Date <= selected_expiry_date)

    roleList = query.all()

    roles_with_skills = []

    for role in roleList:
        skills_data = roleListingSkillProficiency.query.filter_by(Role_Listing_ID=role.Role_Listing_ID).with_entities(roleListingSkillProficiency.Skill_ID).all()
        skills = [skill.Skill_ID for skill in skills_data]
        skill_names = []  # List to store skill names

        for skill_id in skills:
            skill = Skills.query.get(skill_id)  # Query the Skills table to get skill names
            if skill:
                skill_names.append(skill.Skill_Name)

        role_data = role.json()

        # Add Department_Name to role_data
        department = Department.query.filter_by(Department_ID=role.Role_department_ID).first()
        if department:
            role_data['Department_Name'] = department.Department_Name

        # Add Role_Name to role_data
        role_info = Roles.query.filter_by(Role_ID=role.Role_ID).first()
        if role_info:
            role_data['Role_Name'] = role_info.Role_Name

        # Add Country to role_data
        country_info = Country.query.filter_by(Country_ID=role.Role_Country_ID).first()
        if country_info:
            role_data['Country'] = country_info.Country_Name

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



#Create role listing
@app.route("/api/createrole", methods=['POST'])
def create_order():
    Role_Listing_ID = request.json.get('Role_Listing_ID', None)
    Role_ID = request.json.get('Role_ID', None)
    Role_Listing_Desc = request.json.get('Role_Listing_Desc', None)
    Role_department_ID = request.json.get('Role_department_ID', None)
    #Role_Function_ID = request.json.get('Role_Function_ID', None)
    Role_Country_ID = request.json.get('Role_Country_ID', None)
    Available = request.json.get('Available', None)
    Expiry_Date = request.json.get('Expiry_Date', None)
    RoleList = RoleListing(Role_Listing_ID=Role_Listing_ID, Role_ID=Role_ID, Role_Listing_Desc=Role_Listing_Desc, Role_department_ID=Role_department_ID, Role_Country_ID=Role_Country_ID, Available=Available, Expiry_Date=Expiry_Date)

    try:
        db.session.add(RoleList)
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the role listing. " + str(e)
            }
        ), 500
    
    role_skills = request.json.get('Skills_Required', None)
    Proficienct_Listing = request.json.get('skill_pro', None)
    all_role_skills = []
    
    for i in range(len(role_skills)):
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        print(role_skills[i]['Skill_ID'])
        role_skill = roleListingSkillProficiency(Role_Listing_ID=RoleList.Role_Listing_ID, Role_ID=Role_ID, Skill_ID=role_skills[i]['Skill_ID'], Proficienct_Listing=Proficienct_Listing[i])
        all_role_skills.append(role_skill)
        try:
            db.session.add(role_skill)
            db.session.commit()
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred while creating the role listing. " + str(e)
                }
            ), 500
    
    print(json.dumps(RoleList.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": RoleList.json(),
            #"data2": all_role_skills
        }
    ), 201

#Update role listing
@app.route("/api/roles/<string:Role_Listing_ID>", methods=['PUT'])
def update_order(Role_Listing_ID):
    try:
        rolelisting = RoleListing.query.filter_by(Role_Listing_ID=Role_Listing_ID).first()
        if not rolelisting:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "Role_Listing_ID": Role_Listing_ID
                    },
                    "message": "Role listing not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if "Available" in data:
            rolelisting.Available = data['Available']
        if "Expiry_Date" in data:
            rolelisting.Expiry_Date = data['Expiry_Date']
        if "Role_Country_ID" in data:
            rolelisting.Role_Country_ID = data['Role_Country_ID']
        if "Role_Listing_Desc" in data:
            rolelisting.Role_Listing_Desc = data['Role_Listing_Desc']
        if "Role_Function_ID" in data:
            rolelisting.Role_Function_ID = data['Role_Function_ID']
        if "Role_ID" in data:
            rolelisting.Role_ID = data['Role_ID']
        if "Role_department_ID" in data:
            rolelisting.Role_department_ID = data['Role_department_ID']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": rolelisting.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Role_Listing_ID": Role_Listing_ID
                },
                "message": "An error occurred while updating the role listing. " + str(e)
            }
        ), 500

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
    department_record=Department.query.get(staff_record.Department_ID)
    country_record=Country.query.get(staff_record.Country_ID)
    access_id_record=Access_Rights.query.get(staff_record.Access_ID)
    if staff_record:
        staff_data = {
            'Staff_FName': staff_record.Staff_FName if staff_record else None,
            'Staff_LName': staff_record.Staff_LName if staff_record else None,
            'Department_ID': department_record.Department_Name if department_record else None,
            'Country_ID': country_record.Country_Name if country_record else None,
            'Email': staff_record.Email if staff_record else None,
            'Access_ID': access_id_record.Access_Control_Name if access_id_record else None
        }
        return jsonify(staff_data)
        #    {
         #       "code": 200,
          ###)
        
    #return jsonify(
     #   {
      #      "code": 404,
       #     "message": "Role not found."
        #}
   # ), 404

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

#Update Skill Proficiency
@app.route('/api/update-skill-proficiency/<int:role_listing_id>', methods=['PUT'])
def update_skill_proficiency(role_listing_id):
    skill_id = request.json.get('Skill_ID', None)
    try: 
        staffskill = roleListingSkillProficiency.query.filter_by(Role_Listing_ID=role_listing_id, Skill_ID=skill_id).first()
        if not staffskill:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "Role_Listing_ID": role_listing_id,
                        "Skill_ID": skill_id
                    },
                    "message": "Skill not found."
                }
            ), 404
        data = request.get_json()
        if 'Skill_ID' in data:
            staffskill.Skill_ID = data['Skill_ID']
        if 'Proficiency' in data:
            staffskill.Proficienct_Listing = data['Proficiency']

        db.session.commit()
        return jsonify(
                {
                    "code": 200,
                    "data": staffskill.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Role_Listing_ID": role_listing_id,
                    "Skill_ID": skill_id
                },
                "message": "An error occurred while updating. " + str(e)
            }
        ), 500

#GET ALL ROLE NAMES
@app.route('/api/get-roles-info/')
def get_roles_all():
    role_record = Roles.query.all()
    role_data = []
    for role in role_record:
        role_data.append({
            'Role_ID': role.Role_ID,
            'Role_Name': role.Role_Name,
            "Role_Desc": role.Role_Desc
        })

    return jsonify(role_data)

#GET specific role name
@app.route('/api/get-roles-info/<role_id>')
def get_roles_data(role_id):
    role_record = Roles.query.get(role_id)
    role_data = {
        'Role_ID': role_record.Role_ID if role_record else None,
        'Role_Name': role_record.Role_Name if role_record else None,
    }
    return jsonify(role_data)

#GET Specific Department Name
@app.route('/api/get-dept-info/<dept_id>')
def get_dept_data(dept_id):
    dept_record = Department.query.get(dept_id)
    role_data = {
        'Department_ID': dept_record.Role_ID if dept_record else None,
        'Role_Name': dept_record.Role_Name if dept_record else None,
    }
    return jsonify(role_data)


# GET all applications
@app.route("/api/applications/")
def get_all_applications():
    applicationList = Application.query.all()

    if len(applicationList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "applications": [application.json() for application in applicationList]
                }
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "You have no applications."
            }
        ), 404
    

# GET Applications by Role Listing 
@app.route("/api/applications/rolelisting/<int:Role_Listing_ID>")
def get_applications_by_role(Role_Listing_ID):
    applicationList = Application.query.filter_by(Role_Listing_ID=Role_Listing_ID).all()
    application_with_staff = []

    for application in applicationList:

        application_data = application.json()

        # # Add Staff Information to application_data
        staff = Staff.query.filter_by(Staff_ID=application.Staff_ID).first()
        if staff:
            application_data['Staff_Name'] = staff.Staff_FName
            application_data['Email'] = staff.Email

        application_with_staff.append(application_data)

    if len(application_with_staff):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "applications": application_with_staff
                }
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": f"No applications found for Role_Listing_ID {Role_Listing_ID}."
            }
        ), 404
    

# GET Applications for each staff
@app.route("/api/applications/staff/<int:staff_id>/")
def get_staff_applications(staff_id):
    applicationList = Application.query.filter_by(Staff_ID=staff_id).all()
    application_with_role = []

    for application in applicationList:

        application_data = application.json()

        # # Add Role Listing Details to application_data
        role = RoleListing.query.filter_by(Role_Listing_ID=application.Role_Listing_ID).first()
        if role:
            application_data['Role_ID'] = role.Role_ID
            application_data['Role_Listing_Desc'] = role.Role_Listing_Desc
            application_data['Department_ID'] = role.Role_department_ID


        # # Add Department_Name to application_data
        department = Department.query.filter_by(Department_ID=role.Role_department_ID).first()
        if department:
            application_data['Department_Name'] = department.Department_Name

        # Add Role_Name to application_data
        role_info = Roles.query.filter_by(Role_ID=role.Role_ID).first()
        if role_info:
            application_data['Role_Name'] = role_info.Role_Name
        

        application_with_role.append(application_data)

    if len(application_with_role):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "applications": application_with_role
                }
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": f"No applications found for Staff_ID {staff_id}."
            }
        ), 404


# ...

# Create a new route for applying a role
@app.route("/api/apply-role", methods=['POST'])
def apply_role():
    staff_id = request.json.get('Staff_ID', None)
    role_listing_id = request.json.get('Role_Listing_ID', None)

    try:
        # Check if the user has already applied for the role
        existing_application = Application.query.filter_by(
            Staff_ID=staff_id,
            Role_Listing_ID=role_listing_id
        ).first()
        if existing_application:
            return jsonify(
                {
                    "code": 400,
                    "message": "You have already applied for this role."
                }
            ), 400
        # Check if the user has reached the maximum limit of applications
        max_applications = 4  # Adjust as needed
        user_applications = Application.query.filter_by(Staff_ID=staff_id).count()
        if user_applications >= max_applications:
            return jsonify(
                {
                    "code": 401,
                    "message": "You have reached the maximum limit of 4 applications."
                }
            ), 401
        # Create a new application
        new_application = Application(
            Staff_ID=staff_id,
            Role_Listing_ID=role_listing_id,
            Apply=1,  # Assuming 1 means applied; adjust as needed
            Time_Stamp=datetime.now()
        )
        
        db.session.add(new_application)
        db.session.commit()

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while applying for the role. " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": new_application.json(),
            "message": "Role applied successfully."
        }
    ), 201
    
#get all skills
@app.route("/api/allskills")
def get_skills_all():
    skill_record = Skills.query.all()
    skill_data = []
    for skill in skill_record:
        skill_data.append({
            'Skill_ID': skill.Skill_ID,
            'Skill_Name': skill.Skill_Name,
            'Skill_Desc': skill.Skill_Desc
        })

    return jsonify(skill_data)

#get all countries
@app.route("/api/allcountries")
def get_countries_all():
    country_record = Country.query.all()
    country_data = []
    for country in country_record:
        country_data.append({
            'Country_ID': country.Country_ID,
            'Country_Name': country.Country_Name
        })

    return jsonify(country_data)

#get all departments
@app.route("/api/alldepartments")
def get_departments_all():
    department_record = Department.query.all()
    department_data = []
    for department in department_record:
        department_data.append({
            'Department_ID': department.Department_ID,
            'Department_Name': department.Department_Name
        })

    return jsonify(department_data)



# @app.route("/api/application/<staff_id>/<role_listing_id>/")
# def apply(staff_id, role_listing_id):
#       TO FIX -> FK ERROR in the RoleListingId of Application object, NOT SURE IF NEED TO USE RELATIONSHIPs thingy
#     newApplication = Application(Staff_ID=staff_id, Role_Listing_ID=role_listing_id, Apply=1, Time_Stamp=datetime.now())
#     db.session.add(newApplication)
#     db.session.commit()

# get role skill match %, returns a STRING of the #. not integer!
@app.route("/api/calc_rsm/<int:role_listing_id>/<int:staff_id>/")
def calculate_role_skill_match_percentage(role_listing_id, staff_id):
    # Get skills from role listing id
    role_skills_wanted = [skill.Skill_ID for skill in RoleSkills.query.filter_by(Role_ID=role_listing_id).all()]
    # Get skills from staff id
    applicant_skills = [skill.Skill_ID for skill in Staff_Skill.query.filter_by(Staff_ID=staff_id).all()]
    # # Convert both skill lists to sets for efficient intersection calculation
    role_skills_set = set(role_skills_wanted)
    applicant_skills_set = set(applicant_skills)
    # Calculate the number of matching skills (intersection of sets)
    num_matching_skills = len(role_skills_set.intersection(applicant_skills_set))
    # # Calculate the percentage match
    if num_matching_skills > 0:
        role_skill_match_percentage = (num_matching_skills / len(role_skills_set)) * 100
    else:
        role_skill_match_percentage = 0

    result = {
            "role_skill_match_percentage": int(role_skill_match_percentage)
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
