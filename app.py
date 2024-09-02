from flask import Flask, session, request, jsonify, make_response
from flask_login import LoginManager
from datetime import datetime as dt
from flask_pymongo import PyMongo
from utility import *
from group import Group

# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager

login_manager = LoginManager()
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)
app.secret_key = b'yiwpq9853nbmc/sdkf,e.,vx%32985&&%$#@weh' # TODO: change this maybe
# app.config["JWT_SECRET_KEY"] = b'yiwpq9853nbmc/sdkf,e.,vx%32985&&%$#@weh' # TODO: change this maybe
# jwt = JWTManager(app)


@app.get("/hello")
def hello():
    return "hiii\n"

@app.get("/authenticated_hello")
def auth_hello():
    group = authentication_required(session)
    return "hiii " + group.name + "\n"

@app.post("/login")
def login():
    a = request.json
    group_name = get_key_from_json_request(a, "group_name")
    password = get_key_from_json_request(a, "password")
    # res = mongo.db.groups.find_one_or_404({"group_id":group_id, "password":password})
    gr = Group.login_group(group_name, password)
    if gr == None:
        return "groupname or password is incorrect", 404

    session["group_id"] = gr.id 
    # access_token = create_access_token(identity=gr.id)

    # resp = make_response(jsonify(access_token=access_token))
    # resp.set_cookie("access_token", access_token)
    
    return jsonify(group_id=gr.id)


