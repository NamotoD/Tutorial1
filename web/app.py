from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.RentalAPI
rentals = db["Rentals"]

rentals.delete_many({})
rentals.insert({
      'type': 'rentals',
      'id': 'grand-old-mansion',
      'attributes': {
        'title': "Grand Old Mansion",
        'owner': "Veruca Salt",
        'city': "San Francisco",
        'category': "Estate",
        'bedrooms': 15,
        'image': "https://upload.wikimedia.org/wikipedia/commons/c/cb/Crane_estate_(5).jpg",
        'description': "This grand old mansion sits on over 100 acres of rolling hills and dense redwood forests."
      }
    })
rentals.insert(
    {
      'type': 'rentals',
      'id': 'urban-living',
      'attributes': {
        'title': "Urban Living",
        'owner': "Mike Teavee",
        'city': "Seattle",
        'category': "Condo",
        'bedrooms': 1,
        'image': "https://upload.wikimedia.org/wikipedia/commons/0/0e/Alfonso_13_Highrise_Tegucigalpa.jpg",
        'description': "A commuters dream. This rental is within walking distance of 2 bus stops and the Metro."
      }
})
rentals.insert(
    {
      'type': 'rentals',
      'id': 'downtown-charm',
      'attributes': {
        'title': "Downtown Charm",
        'owner': "Violet Beauregarde",
        'city': "Portland",
        'category': "Apartment",
        'bedrooms': 3,
        'image': "https://upload.wikimedia.org/wikipedia/commons/f/f7/Wheeldon_Apartment_Building_-_Portland_Oregon.jpg",
        'description': "Convenience is at your doorstep with this charming downtown rental. Great restaurants and active night life are within a few feet."
      }
})

class GetRentals(Resource):
    def get(self):
        data = dumps(rentals.find())
        retJson = {
            'data': data
        }
        return jsonify(retJson)

class GetRentalById(Resource):
    #postedData = request.get_json()
    #id = postedData['id']
    def get(self, id):
        data = dumps(rentals.find({'id': id}))
        retJson = {
            'data': data
        }
        return jsonify(retJson)
    def delete(self, id):
        rentals.delete_one({'id': id})

api.add_resource(GetRentals, '/rentals')
api.add_resource(GetRentalById, '/rentals/<string:id>')

if __name__=="__main__":
    app.run(host='0.0.0.0')
