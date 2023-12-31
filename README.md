# Automated News Classifier NLP

The "Automated News Classifier NLP" project is a natural language processing (NLP) application that leverages machine learning to automatically classify news headlines into different categories such as Technology, Automobile, Health and Science, Investing, and Politics. The system uses a trained model to predict the category of a given news headline based on its textual content.

## Features:

- Data Processing: Utilizes the spaCy library for text processing, including lowercasing, removing stop words, and lemmatization.

- Model Training: Trains a machine learning model (e.g., RandomForestClassifier) on a labeled dataset of news headlines to predict the corresponding category.

- Streamlit App: Implements a user-friendly web application using Streamlit, allowing users to input a news headline and receive the predicted category.

- Artifact Persistence: Saves the trained model and necessary preprocessing artifacts (e.g., vectorizer, model) using the pickle library for future use.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Automated_NewsClassifier_NLP.git
