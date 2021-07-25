from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"

from model.model import *

"""
    there are few request methods when you work http protocal

    GET - most used and fastest of all the methods and least secure
    POST - it is slow and mostly used to fill forms(mainly when we have to submit userid password etc.). 
            if we talk about REST API then POST method is prefered when we have to create a new data in database
    
    PUT - it is exactly same as POST but it is convention in REST API development to use it for updating any data.

    DELETE - it is used to delete any data in database.

"""


@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        pass
