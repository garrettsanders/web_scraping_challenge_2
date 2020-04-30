from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'C:/web drivers/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)
    



def scrape_info():
    browser = init_browser()
    mars_data = {}
    
    nasa_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    executable_path = {'executable_path': 'C:/web drivers/chromedriver'}
    browser = Browser("chrome", **executable_path, headless=False)

    browser.visit(nasa_url)

    html = browser.html
    nasa_soup = bs(html, 'html.parser')

  #scrape news title
    nasa_title = nasa_soup.find("div",class_="content_title").text
    nasa_title
    

  #scrape paragraph
    nasa_paragraph = nasa_soup.find("div", class_="article_teaser_body").text

    nasa_paragraph

  #JPL Mars Space Images
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    executable_path = {'executable_path': 'C:/web drivers/chromedriver'}
    browser = Browser("chrome", **executable_path, headless=False)
    browser.visit(image_url)

    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    html = browser.html
    img_soup = bs(html, 'html.parser')

    img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    img_url_rel

    mars_image = f'https://jpl.nasa.gov{img_url_rel}'
    mars_image 


#twitter weather
    twitter_weather = "https://twitter.com/marswxreport?lang=en"

    executable_path = {'executable_path': 'C:/web drivers/chromedriver'}
    browser = Browser("chrome", **executable_path, headless=False)

    browser.visit(twitter_weather)
    html = browser.html

    soup_weather = bs(twitter_weather, 'html.parser')

    mars_weather = soup_weather.find("div", class_="css-1dbjc4n")

    mars_weather 
#mars facts dataframe
    facts_url = "https://space-facts.com/mars/"

    executable_path = {'executable_path': 'C:/web drivers/chromedriver'}
    browser = Browser("chrome", **executable_path, headless=False)

    browser.visit(facts_url)

    tables = pd.read_html(facts_url)
    tables

    facts_df = tables[0]
    facts_df

    mars_table = facts_df.to_html()
    mars_table

    final_mars_table = mars_table.replace('\n', '')

    final_mars_table

  #hemisphere data
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    executable_path = {'executable_path': 'C:/web drivers/chromedriver'}
    browser = Browser("chrome", **executable_path, headless=False)

    browser.visit(hemisphere_url)
  
    hemisphere_img_urls=[]


  
#HTML object
    hemisphere_html = browser.html

#Parse HTML with Beautiful Soup
    hemisphere_soup = bs(hemisphere_html, 'html.parser')

#Retreive all items that contain mars hemispheres information
    images = hemisphere_soup.find_all('div', class_='item')


  #loop through items stored
    for x in images:
       h3 = x.find('h3').text
       image_url = x.find('a', class_='itemLink product-item')['href']
    
       #image_soup = bs(image_url, 'html.parser')
    
       full_url = f'https://astrogeology.usgs.gov{image_url}'
    
     #append title and urls to list
    image_data = dict({"title": h3, "image_url": full_url})
    hemisphere_img_urls.append(image_data)

    hemisphere_img_urls

    return mars_data   