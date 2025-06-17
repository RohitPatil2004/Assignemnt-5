from flask import Flask, request, jsonify
from pymongo import MongoClient
from urllib.parse import quote_plus
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app)

username = quote_plus("rohitvpatil3")
password = quote_plus("Rohitpatil@1")
MONGO_URI = f"mongodb+srv://{username}:{password}@yd.nldhork.mongodb.net/?retryWrites=true&w=majority&appName=yd"

try:
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client["user_data"]
    collection = db['submissions']
except Exception as e:
    print(f"Error connecting to MongoDB: {e}", file=sys.stderr)
    sys.exit(1)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Missing required fields"}), 400
    collection.insert_one(data)
    return jsonify({"message": "Data saved successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
