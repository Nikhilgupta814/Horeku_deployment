from flask import Flask, render_template, request
from flask.helpers import flash
import joblib

####  initialize the app ####

app = Flask(__name__)
model = joblib.load('dib_79.pkl')

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/predict', methods =['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg, plas, pres, skin, test, mass, pedi, age)
    output = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if output[0]==1:
        ans = 'Diabatic'

    else:
        ans = 'NOt Diabatic'

    return render_template('predict.html', predict = ans)

#### Run the app ###
if __name__=='__main__':
    app.run()
