import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only once)
nltk.download("vader_lexicon")

# Initialize analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit app
st.title("Tweet Sentiment Analyser")
st.write("This tool classifies tweets as Positive, Negative, or Neutral using **NLTK**.")

# Text input
user_input = st.text_area("Enter your tweet here:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        scores = analyzer.polarity_scores(user_input)
        compound = scores['compound']

        if compound >= 0.05:
            sentiment = "Positive ✅"
        elif compound <= -0.05:
            sentiment = "Negative ❌"
        else:
            sentiment = "Neutral 😐"

        st.subheader("Results:")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Scores:** {scores}")
    else:
        st.warning("⚠️ Please enter some text to analyze.")