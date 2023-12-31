import pandas as pd

auto = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\auto.csv')
healthandscience = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\healthandscience.csv')
invest = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\invest.csv')
politics = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\politics.csv')
tech = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\tech.csv')

news_classifier_df = pd.concat([auto,healthandscience,invest,politics,tech],axis=0)

# Saving to a CSV file
news_classifier_df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Data_Collection\Scraped_dataset\news_classifier_dataset.csv', index = False)
