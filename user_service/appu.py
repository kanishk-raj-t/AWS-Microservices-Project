
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Aman"},
    {"id": 3, "name": "Priya"}
]

@app.route("/")
def home():
    return "Welcome to User Service!"

@app.route("/users")
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

