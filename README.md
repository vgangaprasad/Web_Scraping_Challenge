# Web Scraping

![mission_to_mars](https://www.nasa.gov/sites/default/files/thumbnails/image/concept-gateway-2024-00004.jpg)

I recently learnt Web Scraping and thought of testing my skills by building a web application that scrapes multiple websites to collect data related to the Mission to Mars and display the information in a single HTML page. 


### Tools and Technologies used

1. Python
2. Jupyter Notebook
3. Beautiful Soup
4. Splinter
5. Pandas
6. MongoDB
7. Flask

### Websites and Data Gathered

* [NASA Mars News Site](https://mars.nasa.gov/news/) - to collect the latest News Title and information related to the corresponding Title. 
* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) - used spliter to navigate site and find the image url for the current Featured Mars Image
* [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en) - to scrape the latest Mars weather tweet from the page.
* [Mars Facts webpage](https://space-facts.com/mars/) - used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
