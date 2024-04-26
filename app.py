from flask import Flask, request
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def sentiment_analysis_endpoint():
    return "<p>Sentiment Analysis</p>"

@app.route("/analyze_sentiment", methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')

    # Perform sentiment analysis on the input text
    sentiment = analyze_sentiment_logic(text)
    
    return {'sentiment': sentiment}

def analyze_sentiment_logic(text):
    # Use TextBlob library for sentiment analysis
    analysis = TextBlob(text)
    
    # Determine sentiment polarity
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
