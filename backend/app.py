from flask import Flask, jsonify, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://mayurb17622:izHk1DasJFOEYBEL@cluster0.gruxr.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client.mydatabase
collection = db.mycollection

@app.route('/')
def index():
    cursor = collection.find()
    data = list(cursor)
    for item in data:
        item['_id'] = str(item['_id'])
    return jsonify(data)


@app.route('/submit', methods=["POST"])
def submit():
    try:
        # Insert data into MongoDB
        data = request.json
        collection.insert_one(data)

        # Redirect to success page
        return jsonify({"message": "Data submitted"}), 201
    
    except Exception as e:
        # Display error on the same page
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('index'))
    

@app.route('/todo', methods=["GET"])
def todo():
    cursor = collection.find()
    data = list(cursor)
    for item in data:
        item['_id'] = str(item['_id'])
    return jsonify(data)


@app.route('/submittodoitem', methods=["POST"])
def todoitem():
    data = request.json
    collection.insert_one(data)

    # Redirect to success page
    return jsonify({"message": "To-Do item added successfully!"}), 201

if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0', port=5000)