from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient("mongodb-service", 27017, username='admin', password='admin')
db = client['bookstore']
collection = db['books']

@app.route('/books', methods=['GET'])
def get_books():
    books = list(collection.find())
    for book in books:
        book['_id'] = str(book['_id'])  # Convert ObjectId to string
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    result = collection.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)})

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"msg": "Book updated"})

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"msg": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
