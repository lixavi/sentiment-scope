class LexiconAnalyzer:
    def __init__(self, lexicon):
        self.lexicon = lexicon

    def analyze_sentiment(self, text):
        words = text.lower().split()
        sentiment_score = sum(self.lexicon.get(word, 0) for word in words)
        
        if sentiment_score > 0:
            sentiment = 'positive'
        elif sentiment_score < 0:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return sentiment
