import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/")
@app.route("/add_plant")
def add_plant():
    categories = mongo.db.plants.find().sort("plant_category", 1)
    return render_template("add_plant.html", categories=categories)


@app.route("/")
@app.route("/all_plants")
def all_plants():
    all_plants = list(mongo.db.plants.find())
    return render_template("all_plants.html", all_plants=all_plants)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
