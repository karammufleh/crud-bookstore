from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = "mongodb://admin:admin@localhost:27017"

try:
    client = MongoClient(MONGO_URI)
    print("Connected to MongoDB successfully!")
    print("Databases:", client.list_database_names())
except Exception as e:
    print("Failed to connect to MongoDB:", str(e))
