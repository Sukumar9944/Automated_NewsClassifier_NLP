# Importing the webdriver
from selenium import webdriver

# For implicit wait
import time
    
# For Data Processing
import pandas as pd

# To find elements
from selenium.webdriver.common.by import By

# To solve browser automatically closing problem
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Define a Driver
driver = webdriver.Chrome(options = options)

# Minimize the browser window
driver.maximize_window()

def scrape(url, section, pages):
    # Fetch the url using the driver
    driver.get(url)

    # Fetching the Data from CNBC
    load_more = driver.find_element(By.CLASS_NAME, 'LoadMoreButton-loadMore')

    for i in range(pages):
        load_more.click()
        time.sleep(5)

    news_header = driver.find_elements(By.CLASS_NAME, 'Card-title')

    news_data = []

    for i in news_header:
        news_data.append({'Header':i.text, 'Section':section})

    news_df = pd.DataFrame(data = news_data, columns = ['Header', 'Section'])
    print(news_df)

    print('The number of News Scraped:', len(news_data))

    time.sleep(5)

    driver.close()

    return news_df