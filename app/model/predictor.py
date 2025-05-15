import joblib
from app.core.config import settings
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import os


for resource in ["punkt", "punkt_tab"]:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load vectorizer
vectorizer_path = os.path.join(BASE_DIR, 'vectorizer.pkl')
vectorizer = joblib.load(vectorizer_path)

# Load model
model_path = os.path.join(BASE_DIR, 'model.pkl')
model = joblib.load(model_path)


ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)

def predict_spam(text: str) -> str:

    transformed_text = transform_text(text)
    # Transform the text using the loaded vectorizer
    features = vectorizer.transform([transformed_text])
    
    # Predict the sentiment using the loaded model
    prediction = model.predict(features)[0]  # Predict using trained model
    return "spam" if prediction == 1 else "not spam"