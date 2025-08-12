from flask import Flask, render_template,redirect,url_for, request,jsonify, send_file
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import Flask
from datetime import datetime
from flask import flash, session
from dotenv import load_dotenv
# from weasyprint import HTML,CSS
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY']="eejfvbhghjokpoihgyu89765t78uijhbgfcvbhn"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    secondary_phone_number = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    emergency_contact_name = db.Column(db.String(100), nullable=False)
    emergency_contact_number = db.Column(db.String(100), nullable=False)
    employment_id = db.Column(db.String(100), nullable=False, unique=True)
    job_title = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    employment_start_date = db.Column(db.Date, nullable=False)
    employment_status = db.Column(db.String(100), nullable=False)
    reporting_manager = db.Column(db.String(100), nullable=True)
    bank_account= db.Column(db.String(100), nullable=False)
    insurance_policy_number = db.Column(db.String(100), nullable=False)
    tax_identification_number = db.Column(db.String(100), nullable=False)
    blood_group = db.Column(db.String(100), nullable=False)
    known_allergies = db.Column(db.String(100), nullable=True)
    special_instructions = db.Column(db.String(100), nullable=True)
    passport_number = db.Column(db.String(100), nullable=False)
    visa_details = db.Column(db.String(100), nullable=False)
    consent = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False)
    signature = db.Column(db.String(100), nullable=True)

# def validate_phone_number(primary_phone_number):
#     if primary_phone_number is None:
#         return False
#     return len(primary_phone_number) == 10 and primary_phone_number is int and primary_phone_number>0 and primary_phone_number*10!=primary_phone_number
# def validate_phone_number(secondary_phone_number):
#     if secondary_phone_number is None:
#         return False
#     return len(secondary_phone_number) == 10 and secondary_phone_number is int and secondary_phone_number>0 and secondary_phone_number*10!=secondary_phone_number

# def validate_aadhar_number(aadhar_number):
#     if aadhar_number is None:
#         return False
#     return len(aadhar_number)==12 and aadhar_number is int and aadhar_number>0 and (str(aadhar_number)[0]!= '0' or str(aadhar_number)[0]!='1')


def add_missing_columns():
    with app.app_context():
        result = db.session.execute(text("PRAGMA table_info(employee);"))
        columns = [row[1] for row in result]
        if 'secondary_phone_number' not in columns:
            db.session.execute(text("ALTER TABLE employee ADD COLUMN secondary_phone_number TEXT not null;"))
            db.session.commit()
            print("Added missing column: secondary_phone_number")
            print("TEXT:not NULL")


@app.route('/template')
def template():
    return render_template('index.html')
def validate_phone_number(phone_number):
    if phone_number is None or not isinstance(phone_number, str):
        return False
    return len(phone_number) == 10 and phone_number.isdigit()

def validate_aadhar_number(aadhar_number):
    if aadhar_number is None or not isinstance(aadhar_number, str):
        return False 
    return len(aadhar_number) == 12 and aadhar_number.isdigit()


