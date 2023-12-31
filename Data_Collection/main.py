from web_scrapper import scrape

# define the url
url = 'https://www.cnbc.com/technology/'

# Technology
tech_df = scrape(url,'Technology', 7)

# Saving to a CSV
tech_df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\tech.csv', index = False)

'-------------------------------------------------------------------------------------------------------------------------'

# define the url
url = 'https://www.cnbc.com/politics/'

# Politics
politics_df = scrape(url,'Politics', 7)

# Saving to a CSV
politics_df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\politics.csv', index = False)

'-------------------------------------------------------------------------------------------------------------------------'

# define the url
url = 'https://www.cnbc.com/investing/'

# Investing
invest_df = scrape(url,'Investing', 7)

# Saving to a CSV
invest_df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\invest.csv', index = False)

'-------------------------------------------------------------------------------------------------------------------------'

# define the url
url = 'https://www.cnbc.com/health-and-science/'

# Health and Science
health_science_df = scrape(url,'Health_and_Science', 7)

# Saving to a CSV
health_science_df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\healthandscience.csv', index = False)

'-------------------------------------------------------------------------------------------------------------------------'

# define the url
url = 'https://www.cnbc.com/autos/'

# Automobile
auto_df = scrape(url,'Automobile', 7)

# Saving to a CSV
auto_df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\auto.csv', index = False)

'-------------------------------------------------------------------------------------------------------------------------'