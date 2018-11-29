# SISTEM PENUNJANG KEPUTUSAN (SPK)
### Menjalankan aplikasi web flask (course06_db_ex)
Di dalam folder/directory buat virtual environment terlebih dahulu:

    > virtualenv venv

Jalankan virtualenv tersebut:

	> cd /venv/Scripts
    > activate

Setelah virtual envronment active, install component yang sudah ada pada requirements.txt:
	
	> pip install -r requirements.txt

Buat database di komputer masing-masing.

Buka file web.py lalu rubah baris:
	
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/dataspk'

dan 
	
	engine = create_engine('mysql+pymysql://root:root@localhost:8889/dataspk')

sesuai dengan setting database masing-masing.
contoh:

user: root
password: password
host: localhost
port: 3306
nama DB: data01

Maka baris tersebut dirubah sbb:

	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/data01'

dan

	engine = create_engine('mysql+pymysql://root:password@localhost:3306/data01')

Setelah itu jalankan aplikasi webnya:
		
	python web.py

Lalu migrasi data dengan mengetikkan alamat berikut di browser:
	
	http://127.0.0.1/migrate

Untuk menginput data dapat menggunakan Link:

	http://127.0.0.1/inputdata

Untuk melihat keseluruhan data dalam bentuk tabel dapat menggunakan Link:

	http://127.0.0.1/tabledata

nantinya data akan menampilkan tabel dan menampilkan nilai rata-rata Tugas, UTS, UAS.


