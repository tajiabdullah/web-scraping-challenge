#####################################################
# Initiation
#####################################################


#Imports
from bs4 import BeautifulSoup
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd
import re
import requests
from IPython.display import Image


####################################################
# Mechanism to Open Webpage on Chrome
####################################################


def init_browser():
    #Passed the executable path as a dictionary to the **kwargs argument
    executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


###################################################
# Red Planet Science Web Scraping 
###################################################


def scrape():
    #Mechanism to open webpage on Chrome
    browser = init_browser()

    #Created variable for webpage
    science_url = "https://redplanetscience.com"
    #Visited webpage
    browser.visit(science_url)


    #Created variable for automated web testing
    science_html = browser.html
    #Used Beautiful Soup to parse through HTML
    science_bs = BeautifulSoup(science_html, "html.parser")
    #Used Prettify to enhance HTML readability
    print(science_bs.prettify())


    #Scraped the Mars news site and collected the latest news title and paragraph text
    #Assigned the text to variables for later reference
    science_title = science_bs.find("div", class_="content_title").text
    science_paragraph = science_bs.find("div", class_="article_teaser_body").text
    print(f"1. Latest News Title: {science_title}")
    print(f"2. Corresponding Paragraph Text: {science_paragraph}")


###################################################
# Mars Space Images Web Scraping
###################################################


    #Created variable for webpage
    space_url = "https://spaceimages-mars.com"
    #Visited webpage
    browser.visit(space_url)


    #Created variable for automated web testing
    space_html = browser.html
    #Used Beautiful Soup to parse through HTML
    space_bs = BeautifulSoup(space_html, "html.parser")
    #Used Prettify to enhance HTML readability
    print(space_bs.prettify())


    #Scraped the space images site and collected the all JPEGs
    jpeg_list = [item['src'] for item in space_bs.select("[src$='.jpg']")]
    print(jpeg_list)


    #Selected the first JPEG in the list using indexing
    #Assigned the JPEG to variable for later reference
    featured_image = [item['src'] for item in space_bs.select("[src$='.jpg']")][0]
    print(featured_image)


    #Printed full url of first JPEG
    featured_image_url = f"https://spaceimages-mars.com/{featured_image}"
    print(f"Complete URL String:\n{featured_image_url}")


###################################################
# Galaxy FACT Web Scraping
###################################################


    #Created variable for webpage
    facts_url = "https://galaxyfacts-mars.com"
    #Visited webpage
    browser.visit(facts_url)


    #Ensured that request succeeded
    response = requests.get(facts_url)
    response


    #Created variable for automated web testing
    facts_html = browser.html
    #Used Beautiful Soup to parse through HTML
    facts_bs = BeautifulSoup(space_html, "html.parser")
    #Used Prettify to enhance HTML readability
    print(space_bs.prettify())


    #Converted site into dataframe
    facts_df = pd.read_html(facts_html)
    facts_df


    #Created new dataframe for relevant table
    facts_df2 = facts_df[1]
    facts_df2


    #Inspected columns
    facts_df2.columns


    #Renamed columns
    facts_df2.columns=("Category", "Information")
    facts_df2


    #Converted table to HTML
    html_table = facts_df2.to_html(index=False)
    print(html_table)


    #Created HTML file and dropped Index
    facts_df2.to_html("table.html",index=False)


###################################################
# GUSS Science Center Webscraping
###################################################


    #Created variable for webpage
    astropedia_url = "https://marshemispheres.com/"
    #Visited webpage
    browser.visit(astropedia_url)


    #Created variable for automated web testing
    astropedia_html = browser.html
    #Used Beautiful Soup to parse through HTML
    astropedia_bs = BeautifulSoup(astropedia_html, "html.parser")
    #Used Prettify to enhance HTML readability
    print(astropedia_bs.prettify())


    #Discovered preliminary image links
    html_list = [item['href'] for item in astropedia_bs.select("[href$='.html']")]
    print(html_list)


    #Eliminated duplicates
    html_list = list(set(html_list))
    html_list


    #Added webpage index to the links of final images
    preliminary_url_list = []

    for item in html_list:
        complete_url = astropedia_url + item
        preliminary_url_list.append(complete_url)

    print(preliminary_url_list)


    #Accessed links to final images urls
    draft_url_list = []


    for item in preliminary_url_list:
        browser.visit(item)
        image_html = browser.html
        image_bs = BeautifulSoup(image_html, "html.parser")
        image_path = image_bs.select_one("ul")
        image_url = image_path.a["href"]
        draft_url_list.append(image_url)
    
    draft_url_list    


    #Added webpage index to the final image url
    final_url_list = []

    for item in draft_url_list:
        final_complete_url = astropedia_url + item
        final_url_list.append(final_complete_url)

    print(final_url_list)


    #Truncated HTML to search for subtitles
    subtitle_html = astropedia_bs.find_all("div", class_="description")

    subtitle_html


    #Created subtitle list
    subtitle_list = []
    
    for item in subtitle_html:
        subtitle = item.find("h3").text
        subtitle_list.append(subtitle)
        
    subtitle_list


    #Created dictionary consisting of subtitle and final image URL
    hemisphere_image_urls = []

    for url, title in zip(final_url_list, subtitle_list):
        hemisphere_image_dictionary = {}
        hemisphere_image_dictionary["Title"] = title
        hemisphere_image_dictionary["Image_URL"] = url
        hemisphere_image_urls.append(hemisphere_image_dictionary)
    
    hemisphere_image_urls 


###################################################
# Scrape Dictionary
###################################################


    mars_dictionary = {
        "Latest_News_Title" : science_title, 
        "Latest_New_Paragraph" : science_paragraph, 
        "Featured_Image" : featured_image_url,
        "Hemisphere_Images" : hemisphere_image_urls
    }

###################################################
# Close Out 
###################################################


    #Closed Browser
    browser.quit()


    #Returned results
    return(mars_dictionary)