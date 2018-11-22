from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/result/<name>')
def result(name):
   dict = {'physics':50,'chemical':60,'maths':70,'statistic':85,'history':65}
   return render_template('result2.html', result = dict, name=name)

if __name__ == '__main__':
   app.run(debug = True)
