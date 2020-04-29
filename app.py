from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars_db")

@app.route("/")
def index():
    mars_data = mongo.db.mission_to_mars_db.find_one()
    return render_template("index.html", data=mars_data)

@app.route("/scrape")
def scrape():
    mars_info = scrape_mars.scrape_info()
    mars_info = scrape_mars.scrape_images()
    mars_info = scrape_mars.scrape_twitter()
    mars_info = scrape_mars.scrape_dataframe()
    mars_info = scrape_mars.scrape_hemisphere()

    mongo.db.collection.update({}, mars_info, upsert=True)

    return redirect("/")

    if __name__ == '__main__':
        app.run(debug=True)


