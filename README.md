# SISTEM PENUNJANG KEPUTUSAN (SPK)
### Menjalankan aplikasi web flask (course06_db_ex)
Di dalam folder/directory buat virtual environment terlebih dahulu:

    > virtualenv venv

Jalankan virtualenv tersebut:

	> cd /venv/Scripts
    > activate

Setelah virtual envronment active, install component yang sudah ada pada requirements.txt:
	
	> pip install -r requirements.txt

Buka file web.txt lalu rubah baris:
	
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/dataspk'

dan 
	
	engine = create_engine('mysql+pymysql://root:root@localhost:8889/dataspk')

sesuai dengan database masing-masing.



