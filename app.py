import os
from flask import (
    Flask, flash, render_template,
    redirect, request, url_for)
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
@app.route("/index")
def index():
    return render_template("index.html", page_title="Home")


"""
route to select and browse all plants in plantarium db
"""


@app.route("/all_plants")
def all_plants():
    plants = mongo.db.plants.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    places = mongo.db.places.find().sort("plant_places", 1)
    return render_template(
        "all_plants.html", categories=categories, places=places, plants=plants)


"""
route to browse plants by plant_place category
"""
""
@app.route("/browse_place/<plant_place>")
def browse_place(plant_place):
    categories = mongo.db.categories.find()
    places = mongo.db.places.find().sort("plant_places", 1)
    return render_template(
        "browse_place.html", categories=categories, places=places)



"""
route for browse plant by plant_id
"""


@app.route("/browse_plants/<plant_id>")
def browse_plantns(plant_id):

    categories = mongo.db.categories.find_one()
    places = mongo.db.places.find()
    return render_template("browse_plants.html", categories=categories, places=places)


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
            "plant_notes": request.form.getlist("plant_notes")
        }

        mongo.db.plants.insert_one(plant)
        flash("Plant Successfully Added.")
        return redirect(url_for("index"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    places = mongo.db.places.find().sort("plant_places", 1)
    return render_template(
        "add_plant.html", categories=categories, places=places)


"""
This route is for edit plant
"""


@app.route("/edit_plant/<plant_id>", methods=["GET", "POST"])
def edit_plant(plant_id):
    if request.method == "POST":
        wish_list = "on" if request.form.get(
            "plant_on_wish_list") else "no"
        submit = {
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

        mongo.db.plants.update({"_id": ObjectId(plant_id)}, submit)
        flash("Plant Successfully Updated.")
    plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    places = mongo.db.places.find().sort("plant_places", 1)
    return render_template(
        "edit_plant.html", categories=categories, plant=plant, places=places)


"""
This is route to delete a single plant from database
"""


@app.route("/delete_plant/<plant_id>")
def delete_plant(plant_id):
    mongo.db.plant.remove({"_id": ObjectId(plant_id)})
    flash("Plant Successfully Removed.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
