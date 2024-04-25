from flask import Flask

app = Flask(__name__)

@app.route("/")
def sentiment_analysis():
    # CODE HERE
    return "<p>Sentiment Analysis</p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)