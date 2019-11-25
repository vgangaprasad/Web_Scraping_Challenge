import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import time

def scrape_mars():

  # NASA News
  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)
  news_result = requests.get("https://mars.nasa.gov/news/")
  news_src = news_result.content
  soup = BeautifulSoup(news_src, 'lxml')
  title = soup.find('div', class_='content_title').find('a').text
  news_p = soup.find('div', class_='rollover_description').text

  # Scrape JPL Mars Space Images -- Featured Image
  images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
  browser.visit(images_url)
  html = browser.html
  images_soup = BeautifulSoup(html, 'lxml')
  image_link = images_soup.find('div', class_='carousel_items')
  image_alt = image_link.article['alt']
  base_url = "https://www.jpl.nasa.gov"
  image_url = base_url + image_link.article.a['data-fancybox-href']
  browser.quit()

  #Scrape Mars Weather Twitter account. 
  twitter_browser = Browser('chrome', **executable_path, headless=False)
  twitter_url = "https://twitter.com/marswxreport?lang=en"
  twitter_browser.visit(twitter_url)
  twitter_html = twitter_browser.html
  twitter_soup = BeautifulSoup(twitter_html, 'lxml')
  mars_weather = twitter_soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
  twitter_browser.quit()

  #Scrape Space Facts Mars page
  # Use Pandas
  space_browser = Browser('chrome', **executable_path, headless=False)
  space_url = "https://space-facts.com/mars/"
  space_browser.visit(space_url)
  space_html = space_browser.html
  space_soup = BeautifulSoup(space_html, 'lxml')
  space_table = space_soup.find('table', class_="tablepress tablepress-id-p-mars")
  mars_df = pd.read_html(space_url)[0]
  mars_df.columns = ['Characteristic', 'Fact']
  mars_html = mars_df.to_html()
  space_browser.quit()


  #Scrape USGS Astrogeology site for images of Mars' hemispheres
  USGS_browser = Browser('chrome', **executable_path, headless=False)
  USGS_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
  main_url = 'https://astrogeology.usgs.gov'
  USGS_browser.visit(USGS_url)
  USGS_html = USGS_browser.html
  USGS_soup = BeautifulSoup(USGS_html, 'lxml')
  
  hemisphere_image_urls = []
  USGS_hemis_a = USGS_soup.find_all('div', class_="item")
  main_url = "https://astrogeology.usgs.gov"
  for hemi in USGS_hemis_a:
    USGS_title = hemi.h3.text[:-9]
    USGS_hemi_url = main_url+hemi.a['href']
    USGS_browser.visit(USGS_hemi_url)
    USGS_img_html = USGS_browser.html
    USGS_img_soup = BeautifulSoup(USGS_img_html, 'html.parser')
    #print(USGS_img_soup)
    part_url = USGS_img_soup.find('img', class_='wide-image')['src']
    USGS_img_url = main_url + part_url
    hemi_dict = {"title":USGS_title,"img_url": USGS_img_url}
    hemisphere_image_urls.append(hemi_dict)
  USGS_browser.quit()



  ## Make results dictionary

  Mars_dict = {"Headline": title, \
               "Summary": news_p, \
               "ImageURL": image_url, \
               "Weather": mars_weather, \
               "Mars_Facts": mars_html, \
               "HD": hemisphere_image_urls}

  print(Mars_dict)
  return Mars_dict