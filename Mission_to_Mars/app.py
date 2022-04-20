##################################################
# Dependencies
##################################################

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

##################################################
# Flask Initiation
##################################################

app = Flask(__name__)

##################################################
# MangoDB Initiation
##################################################

app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars_app"
mongo = PyMongo(app)

mars_data = mongo.db.mars_data.find_one()

##################################################
# Flask Routes
##################################################

@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars_data
    mars_new_data = scrape_mars.scrape()
    mars_data.update_one({}, {"$set": mars_new_data}, upsert=True)
    return redirect("/", code=302)

##################################################
# Close Out by Defining Main Behavior
##################################################
if __name__ == "__main__":
    app.run(debug=True)
    