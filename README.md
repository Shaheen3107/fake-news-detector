# 📰 Fake News Detector

A Machine Learning + NLP web application that detects whether a news article is **Real or Fake** with a confidence score. Built using Python, Scikit-learn, and deployed with Streamlit.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-app-link.streamlit.app)  
*(Replace with your actual Streamlit Cloud URL after deployment)*

---

## 📌 Project Overview

Fake news has become a major problem in the digital age. This project builds a text classification model trained on thousands of real and fake news articles to automatically detect misinformation.

The model processes raw news text through an NLP pipeline and classifies it as **Fake** or **Real** along with a confidence percentage.

---

## 🧠 NLP & ML Pipeline

```
Raw Text → Preprocessing → TF-IDF Vectorization → Logistic Regression → Prediction
```

### Text Preprocessing Steps:
- Lowercasing
- URL removal (Regex)
- Punctuation & number removal
- Tokenization
- Stopword Removal
- Stemming (Porter Stemmer)

---

## 📊 Dataset

- **Source:** [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- **Size:** ~44,000 news articles
- **Classes:** Fake (0) | Real (1)
- **Features used:** Title + Article Text (combined)

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| NLP | NLTK (Tokenization, Stopwords, Stemming) |
| Vectorization | TF-IDF (Scikit-learn) |
| Model | Logistic Regression |
| Evaluation | Accuracy, Confusion Matrix, Classification Report |
| Deployment | Streamlit |
| Model Saving | Joblib |

---

## 📁 Project Structure

```
fake-news-detector/
│
├── app.py                        # Streamlit web application
├── fake_news_detector.ipynb      # Model training notebook
├── model.pkl                     # Trained Logistic Regression model
├── vectorizer.pkl                # Fitted TF-IDF Vectorizer
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Shaheen3107/fake-news-detector.git
cd fake-news-detector
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit app**
```bash
streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 📈 Model Performance

| Metric | Score |
|---|---|
| Accuracy | ~98% |
| Precision | ~98% |
| Recall | ~98% |
| F1 Score | ~98% |

---

## 💡 Key Concepts Covered

- Text Preprocessing & Cleaning
- Regular Expressions (Regex)
- Tokenization & Stopword Removal
- Stemming (Porter Stemmer)
- TF-IDF Vectorization
- Logistic Regression for Text Classification
- Model Serialization with Joblib
- Web App Deployment with Streamlit

---

## 🙋 Author

**Shaheen Akram**  
Aspiring Machine Learning & Data Science Engineer  
[GitHub](https://github.com/Shaheen3107) | [LinkedIn](www.linkedin.com/in/shaheen-akram-232696a3)