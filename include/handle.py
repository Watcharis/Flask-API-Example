import sys
sys.path.append('../database/datbases')
from databases import DatabasesCar
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask
from flask import jsonify
from flask import request
import requests
import json


databasescar = DatabasesCar()

db = databasescar.data_spec_car()
#print(data)

#test_class_1 = data.storecar.insert_one({"id":2,"gen":"toyota"})
#test_class_2 = data.storecar.find_one({"id":2,"gen":"toyota"})
#print(test_class_2)

class HandleRepoPostMethods : 
    
    def post_method(self):
        try :
            body = request.get_json()
        except Exception as e :
            print(e)
            return jsonify({"status":400, "messages": "invalide body request"})
        try :
            _body = body
            print(type(_body))
        except Exception as e :
            print(e)
            return jsonify({"status":402, "messages": "invalide body"})
        try:
            data_car = db.storecar.insert(_body)
            print(data_car)
        except Exception as e :
            print(e)
            return jsonify({"status":401, "messages": "invalide insert body"})
        
        return jsonify({"status":200})
    

class HandleRepoGetMethods :

   def get_method(self):

        try:
            id = "5d848c9ac2b2147e20468c2b"
            data_get = db.storecar.find({"_id" : ObjectId(id)})
            print(data_get)
        except Exception as e:
            print(e)
            return jsonify({"status":401, "messages": "invalide query data"})
        
        new_data_get = list(data_get)
        print(type(new_data_get))
        for item in new_data_get:
            item["_id"] = str(item["_id"])
            print(item)

        return jsonify({"status":200, "message": item })
      

class HandleRepoPutMethods :

    def put_method(self):
        try:
            id = "5d786d42857171c90d68282c"
            data_updates = db.storecar.update({"_id" : ObjectId(id)},{"$set" :{"id" : 3}})
            print(data_updates)
        except Exception as e :
            print(e)
            return jsonify({"status":403,"message" : "invalide update data"})
        
        return jsonify({"status":200})
