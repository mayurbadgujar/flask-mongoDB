from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://mayurb17622:izHk1DasJFOEYBEL@cluster0.gruxr.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client.mydatabase
collection = db.mycollection

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')

        # Insert data into MongoDB
        data = {"name": name, "email": email}
        collection.insert_one(data)

        # Redirect to success page
        return redirect(url_for('success'))
    
    except Exception as e:
        # Display error on the same page
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Data submitted successfully!"


@app.route('/todo')
def todo():
    return render_template('todo.html')


@app.route('/submittodoitem', methods=["POST"])
def todoitem():
    itemName = request.form.get('itemName')
    description = request.form.get('itemDescription')

    # Insert data into MongoDB
    data = {"itemName": itemName, "itemDescription": description}
    collection.insert_one(data)

    # Redirect to success page
    return redirect(url_for('success'))

if __name__ == '__main__':
    app.run(debug=True)