import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class NLTKAnalyzer:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        # NLTK sentiment analysis implementation
        scores = self.sid.polarity_scores(text)
        compound_score = scores['compound']
        
        if compound_score >= 0.05:
            sentiment = 'positive'
        elif compound_score <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return sentiment
