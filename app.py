from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

# ---- MongoDB Atlas Connection ----
# Replace with your own MongoDB Atlas connection string
MONGO_URI = "your_mongodb_atlas_connection_string"
client = MongoClient(MONGO_URI)
db = client["flaskdb"]
collection = db["users"]

# ---- /api Route ----
@app.route("/api")
def get_data():
    """Reads JSON data from file and returns it."""
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

# ---- Form Route ----
@app.route("/submit", methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        try:
            name = request.form["name"]
            age = int(request.form["age"])

            # Insert into MongoDB
            collection.insert_one({"name": name, "age": age})

            # Redirect on success
            return redirect(url_for("success"))
        except Exception as e:
            # Show error on same page
            return render_template("form.html", error=str(e))
    return render_template("form.html")

# ---- Success Route ----
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
