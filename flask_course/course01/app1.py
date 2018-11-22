from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello Flask-python !'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ =='__main__':
    # app.run()
    app.run(debug = True)
