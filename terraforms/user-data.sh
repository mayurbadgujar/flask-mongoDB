#!/bin/bash

# Update and install dependencies
yum update -y
yum install -y python3 nodejs npm

# Install Flask (Python backend)
pip3 install flask

# Create a directory for the Flask app
mkdir -p /home/ec2-user/flask-app
cat <<EOF > /home/ec2-user/flask-app/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

# Start the Flask app
python3 /home/ec2-user/flask-app/app.py &

# Create a directory for the Express app
mkdir -p /home/ec2-user/express-app
cd /home/ec2-user/express-app

# Initialize a Node.js project and install Express
npm init -y
npm install express

# Create the Express app
cat <<EOF > /home/ec2-user/express-app/index.js
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from Express!');
});

app.listen(port, () => {
  console.log(\`Express app listening at http://localhost:\${port}\`);
});
EOF

# Start the Express app
node /home/ec2-user/express-app/index.js &