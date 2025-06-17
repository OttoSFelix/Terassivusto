from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')


@app.route("/")
def index():
    return redirect('/etusivu')

@app.route('/etusivu')
def etusivu():
    return render_template("etusivu.html")

@app.route('/yhteystiedot')
def yhteystiedot():
    return render_template('yhteystiedot.html')

@app.route('/hinnasto')
def hinnasto():
    return render_template('hinnasto.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/galleria')
def galleria():
    return render_template('galleria.html')