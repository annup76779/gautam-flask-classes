from flask import Flask, request, jsonify

app = Flask(__name__)

# htts://example.com/

# setting a route '/' 
@app.route("/")
def index():
    return "Hello World!" 

@app.route("/login", methods=["POST"])
def login():
    userid = request.form.get("userid")
    password = request.form.get("password")
    if userid == "annup76779" and password =="76779":
        return jsonify(status = True, msg="You are logged in.")
    else:
        return jsonify(status = False, msg="Userid or password is invalid.")