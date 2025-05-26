from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy  import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACH_MODIFICATIONS'] = False

# create Database Instance 
db = SQLAlchemy(app)
# define a Class for defining model of patient Table 
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    disease = db.Column(db.String(200))
    date = db.Column(db.Date,default =datetime.utcnow)
    
    


# User Authentication
USERNAME = 'admin'
PASSWORD = 'admin123'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')


# Dashboard 
@app.route('/dashboard')
def dashboard():
    patients = Patient.query.all()
    

    return render_template('dashboard.html',patients =patients)

# Add Patient details 
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method =='POST':
        name = request.form.get('Patient-Name')
        age =  request.form.get('Patient-Age')
        gender = request.form.get('Gender')
        phone = request.form.get('Patient-PhoneNo')
        desc = request.form.get('Patient-desc')   
        date = datetime.strptime(date_str,'%Y-%m-%d').date() if date_str  else datetime.utcnow().date()
#
        new_patient = Patient(name=name, age= age, gender= gender,phone= phone,disease=desc,date=date)
        db.session.add(new_patient)
        db.session.commit()
        
        print(f"Patient Added : {name},{age},{phone}")   
        return redirect(url_for('dashboard'))
    return render_template('add_patient.html')

@app.route('/delete_patient/<int:patient_id>',methods = ['POST'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/update_patient/<int:patient_id>',methods =['GET','POST'])
def update_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    if request.method == 'POST':
        patient.name = request.form['Patient-Name']
        patient.age = request.form['Patient-Age']
        patient.gender = request.form['Gender']
        patient.phone = request.form['Patient-PhoneNo']
        patient.disease = request.form['Patient-desc']
        
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('update_patient.html',patient=patient)


# Sort the Data by date 
@app.route('/patients_by_date')
def  patients_by_date():
    Selected_date= request.args.get('date')
    patients =get_patients_by_date(Selected_date)
    
    return render_template('patients_by_date.html',patients=patients,Selected_date=Selected_date)
    
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)