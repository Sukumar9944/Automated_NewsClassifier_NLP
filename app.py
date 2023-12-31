import streamlit as st
import pickle
import time
from Model_Training.processor import processing

# Setting Webpage Configurations
st.set_page_config(page_icon="⚙",page_title="Ai News Classifier", layout="wide")

st.title(':red[Classy AI] - Automated News Classifier🚀')

# Loading the model and the Vectorizer
model = pickle.load(open(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Artifacts\model.pkl', 'rb'))
vectorizer = pickle.load(open(r'F:\GUVI_DATA_SCIENCE\Project\Automated_NewsClassifier_NLP\Artifacts\vectorizer.pkl', 'rb'))

# 'Microsoft’s upcoming Surface lineup will feature a next-gen NPU: Report'
text = st.text_input('Enter your Headline')

# Text processing
processed_df = processing(text)

# Submit buttonb
submit = st.button('Classify')

if submit:
    with st.spinner('Please wait'):
        time.sleep(1)
     
    input_vectorized = vectorizer.transform(processed_df['Header'])
  
    input_prediction = model.predict(input_vectorized)

    if input_prediction == 0:
        input_prediction = 'Technology'

    elif input_prediction == 1:
        input_prediction = 'Automobile'

    elif input_prediction == 2:
        input_prediction = 'Health and Science'
    
    elif input_prediction == 3:
        input_prediction = 'Investing'
    
    elif input_prediction == 4:
        input_prediction = 'Politics'

    st.subheader(f':red[Section] : {input_prediction}')

    st.success('Done!')
