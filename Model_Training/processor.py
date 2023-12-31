import spacy
import re
import pandas as pd


def processing(text):

    processing = spacy.load('en_core_web_md')
    
    corpus = []

    # Replacing numbers and Special Characters with whitespace
    news = re.sub('[^a-zA-Z\s]', '', text)

    # Convert the String to lowercase
    news = news.lower()

    # Removing Stop word and Lemmatisation
    doc = processing(news)
    
    news = [token.lemma_ for token in doc if not token.is_stop]
    news = ' '.join(news)

    corpus.append({'Header':news})

    processed_header = pd.DataFrame(data = corpus, columns = ['Header'])

    return processed_header
