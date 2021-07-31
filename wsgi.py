from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy, sqlalchemy # object relational mapper ORM

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"

from model.model import User

"""
    there are few request methods when you work http protocal

    GET - most used and fastest of all the methods and least secure
    POST - it is slow and mostly used to fill forms(mainly when we have to submit userid password etc.). 
            if we talk about REST API then POST method is prefered when we have to create a new data in database
    
    PUT - it is exactly same as POST but it is convention in REST API development to use it for updating any data.

    DELETE - it is used to delete any data in database.

"""
# { REST-API }

@app.route("/register", methods=["POST"])
def register():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            # we will save data in database
            user = User(user_email=email)
            user.hash_password(password)

            db.session.add(user)
            db.session.commit()

            return jsonify(status = True, msg="User registered.")
        
        return jsonify(status = False, 
                msg = "Email is missing!" if email is None else "Password is missing!"
            )


    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        return jsonify(status = False, msg="email is already registered.")
    except:
        db.session.rollback()
        return jsonify(
            status = False, 
            msg = "Unknown Error Occured!"
        )



@app.route("/login", methods=["POST"])
def login():
    try:
        email, password = request.form.get("email"), request.form.get("password")
        if email and password:
            #verifying the user
            "SELECT password FROM myappusers WHERE user_email=?"
            "SELECT * FROM myappusers WHERE user_email=? LIMIT=1"
            "SELECT * FROM myappusers WHERE id=?"
            # user = User.query.get(2)
            user = User.query.filter_by(user_email = email).first()
            if user.verify_password(password):
                return jsonify(status = True, msg = "Logged in!")
            else:
                return jsonify(status =False, msg = "password didn't matched!")
            # user = User.query.with_entities(User.password, User.user_email).filter_by(user_email = email)

        else:
            return jsonify(status = False, msg = "Email is missing!" if email is None else "Password is missing!")

    except Exception as e:
        print(e,"\n")
        return jsonify(status = False, msg="Unknown error occured!")

