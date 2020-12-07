from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)



# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
# mongo = PyMongo(app)

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars
collection = db.mars.mars


@app.route("/")
def index():
    mars = list(db.collection.find())
#     mars_info = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def web_scrape():
#     db.collection.remove({})
    mars_data = scrape_mars.scrape()
#     db.collection.insert_one(mars_data).inserted_id
#     mongo.db.collection.insert_one(mars_data)
    
    mongo.db.collection.update({}, mars_data, upsert=True)
#     mars.update({}, mars_data, upsert=True)
    return redirect("/")
#     return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)