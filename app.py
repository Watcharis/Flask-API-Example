from flask import Flask, jsonify, request
from pymongo import MongoClient
import json
import sys
sys.path.append('./include')
import sys
sys.path.append('./database')
from databases import DatabasesCar
from handle import HandleRepoPostMethods, HandleRepoGetMethods,HandleRepoPutMethods

app = Flask(__name__)

handlerepopostmethods = HandleRepoPostMethods()
handlerepogetmethods = HandleRepoGetMethods()
handlerepoputmethods = HandleRepoPutMethods()

@app.route("/addcar",methods = ["POST"])
def post_spec_car():
    return handlerepopostmethods.post_method()

@app.route("/showcar",methods = ["GET"])
def get_spec_car():
    return handlerepogetmethods.get_method()

@app.route("/updatecar",methods = ["PUT"])
def put_spec_car():
    return handlerepoputmethods.put_method()





if __name__ == "__main__":
    
    app.run(host='127.0.0.1', port=8000)
    app.debug = True
