# from flask import Flask, request, render_template
# import pandas as pd
# import home

# #declaring a Flask app

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def main():

#     if request.method == "POST": # If the form is submitted

#        clf = joblib.load("data.pkl") 

from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')
STATIC_URL = 'static/sample/'
# url_for('static', filename='samplee.css')

@app.route('/')
def home():
   return render_template('sample.html')
if __name__ == '__samplee__':
   app.run(debug = True)