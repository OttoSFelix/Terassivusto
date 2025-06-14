from flask import Flask
from sqlalchemy.sql import text
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return redirect('/etusivu')

@app.route('/etusivu')
def etusivu():
    sql = "SELECT text FROM text;"
    result = db.session.execute(text(sql))
    teksti = result.fetchall()
    print(teksti)
    return render_template("etusivu.html", text = teksti)
