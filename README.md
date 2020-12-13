# web-scraping-challenge

### Step 1 - Scraping
- Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
- Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all the scraping and analysis tasks. 

#### NASA Mars News
- Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. 

#### PL Mars Space Images - Featured Image
- Used splinter to navigate the site and find the image url for the current Featured Mars Image.

#### Mars Facts
- Used Pandas to scrape the table containing facts about the planet.

#### Mars Hemispheres
- Used Pandas and the url string to find the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
- Appended the dictionary with the image url string and the hemisphere title to a list. 

### Step 2 - MongoDB and Flask Application
- Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped.

![Alt text](//Users/yaden/Desktop/web-scraping-challenge/mission_to_mars/Images/page1.png?raw=true "Title")


![alt text](/Users/yaden/Desktop/page2.png)
