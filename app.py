from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/sbrp'
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

#To check whether it can connect
@app.route('/')
# def index():
#     return "Hello"
def index():
    # Query the Staff table, assuming you want to fetch a specific staff record by ID (e.g., ID=1)
    staff_record = Staff.query.get(1)  # You can change the ID as needed

    if staff_record:
        staff_data = {
            'Staff_FName': staff_record.Staff_FName,
            'Staff_LName': staff_record.Staff_LName,
            'Dept': staff_record.Dept,
            'Country': staff_record.Country,
            'Email': staff_record.Email,
            'Access_Rights': staff_record.Access_Rights
        }
        return render_template('index.html', staff=staff_data)
    else:
        return render_template('index.html', staff=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)