@app.route('/', methods=['GET', 'POST'])
def index():
    employee = None
    if request.method == 'POST':
        form_data = request.form
        print("Secondary Phone Number:", form_data.get('secondary_phone_number'))
        print('getting form data',request)
        print("received form data:", form_data) 
        yesorno = form_data.get('consent')
        print(yesorno)
        if yesorno == "0":
            print('Please consent')
            flash('Please enter the consent')
            return redirect(url_for('index'))
        
        # primary_phone_number = form_data.get('primary_phone_number')
        # secondary_phone_number = form_data.get('secondary_phone_number')
        # aadhar_number = form_data.get('aadharnumber')
        
        # if not (validate_phone_number(primary_phone_number) and 
        #         validate_phone_number(secondary_phone_number)):
        #     flash('Invalid phone number. Please enter valid numbers.', 'danger')
        #     return redirect(url_for('success'))
        # if not (validate_aadhar_number(aadhar_number)):
        #     flash('Invalid Aadhar number. Please enter valid number.', 'danger')
        #     return redirect(url_for('success'))
            
        try:
            date_of_birth = datetime.strptime(form_data.get('dateofbirth'), '%Y-%m-%d').date() if form_data.get('dateofbirth') else None
            employment_start_date = datetime.strptime(form_data.get('employmentstartdate'), '%Y-%m-%d').date() if form_data.get('employmentstartdate') else None
            final_date = datetime.strptime(form_data.get('finaldate'), '%Y-%m-%d').date() if form_data.get('finaldate') else None
            
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
                secondary_phone_number=form_data.get('secondary_phone_number'),
                email=form_data.get('email'),
                emergency_contact_name=form_data.get('emergencycontactname'),
                emergency_contact_number=form_data.get('emergencycontactnumber'),
                employment_id=form_data.get('employmentid'),
                job_title=form_data.get('jobtitle'),
                department=form_data.get('department'),
                employment_start_date=employment_start_date,
                employment_status=form_data.get('employmentstatus'),
                reporting_manager=form_data.get('reportingmanager')if form_data.get('reportingmanager') else None,
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
                signature=form_data.get('signature')if form_data.get('signature') else None
            )
            db.session.add(employee)
            db.session.commit()
            
            if  yesorno == "1":
                print('Consent received')
            flash("Form submitted successfully!",'success') 
            return render_template('success.html', employee=employee)
        except Exception as e:
            db.session.rollback()
            logging.error(f"An error occurred while adding employee: {e}")
            flash("Form submitted successfully!")
            return redirect(url_for('index'))
    return  render_template('index.html',employee=employee)

    
@app.route('/submit', methods=['POST'])
def submit():
    
    required_fields = [
        'firstname', 'lastname', 'dateofbirth', 'gender', 'aadharnumber',
        'Maritalstatus', 'primaryphonenumber', 'currentaddress','permanentaddress',
        'secondary_phone_number', 'email',
        'emergencycontactname', 'emergencycontactnumber', 'employmentid',
        'jobtitle', 'department', 'employmentstartdate', 'employmentstatus',
        'bankaccount','insurancepolicynumber', 'taxidentificationnumber',
        'bloodgroup', 'passportnumber','visadetails','finaldate'
    ]
    missing_fields = []
    for field in required_fields:
        if not request.form.get(field):
            missing_fields.append(field)

    if missing_fields:
        flash(f'Please fill in the following fields: {", ".join(missing_fields)}', 'danger')
        return redirect(url_for('index'))


    for field in required_fields:
        if not request.form.get(field):
            return render_template('template', alert='Please fill this field.')
        
    # webPage = HTML(url_for('success'))
    # webCss = CSS(url_for('download_css'))
    # webPage.write_pdf(
    # '/tmp/form-content.pdf',optimize_images=True, stylesheets=[webCss])
        
    flash('Form submitted successfully!','success')  
    return redirect(url_for('success'))

@app.route('/cancel')
def cancel():
    flash('Form submission canceled.')
    return redirect(url_for('index'))
@app.route('/set_printed_flag', methods=['POST'])
def set_printed_flag():
    session['form_printed'] = True
    return '', 204  # No content response

@app.route('/success',methods=['GET'])
def success():
    form_printed = session.pop('form_printed', False)
    return render_template('success.html',form_printed=form_printed)

        
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        'id': employee.id,
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'date_of_birth': employee.date_of_birth,
        'job_title': employee.job_title,
        'email': employee.email,
        'secondary_phone_number':employee.secondary_phone_number,
    } for employee in employees])
          
    
    employees = Employee.query.filter_by(is_employee=True).all()

    return {'employees': [employee.name for employee in employees]}

with app.app_context():
    db.create_all()
    add_missing_columns()

    

if __name__ == "__main__":
    app.run(debug=True)
