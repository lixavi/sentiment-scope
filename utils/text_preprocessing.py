import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

class TextPreprocessor:
    def __init__(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def preprocess_text(self, text):
        # Tokenization
        tokens = word_tokenize(text.lower())

        # Remove punctuation and stopwords
        filtered_tokens = [token for token in tokens if token not in string.punctuation and token not in self.stop_words]

        # Stemming
        stemmed_tokens = [self.stemmer.stem(token) for token in filtered_tokens]

        return stemmed_tokens
