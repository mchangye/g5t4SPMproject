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

class Skills(db.Model): # testing skills table
    Skill_Name = db.Column(db.String(50), primary_key=True)

class Roles(db.Model): # testing skills table
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(50), nullable=False)

class Role_Skill(db.Model): #test role skill table
    Role_Name = db.Column(db.String(50), primary_key=True)
    Skill_Name = db.Column(db.String(50), primary_key=True) #how to account for foreign keys?


#To check whether it can connect
@app.route('/api/landing')
def get_landing_message():
    landing_message = "Landing for Flask"
    return jsonify(landing_message=landing_message)

@app.route('/api/get-staff-info')
def staff_info_landing():
    return 'This is the landing page for Get Staff Info'

#testing if it can fetch
# @app.route('/api/get-staff-info/1')
# def get_staff_data1():
#     staff_record = Staff.query.get(1)
#     staff_data = {
#         'Staff_FName': staff_record.Staff_FName if staff_record else None,
#         'Staff_LName': staff_record.Staff_LName if staff_record else None,
#         'Department_ID': staff_record.Department_ID if staff_record else None,
#         'Country_ID': staff_record.Country_ID if staff_record else None,
#         'Email': staff_record.Email if staff_record else None,
#         'Access_Rights': staff_record.Access_Rights if staff_record else None
#     }
#     return jsonify(staff_data)

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

@app.route('/api/get-roles-info')
def roles_info_landing():
    return 'This is the landing page for Get Roles Info'

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
