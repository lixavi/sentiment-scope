# main.py
from sentiment_analysis.nltk_sentiment import nltk_analyze
from sentiment_analysis.spacy_sentiment import spacy_analyze
from text_processing.text_preprocessing import preprocess_text

def main():
    # Read text from a file
    with open("data/sample_text.txt", "r") as file:
        text = file.read()

    # Preprocess the text
    preprocessed_text = preprocess_text(text)

    # Perform sentiment analysis using NLTK
    nltk_result = nltk_analyze(preprocessed_text)
    print("NLTK Sentiment:", nltk_result)

    # Perform sentiment analysis using spaCy
    spacy_result = spacy_analyze(preprocessed_text)
    print("spaCy Sentiment:", spacy_result)

if __name__ == "__main__":
    main()
