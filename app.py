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

"""
add route for home page
"""


@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


"""
This is route for add plant page with form
"""


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        wish_list = "on" if request.form.get(
            "plant_on_wish_list") else "no"
        plant = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("plant_name"),
            "plant_img": request.form.get("plant_img"),
            "plant_on_wish_list": wish_list,
            "plant_description": request.form.get("plant_description"),
            "plant_place": request.form.getlist("plant_place"),
            "plant_tips": request.form.get("plant_tips"),
            "plant_more_info": request.form.get("plant_more_info"),
            "plant_notes": request.form.getlist("plant_notes")
        }

        mongo.db.plants.insert_one(plant)
        flash("Plant Successfully Added.")
        return redirect(url_for("all_plants"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    places = mongo.db.places.find().sort("plant_places", 1)
    return render_template(
        "add_plant.html", categories=categories, places=places)





"""
route for all plants serching page
"""


@app.route("/")
@app.route("/all_plants")
def all_plants():
    places = mongo.db.places.find().sort("plant_places", 1)
    all_plants = list(mongo.db.plants.find())
    return render_template(
        "all_plants.html", all_plants=all_plants, places=places)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
