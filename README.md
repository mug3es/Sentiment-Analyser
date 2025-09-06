Twitter Sentiment Analysis (NLTK + Streamlit)

This project is a simple sentiment analysis tool that classifies text into Positive, Negative, or Neutral using the VADER sentiment analyzer available in the Natural Language Toolkit (NLTK). A lightweight web interface is built with Streamlit.

Features
	•	Uses NLTK’s VADER model, which is designed for short, informal text such as tweets.
	•	Classifies text into three categories: Positive, Negative, Neutral.
	•	Runs in a web browser through Streamlit.
	•	Easy to install and run locally.

Installation
	1.	Clone this repository:
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
	2.	Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
	3.	Install dependencies:
pip install -r requirements.txt
	4.	Download the required NLTK data (only needed once):
import nltk
nltk.download(“vader_lexicon”)

Usage

Run the application with:
streamlit run app.py

The app will start a local server, usually accessible at http://localhost:8501

Example

Input:
Crime has increased in the city

Output:
Sentiment: Negative

Project Structure

app.py              - Streamlit application
requirements.txt    - Dependencies
README.md           - Documentation

Acknowledgments
	•	NLTK: Natural Language Toolkit
	•	Streamlit: Python framework for web apps