from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId for MongoDB

# Connect to MongoDB server
client = MongoClient("mongodb+srv://sief4136:sief2008@cluster0.xsqdvfg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['fitQuest']
users_collection = db['users']
exercises_collection = db['exercises']

def addUser(user):
    result = users_collection.insert_one(user)
    return result.inserted_id if result else None

def getUser(username):
    user = users_collection.find_one({"username": username})
    return user if user else None

def getUserById(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    return user if user else None

def editUser(user_id, update_fields):
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_fields})
    return result.modified_count > 0

def loadExercises():
    """ Load all exercises from the collection """
    exercises = exercises_collection.find()
    return list(exercises)

def loadFilteredExercises(weight, height, age, location):
    """Load exercises filtered by weight, height, age, and location."""
    query = {
        "min_weight": {"$lte": weight},
        "max_weight": {"$gte": weight},
        "min_height": {"$lte": height},
        "max_height": {"$gte": height},
        "min_age": {"$lte": age},
        "max_age": {"$gte": age}
    }

    if location != "All Locations":
        query["location"] = location

    exercises = exercises_collection.find(query)
    return list(exercises)