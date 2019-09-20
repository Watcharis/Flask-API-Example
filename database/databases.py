from pymongo import MongoClient
class DatabasesCar :
    def data_spec_car(self):
        client = MongoClient('localhost:27017')
        db = client['speccar']
        return db



#spec_car = DatabasesCar()
#db = spec_car.data_spec_car()
#create_collection = db.storecar.insert_one({"id":1, "gen":"Hunydai"})
#serach_collection = db.storecar.find_one({"id":1})
#print(serach_collection)