#!/usr/bin/env python
import datetime
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from app.main.controller.api_auth import *
from app.main.model.models import *

# from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "92b5c7b10ed09879ca40ac46b236cdfb"

app.config["MONGODB_SETTINGS"] = "mongodb://localhost/prodaction_db"
app.permanent_session_lifetime = datetime.timedelta(minutes=20)
app.config.from_object(__name__)


api = Api(app)



@app.route("/")
def index():
    print(User.objects.all())
    return {"choice": True}


if __name__ == "__main__":
    app.run(debug=True)
