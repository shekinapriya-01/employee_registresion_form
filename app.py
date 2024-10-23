from flask import Flask, render_template, request,jsonify
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
import templates

# app = Flask(__name__)
# database_url = config('DATABASE_URL')
# print(database_url) 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee_database.db'
# app.config('DATABASE_URL', default='sqlite:///employee_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

app.debug=True
    
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    aadhar_number = db.Column(db.String(100), nullable=False)
    marital_status = db.Column(db.String(100), nullable=False)
    primary_phone_number = db.Column(db.String(100), nullable=False, unique=True)
    current_address = db.Column(db.String(100), nullable=False)
    permanent_address = db.Column(db.String(100), nullable=False)
    secondary_phone_number = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    emergency_contact_name = db.Column(db.String(100), nullable=False)
    emergency_contact_number = db.Column(db.String(100), nullable=False)
    employment_id = db.Column(db.String(100), nullable=False, unique=True)
    job_title = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    employment_start_date = db.Column(db.Date, nullable=False)
    employment_status = db.Column(db.String(100), nullable=False)
    # reporting_manager = db.Column(db.String(100), nullable=False)
    bank_account= db.Column(db.String(100), nullable=False)
    insurance_policy_number = db.Column(db.String(100), nullable=False)
    tax_identification_number = db.Column(db.String(100), nullable=False)
    blood_group = db.Column(db.String(100), nullable=False)
    known_allergies = db.Column(db.String(100), nullable=False)
    special_instructions = db.Column(db.String(100), nullable=False)
    passport_number = db.Column(db.String(100), nullable=False)
    visa_details = db.Column(db.String(100), nullable=False)
    consent = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False)
    signature = db.Column(db.LargeBinary, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def handle_form_data():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        print('getting form data',request)
        form_data = request.form
        signature = request.files.get('signature')
        print("received form data:", form_data)
        try:
                # Convert date strings to date objects
            date_of_birth = datetime.strptime(form_data.get('dateofbirth'), '%Y-%m-%d').date() if form_data.get('dateofbirth') else None
            employment_start_date = datetime.strptime(form_data.get('employmentstartdate'), '%Y-%m-%d').date() if form_data.get('employmentstartdate') else None
            final_date = datetime.strptime(form_data.get('finaldate'), '%Y-%m-%d').date() if form_data.get('finaldate') else None
            sign_Data=signature.read()
            print('getting data')
            employee = Employee(
                first_name=form_data.get('firstname'),
                last_name=form_data.get('lastname'),
                date_of_birth=date_of_birth,
                gender=form_data.get('gender'),
                aadhar_number=form_data.get('aadharnumber'),
                marital_status=form_data.get('Maritalstatus'),
                primary_phone_number=form_data.get('primaryphonenumber'),
                current_address=form_data.get('currentaddress'),
                permanent_address=form_data.get('permanentaddress'),
                secondary_phone_number=form_data.get('secondaryphonenumber'),
                email=form_data.get('email'),
                emergency_contact_name=form_data.get('emergencycontactname'),
                emergency_contact_number=form_data.get('emergencycontactnumber'),
                employment_id=form_data.get('employmentid'),
                job_title=form_data.get('jobtitle'),
                department=form_data.get('department'),
                employment_start_date=employment_start_date,
                employment_status=form_data.get('employmentstatus'),
                # reporting_manager=form_data.get('reportingmanager'),
                bank_account=form_data.get('bankaccount'),
                insurance_policy_number=form_data.get('insurancepolicynumber'),
                tax_identification_number=form_data.get('taxidentificationnumber'),
                blood_group=form_data.get('bloodgroup'),
                known_allergies=form_data.get('knownallergies'),
                special_instructions=form_data.get('specialinstructions'),
                passport_number=form_data.get('passportnumber'),
                visa_details=form_data.get('visadetails'),
                consent=bool(form_data.get('consent')),
                date=final_date,
                signature=sign_Data # Assuming signature handling is correct
            )

            db.session.add(employee)
            db.session.commit()

            print(employee)
            return jsonify({"message": 'Form submitted successfully!'})
            
        except Exception as e:
            print("Error occurred:", e)
            return jsonify({"message": 'An error occurred while submitting the form.'}), 5000
        # finally:
        #     return jsonify({"msg":"THank you"})




@app.route('/employees', methods=['GET'])
def get_employees():
    
    employees = Employee.query.filter_by(is_employee=True).all()

    return {'employees': [employee.name for employee in employees]}
    #return jsonify([{'id': employee.id, 'first_name': employee.first_name, 'last_name': employee.last_name, 'date_of_birth': employee.date_of_birth} for employee in employees])


with app.app_context():
    db.create_all()

    # if __name__ == '__main__':
    #  app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
