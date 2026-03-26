from flask import Flask, request, render_template, redirect
import pickle
from db import Database
import numpy as np

app = Flask(__name__)   #WSGI 

with open('pipe_lr.pkl', 'rb') as file:
    pipe = pickle.load(file)

# obj = Database()

# @app.route("/")
# def home():
#     return redirect('/predict')


@app.route('/predict', methods = ['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        bmi = request.form['bmi']
        children = request.form['children']
        smoker = request.form['smoker']
        region = request.form['region']
        prediction = np.round(pipe.predict([[age, sex, bmi, children, smoker, region]])[0], 2)
        # obj.save_predictions(age, sex, bmi, children, smoker,region, prediction)
        return render_template('predict.html', pred = prediction)
     
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug= True)
