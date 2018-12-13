from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_wtf import FlaskForm 
from wtforms import TextField, IntegerField, SubmitField, validators

app = Flask(__name__)
app = Flask(__name__)
app.secret_key = 'development key'
# ================app.config diganti sesuai dengan database yang dibuat========
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/dataspk'
Bootstrap(app)
#========DB========
db = SQLAlchemy(app)
# ========sama dengan yang di app.config=========
engine = create_engine('mysql+pymysql://root:root@localhost:8889/dataspk')

# ===============Method==============
#========Mengambil data dari database=> dataframe ===========
def fetchData():
    df = pd.read_sql_table("siswa",engine, columns=['nim','nama', 'tugas', 'uts', 'uas'])
    return df

def nilaiArray(df):
    tugas_array = np.array(df['tugas'])
    uts_array = np.array(df['uts'])
    uas_array = np.array(df['uas'])

    return tugas_array, uts_array, uas_array


# ===========Membuat Table di DB==============
class siswa(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   nim = db.Column(db.String(10))
   nama = db.Column(db.String(50))
   tugas = db.Column(db.Integer)  
   uts = db.Column(db.Integer)
   uas = db.Column(db.Integer)

# ==========================Form==========================
class FormSiswa(FlaskForm):
   nim = TextField("Nim ",[validators.Required("Nim")])
   nama = TextField("Nama", [validators.Required("Nama")])
   tugas = IntegerField("Tugas", [validators.Required("Tugas")])
   uts = IntegerField("UTS", [validators.Required("UTS")]) 
   uas = IntegerField("UAS", [validators.Required("UAS")])
   submit = SubmitField("Input")

#=====================Router===================

#======Migrate database=======================
@app.route('/migrate')
def migrate():
    db.create_all()
    db.session.commit()
    return "Migrating Data......"

#================Input Data=================
@app.route('/inputdata', methods=['GET','POST'])
def inputData():
    form = FormSiswa()
    if form.validate_on_submit():
        dataSiswa = siswa(nim=form.nim.data, nama=form.nama.data, tugas=form.tugas.data, uts=form.uts.data,uas=form.uas.data)
        db.session.add(dataSiswa)
        db.session.commit()
        return "Success Input data......."
    return render_template("inputdata.html", form=form)

#==================Menampilkan Tabel Data=========
@app.route('/tabledata')
def tableData():
    tabel = fetchData()
    tugas_array, uts_array, uas_array = nilaiArray(tabel)
    avgtugas = np.average(tugas_array)
    avguts = np.average(uts_array)
    avguas = np.average(uas_array)
    return render_template('tabledata.html',data_frame = tabel.to_html(classes='table table-striped table-dark'), 
    avgtugas=avgtugas,avguts=avguts, avguas=avguas)

if __name__ == '__main__':
   app.run(debug = True)