from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_wtf import FlaskForm 
from wtforms import TextField, IntegerField, SubmitField, validators, TextAreaField

app = Flask(__name__)
app.secret_key = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/spk01'
Bootstrap(app)
#========DB========
db = SQLAlchemy(app)
engine = create_engine('mysql+pymysql://root:root@localhost:8889/spk01')

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   age = db.Column(db.Integer)

def __init__(self, name):
   self.name = name
   
# =======Form=========
class ContactForm(FlaskForm):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   city = TextField("City", [validators.Required("Please enter city.")])
   address = TextAreaField("Address", [validators.Required("Please enter your Address.")])
   age = IntegerField("age") 
   submit = SubmitField("Input")

# =========Router========
@app.route('/')
def index():
    db.create_all()
    db.session.commit()
    return ("Migrate data..")

@app.route('/success')
def success():
    
    return render_template('success.html')

@app.route('/tabledata')
def tabledata():
    df = pd.read_sql_table("students",engine, columns=['name','city', 'addr', 'age'])

    return render_template('tabledata.html',data_frame=df.to_html(classes='table table-striped table-dark'))

@app.route('/new', methods = ['GET', 'POST'])
def new():
    form = ContactForm()
   
    if form.validate_on_submit():
        student = students(name=form.name.data, city=form.city.data, addr=form.address.data, age=form.age.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('newdata.html', form=form)

if __name__ == '__main__':
   app.run(debug = True)