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
    browser = init_browser()
    collection.drop()
    
    mars_data= {}


    #Latest News About Mars
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    time.sleep(1)
    news_html = browser.html
    news_soup = bs(news_html, 'lxml')
    article = news_soup.find('div', class_= 'list_text')
    news_title = article.find('div', class_= 'content_title').text
    news_info = article.find('div', class_= 'article_teaser_body').text

    # Featured Image of Mars
    image_url = "https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA24247-640x350.jpg"
    browser.visit(image_url)
    time.sleep(1)
    html = browser.html
    image_soup = bs(html, 'html.parser')
    image = image_soup.find("img")['src']
    featured_image=image

    # Mars Facts
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(1)
    data = pd.read_html(url)
    mars_df = pd.DataFrame(data[0])
    mars_df.columns = ["Description", "Value"]
    clean_df = mars_df.set_index("Description")
    facts = clean_df.to_html(header= False, index= False)    

    # Mars Hemispheres
    hemispheres_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(1)

    first = browser.find_by_tag('h3')[0].text
    second = browser.find_by_tag('h3')[1].text
    third = browser.find_by_tag('h3')[2].text
    fourth = browser.find_by_tag('h3')[3].text

    browser.find_by_css('.thumb')[0].click()
    first_img = browser.find_by_text('Sample')['href']
    browser.back()

    browser.find_by_css('.thumb')[1].click()
    second_img = browser.find_by_text('Sample')['href']
    browser.back()

    browser.find_by_css('.thumb')[2].click()
    third_img = browser.find_by_text('Sample')['href']
    browser.back()

    browser.find_by_css('.thumb')[3].click()
    fourth_img = browser.find_by_text('Sample')['href']

    hemisphere_image_urls = [
    {'title': first, 'img_url': first_img},
    {'title': second, 'img_url': second_img},
    {'title': third,  'img_url': third_img},
    {'title': fourth, 'img_url': fourth_img}
    ]

# Dictionary values:
    mars_data['news_url'] = news_url
    mars_data['news_title'] = news_title
    mars_data['news_info'] = news_info
    mars_data['featured_image'] = featured_image
    mars_data['facts'] = facts
    mars_data['hemisphere_images'] = hemisphere_image_urls
    
    browser.quit()

    return mars_data

