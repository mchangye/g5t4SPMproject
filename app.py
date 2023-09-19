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
    Dept = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Access_Rights = db.Column(db.Integer, nullable=False)  # Updated column name

class Skills(db.Model): # testing skills table
    Skill_Name = db.Column(db.String(50), primary_key=True)

class Roles(db.Model): # testing skills table
    Role_Name = db.Column(db.String(50), primary_key=True)

class Role_Skill(db.Model): #test role skill table
    Role_Name = db.Column(db.String(50), primary_key=True)
    Skill_Name = db.Column(db.String(50), primary_key=True) #how to account for foreign keys?


#To check whether it can connect
@app.route('/')
# def index():
#     return "Hello"
def index():
    # Query the Staff table, assuming you want to fetch a specific staff record by ID (e.g., ID=1)
    staff_record = Staff.query.get(1)  # You can change the ID as needed
    roles_record = Roles.query.all()

    staff_data = {
        'Staff_FName': staff_record.Staff_FName if staff_record else None,
        'Staff_LName': staff_record.Staff_LName if staff_record else None,
        'Dept': staff_record.Dept if staff_record else None,
        'Country': staff_record.Country if staff_record else None,
        'Email': staff_record.Email if staff_record else None,
        'Access_Rights': staff_record.Access_Rights if staff_record else None
    }

    roles_names = [record.Role_Name for record in roles_record]

    return render_template('index.html', staff=staff_data, roles=roles_names)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
