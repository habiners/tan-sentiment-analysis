from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

ps = PorterStemmer()
sbstemmer = SnowballStemmer("english") # Better daw ni

from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# pip install --upgrade pip setuptools # Done
# pip install virtualenv # Done
# pip install flask
# pip install flask flask-jsonpify flask-sqlalchemy flask-restful flask-cors

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def greet():
    return jsonify({"text": "Welcome to the Sentiment Analysis Web Service!"})


class Sentiment_Analysis(Resource):
  def get(self, userInput):
    # print(userInput)
    tokenizedRow = userInput.split(' ')
    stemmed = ""
    for word in tokenizedRow:
        stemmed += (sbstemmer.stem(word) + " ")
    # print(stemmed)
    sentiment = analyzer.polarity_scores(stemmed)
    # print(sentiment)
    return jsonify(sentiment)

api.add_resource(Sentiment_Analysis, '/sentiment-analysis/<userInput>')

if __name__ == "__main__":
    app.run(port=5002)
