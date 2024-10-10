# web-scraper
This is a Python-based web scraper tool that extracts product prices, images, and reviews from websites. It uses Selenium for browser automation and BeautifulSoup for parsing the HTML content. The tool includes a graphical user interface (GUI) built with Tkinter for ease of use.

**Features**
1.Scrapes product details like names, prices, and images.
2.Displays scraped data in a scrollable text box.
3.Provides a user-friendly interface with buttons for scraping and exiting.
4.Option to run the scraper in headless mode (no browser UI).




**Requirements**
1.Python 3.x
2.Tkinter
3.Selenium
4.BeautifulSoup
5.Requests
6.PIL (Python Imaging Lib
7.WebDriver Manager



**Installation**
Clone the repository:
bash
Copy code
git clone <repository_url>
Install required libraries:
bash
Copy code
pip install selenium beautifulsoup4 requests pillow tkinter webdriver-manager
Usage
Run the application:
bash
Copy code
python scraper_tool.py
Enter a valid URL into the text box.
Click the Scrape button to retrieve data.
Scraped product information will be displayed in the text area, and images will be shown in the GUI.
