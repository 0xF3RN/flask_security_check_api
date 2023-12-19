from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from hashing import Hasher
import pwnedpasswords as pwdc

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/new"
mongo = PyMongo(app)


@app.route('/api/v2/add_password', methods=["POST"])
def api_add_data():
    collection = mongo.db.new
    json_data = request.get_json()
    try:
        if len(json_data) == 2 and all(field in json_data for field in ["username", "password"]):
            pass
    except Exception:
        return Response(f" [Error] Invalid JSON format", 400)
    try:
        if pwdc.check(json_data["password"]):
            return Response("[Error] This password is leaked", 400)
        hasher = Hasher(json_data["username"], json_data["password"])
        encrypted = str(hasher.get_hash())
        newdoc = {"username": json_data["username"], "password": encrypted}
        arg = {"password": encrypted}
        data = list(collection.find(arg))
        if not data:
            collection.insert_one(newdoc)
            return Response(f"[INFO] New user has been added", 200)
        return Response("[INFO] This user is already existing", 400)
    except Exception:
        return Response(f" [Error] Unknown", 500)


@app.route('/api/v2/check_password', methods=["GET"])
def check_password():
    collection = mongo.db.new
    json_data = request.get_json()
    try:
        if len(json_data) == 2 and all(field in json_data for field in ["username", "password"]):
            pass
    except Exception:
        return Response(f" [Error] Invalid JSON format", 400)
    try:
        hasher = Hasher(json_data["username"], json_data["password"])
        encrypted = str(hasher.get_hash())
        arg = {"password": encrypted}
        data = list(collection.find(arg))
        if not data:
            return Response(f"[INFO] This user doesn't exist", 200)
        return Response("[INFO] This user is already existing", 400)
    except Exception:
        return Response(f" [Error] Unknown", 500)


@app.route('/api/v2/remove_password', methods=["POST"])
def remove_password():
    collection = mongo.db.new
    json_data = request.get_json()
    try:
        if len(json_data) == 2 and all(field in json_data for field in ["username", "password"]):
            pass
    except Exception:
        return Response(f" [Error] Invalid JSON format", 400)
    try:
        hasher = Hasher(json_data["username"], json_data["password"])
        encrypted = str(hasher.get_hash())
        arg = {"password": encrypted}
        data = list(collection.find(arg))
        if not data:
            return Response(f"[INFO] This user doesn't exist", 400)
        collection.delete_one(arg)
        return Response("[INFO] Deleted", 200)
    except Exception:
        return Response(f" [Error] Unknown", 500)


if __name__ == '__main__':
    app.run(debug=True)
