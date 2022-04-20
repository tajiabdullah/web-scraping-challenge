# Web Scraping Homework - Mission to Mars

![image](https://user-images.githubusercontent.com/95979913/163665737-6f8ce96e-c6dd-4630-a965-0a90d1770eb4.png)

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

## Step 1 - Scraping

I completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, which is in a Jupyter Notebook file called `mission_to_mars.ipynb`. My parameters were as follows. 

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. Assigned the text to variables  for later reference.

### JPL Mars Space Images - Featured Image

* Visited the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used splinter to navigate the site and found the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`.

* Made sure to find the image url to the full size `.jpg` image.

* Made sure to save a complete url string for this image.

### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and useed Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Useed Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name; and used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Started by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executes all code scraping from above and returns one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that imports the `scrape_mars.py` script, calls the `scrape` function, and stores the return value in Mongo as a Python dictionary.

* Created a root route `/` that queries the Mongo database and passes the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 

