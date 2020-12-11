from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars
collection = db.mars

@app.route("/")
def index():
    mars = collection.find_one({})
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def web_scrape():
    mars_data = scrape_mars.scrape()
    collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)