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

# def scrape():
#     final_data = {}
#     output = marsNews()
#     final_data["Title"] = output[0]
#     final_data["News"] = output[1]
#     final_data["Featured Image"] = mars_img()
#     final_data["Facts About Mars"] = mars_facts()
#     final_data["Mars' Hemispheres"] = mars_hem()
    
def scrape():
    browser = init_browser()
    collection.drop()
    
    mars_data= {}
    
    
    
# def mars_news():
    #Latest News About Mars
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    time.sleep(1)

    news_html = browser.html
    news_soup = bs(news_html, 'lxml')
    article = news_soup.find('div', class_= 'list_text')
    news_title = article.find('div', class_= 'content_title').text
    news_info = article.find('div', class_= 'article_teaser_body').text
#     return news_title, news_info

    
    # Featured Image of Mars
# def feat_image():
    image_url = "https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA24247-640x350.jpg"
    browser.visit(image_url)


    time.sleep(1)

    html = browser.html
    image_soup = bs(html, 'html.parser')
    image = image_soup.find("img")['src']
    featured_image=image
    # featured_image = "https://www.jpl.nasa.gov" + image
#     return featured_image
    
    
    # Mars Facts
# def mars_facts():

    url = 'https://space-facts.com/mars/'
    browser.visit(url)


    time.sleep(1)

    data = pd.read_html(url)
    mars_df = pd.DataFrame(data[0])
#     facts = mars_df.to_html(header= False, index= False)
#     url = 'https://space-facts.com/mars/'
#     data = pd.read_html(url)
#     browser.visit(data)
#     facts_html = browser.html
#     mars_data = pd.DataFrame(data[0])    
    mars_df.columns = ["Description", "Value"]
    clean_df = mars_df.set_index("Description")
    facts = clean_df.to_html(header= False, index= False)    
#     return facts

    # Mars Hemispheres
# def mars_hem():
    hemispheres_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    
    time.sleep(1)

    hem_html = browser.html
    hemisphere_soup = bs(html, "html.parser")
    mars_hemispheres= []
    # hem_info = hemisphere_soup.find('div', class_= "item")
    hemispheres = hemisphere_soup.find_all('div', class_ = 'item')

    for hemisphere in hemispheres:
        browser.visit(hemispheres_url)
        hem_html = browser.html
        hem_soup= bs(hem_html, "html.parser")

        hem_titles = hem_soup.find('h3').text
        new_title = hem_titles.replace('Enhanced', '')

        ref_link = hem_soup.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + ref_link            

        downloads = hem_soup.find("div", class_="downloads")
        image_downloads = downloads.find("a")["href"]

        hem_dict = {'Title': new_title, 'Image URL': image_link}
        mars_hemispheres.append(hem_dict)

#     return mars_hemispheres

# Dictionary values:

    mars_data['news_url'] = news_url
    mars_data['news_title'] = news_title
    mars_data['news_info'] = news_info
    mars_data['featured_image'] = featured_image
    mars_data['facts'] = facts
    mars_data['hemisphere_images'] = mars_hemispheres
    
    browser.quit()

    return mars_data




    
# def scrape_all():
#     executable_path = {"executable_path": "/Users/yaden/Downloads/chromedriver"}
#     browser = Browser("chrome", **executable_path, headless=False)
#     news_title = mars_news(title)
#     mars_info = mars_news(info)
#     image = featured_image(browser)
#     facts = mars_facts(browser)
#     hemisphere_images = mars_hem(browser)

#     data = {
#         "title": title,
#         "info": info,
#         "image": featured_image,
#         "facts": facts,
#         "hemispheres": mars_hemispheres
#     }

#     return data 



    
