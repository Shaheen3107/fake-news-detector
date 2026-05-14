import streamlit as st
import joblib
import re
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load model and vectorizer

st.set_page_config(page_title="Fake News Detector", page_icon="📰")

model = joblib.load(r"C:\Users\shahe\Machine Learning\NLP\Fake News Detector\model.pkl")
vectorizer = joblib.load(r"C:\Users\shahe\Machine Learning\NLP\Fake News Detector\vectorizer.pkl")

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# UI

st.title("📰 Fake News Detector")
st.write("Enter a news article below to check if it's Real or Fake.")

user_input = st.text_area("Paste news article here", height=200)

if st.button("Check News"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = preprocess(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        probability = model.predict_proba(vectorized)[0]

        if prediction == 1:
            st.success(f"✅ This news appears to be REAL")
            st.write(f"Confidence: {round(probability[1]*100, 2)}%")
        else:
            st.error(f"🚨 This news appears to be FAKE")
            st.write(f"Confidence: {round(probability[0]*100, 2)}%")