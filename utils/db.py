from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId for MongoDB

# Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")
db = client['fitQuest']
collection = db['users']

def addUser(user):
    result = collection.insert_one(user)
    return result.inserted_id if result else None

def getUser(username):
    user = collection.find_one({"username": username})
    return user if user else None

def getUserById(id):
    user = collection.find_one({"_id": ObjectId(id)})
    return user if user else None

def editUser(user_id, update_fields):
    result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_fields})
    return result.modified_count > 0
