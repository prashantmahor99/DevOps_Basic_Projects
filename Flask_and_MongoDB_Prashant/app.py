import os
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def get_collection():
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise RuntimeError("MONGO_URI is not configured. Add it to your .env file.")
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    db = client[os.getenv("MONGO_DB", "devops_assignment")]
    return db[os.getenv("MONGO_COLLECTION", "submissions")]


@app.route("/api", methods=["GET"])
def api():
    """Task 1: Return backend data as JSON."""
    data = {
        "project": "Flask & MongoDB DevOps Assignment",
        "status": "success",
        "message": "JSON API route is working",
        "technology": ["Flask", "MongoDB Atlas"]
    }
    return jsonify(data), 200

@app.route("/", methods=["GET", "POST"])
@app.route("/get", methods=["GET", "POST"])
@app.route("/post", methods=["GET", "POST"])
def index():
    """Task 2: Frontend form that stores submitted data in MongoDB Atlas."""
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            error = "All fields are required."
            return render_template("index.html", error=error, name=name, email=email, message=message)

        document = {"name": name, "email": email, "message": message}

        try:
            collection = get_collection()
            collection.insert_one(document)
            return redirect(url_for("success"))
        except (PyMongoError, RuntimeError) as exc:
            error = f"Unable to save data: {exc}"
            return render_template("index.html", error=error, name=name, email=email, message=message)

    return render_template("index.html", error=error)


@app.route("/success" , methods=["post", "get"])
def success():
    return render_template("success.html")

@app.route("/view", methods=["GET"])
def view():
    try:
        collection = get_collection()

        data = list(collection.find({}, {"_id": 0}))

        return jsonify(data)

    except (PyMongoError, RuntimeError) as exc:
        return jsonify({
            "error": f"Unable to fetch data: {exc}"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
