# Automated News Classifier NLP

"Automated News Classifier NLP" is a tool that classifies news headlines (Technology, Automobile, Health and Science, Investing, Politics) using machine learning. It leverages Selenium for dynamic web scraping , ensuring the model is trained on up-to-date and diverse news data and text preprocessing is done using Spacy Library.

## Features:

- Data Collection: The Data is Scraped dynamically using Selenium

- Data Processing: Utilizes the spaCy library for text processing, including lowercasing, removing stop words, and lemmatization.

- Model Training: Trains a machine learning model (e.g., RandomForestClassifier) on a labeled dataset of news headlines to predict the corresponding category.

- Streamlit App: Implements a user-friendly web application using Streamlit, allowing users to input a news headline and receive the predicted category.

- Artifact Persistence: Saves the trained model and necessary preprocessing artifacts (e.g., vectorizer, model) using the pickle library for future use.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Automated_NewsClassifier_NLP.git

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:

   ```bash
   streamlit run app.py

## Usage

- Enter a news headline in the text input box.
- Click the "Classify" button to see the predicted category.

## Files and Directories

- Data_Collection/: Contains the code which is used for Selenium web scraping
- Datasets/: Contains the datasets used for model training
- Model_Training/: Contains code for data processing and model training.
- Artifacts/: Stores the saved model and vectorization artifacts.
- Data_preprocessing/: Contains the code for text preprocessing using Spacy module
- app.py: Includes the Streamlit web application code.
- Workflow.txt: contains the Basic workflow for the projects
