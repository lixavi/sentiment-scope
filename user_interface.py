from analysis.nltk_analyzer import NLTKAnalyzer
from analysis.spacy_analyzer import SpacyAnalyzer
from utils.data_manager import DataManager
from utils.data_visualization import DataVisualization

class UserInterface:
    def __init__(self):
        self.nltk_analyzer = NLTKAnalyzer()
        self.spacy_analyzer = SpacyAnalyzer()
        self.data_manager = DataManager()
        self.data_visualization = DataVisualization()

    def analyze_sentiment(self, text):
        nltk_sentiment, _ = self.nltk_analyzer.analyze_sentiment(text)
        spacy_sentiment, _ = self.spacy_analyzer.analyze_sentiment(text)

        print("Sentiment Analysis Results:")
        print("NLTK Analyzer:", nltk_sentiment)
        print("spaCy Analyzer:", spacy_sentiment)

        return nltk_sentiment, spacy_sentiment

    def visualize_sentiment_distribution(self, sentiments):
        self.data_visualization.plot_sentiment_distribution(sentiments)

    def load_text_from_file(self, file_path):
        return self.data_manager.read_text_file(file_path)

    def save_sentiment_results(self, file_path, nltk_sentiment, spacy_sentiment):
        results = f"NLTK Sentiment: {nltk_sentiment}\nspaCy Sentiment: {spacy_sentiment}"
        self.data_manager.save_text_file(file_path, results)
