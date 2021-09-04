# web-scraping-challenge
This challenge builds a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what was done.

Step 1 - Scraping

A complete initial scraping was done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

A Jupyter Notebook file called mission_to_mars.ipynb was created and used to complete all of the scraping and analysis tasks. The following outlines what was scraped.


-NASA Mars News

Scraped the Mars News Site and collected the latest News Title and Paragraph Text . Assigned the text to variables that can referenced later.


-JPL Mars Space Images - Featured Image

Featured Space Image site was visited

Using splinter to navigate the site and found the image url for the current Featured Mars Image and assigned the url string to a variable called featured_image_url.


-Mars Facts

The Mars Facts webpage here was visited and Pandas was used to scrape the table containing facts about the planet including Diameter, Mass, etc.

Using Pandas the data was converted to a HTML table string.


-Mars Hemispheres

The astrogeology site was visited to obtain high resolution images for each of Mar's hemispheres.

Using each of the links to the hemispheres the image url to the full resolution image was found.

The image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name was saved. Using a Python dictionary the data was stored using the keys img_url and title.

The dictionary with the image url string and the hemisphere title was appended to a list. This list contains one dictionary for each hemisphere.


Step 2 - MongoDB and Flask Application

Using MongoDB with Flask template, a new HTML page was created that displays all of the information that was scraped from the URLs above.

The Jupyter notebook was converted into a Python script called scrape_mars.py with a function called scrape that executes all of the scraping code from above and return one Python dictionary containing all of the scraped data.

Next, a route called /scrape was created that will import the scrape_mars.py script and call the scrape function.

The return value was stored in Mongo as a Python dictionary.

A root route / was created that queries the Mongo database and passes the mars data into an HTML template to display the data.

A template HTML file called index.html was created that takes the mars data dictionary and displays all of the data in the appropriate HTML elements.


