from flask import Flask, jsonify

# Create Flask application
app = Flask(__name__)

# Sample user data
users = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Aman"},
    {"id": 3, "name": "Priya"}
]

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

# Home page
@app.route("/")
def home():
    return "Welcome to our Shopping Application!"

# User functionality
@app.route("/users")
def get_users():
    return jsonify(users)

# Product functionality
@app.route("/products")
def get_products():
    return jsonify(products)

# Run application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
