import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import re
import ssl

# Fix SSL issue on Mac
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download stopwords
nltk.download('stopwords')

# Load CSV
data = pd.read_csv('data/sample_sentiment_analysis.csv')

# Keep only necessary columns
data = data[['content', 'sentiment']]

# Preprocessing function
def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

# Clean text
data['clean_text'] = data['content'].apply(clean_text)

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    data['clean_text'], data['sentiment'], test_size=0.2, random_state=42
)

# Vectorize text
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Test accuracy
y_pred = model.predict(X_test_vec)
print("Test Accuracy:", accuracy_score(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and vectorizer saved successfully!")