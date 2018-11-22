from flask import Flask, render_template, request, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

app = Flask(__name__)
app.secret_key = 'development key'

# =======Form=========
class ContactForm(FlaskForm):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   website = TextField("Website", ,[validators.Required("Please enter your website.")])
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++',), 
      ('py', 'Python'),('java', 'java'), ('js','java-script')])
   submit = SubmitField("Send")


# ========router=======
@app.route('/')
def index():
    return redirect(url_for('contact'))

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
   
    if request.method == 'POST':
        if form.validate() == False:
            flash('fill all field first!')
            return render_template('contact.html', form = form)
        else:
            return redirect(url_for('success'))
    elif request.method == 'GET':
        return render_template('contact.html', form = form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
   app.run(debug = True)