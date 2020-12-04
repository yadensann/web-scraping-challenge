import pymongo
import requests
from splinter import Browser 
from bs4 import BeautifulSoup as bs 
import pandas as pd
import time 

# Database 
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_db
collection = db.mars

def init_browser():
    #Site Navigation
    executable_path = {"executable_path": "/Users/yaden/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    final_data = {}
    output = marsNews()
    final_data["Title"] = output[0]
    final_data["News"] = output[1]
    final_data["Featured Image"] = mars_img()
    final_data["Facts About Mars"] = mars_facts()
    final_data["Mars' Hemispheres"] = mars_hem()
    
    return final_data

    browser = init_browser()
    collection.drop()

def mars_news():
    #Latest News About Mars
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    news_html = browser.html
    news_soup = bs(news_html, 'lxml')
    title = news_soup.find('div', class_='content_title').text
    info = news_soup.find('div', class_= 'rollover_description_inner').text
    
    # Featured Image of Mars
def mars_img():
    link = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')
    image = soup.find('img', class_='thumb')['src']
    featured_image = "https://www.jpl.nasa.gov" + image
    return featured_image
    
    
    # Mars Facts
def mars_facts():
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    facts_html = browser.html
    facts_pandas = pd.read_html(facts_url)
    facts_df= pd.DataFrame(mars_data[0])
    facts_df.columns = ["Description", "Value"]
    facts_df = mars_data.set_index("Description")
    final_data = facts_df.to_html(index = True, header =True)
    return final_data

    # Mars Hemispheres
def mars_hem():
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hem_browser.visit(hemispheres_url)
    hem_html = browser.html
    hemisphere_soup = bs(html, "html.parser")
    mars_hemispheres= []
    hem_info = soup.find('div', class_= "item")
    hemispheres = products.find_all('div', class_ = 'item')
    
    for hemisphere in hemispheres:
        title = hemisphere.find('h3').text
        new_title = title.replace('Enhanced', '')
        reference = hemisphere.find('a')['href']
        hem_img = "https://astrogeology.usgs.gov/" + reference
        browser.visit(hem_img)
        html = browser.html
        hem_soup = bs(html, 'html', parser)
        downloads = soup.find('div', class_= 'downloads')
        img = downloads.find('a')['href']
        hem_dict = {'Title': title, 'Image URL': img}
        mars_hemispheres.append(dictionary)
    
    return mars_hemispheres