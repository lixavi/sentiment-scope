class SentimentComparison:
    def __init__(self):
        pass

    def compare_sentiments(self, sentiment1, sentiment2):
        if sentiment1 == sentiment2:
            return "Sentiments are the same."
        else:
            return "Sentiments are different."

    def compare_multiple_texts(self, texts, analyzers):
        sentiments = [analyzer.analyze_sentiment(text) for text, analyzer in zip(texts, analyzers)]
        comparison_results = []

        for i in range(len(sentiments) - 1):
            for j in range(i + 1, len(sentiments)):
                comparison_results.append(self.compare_sentiments(sentiments[i], sentiments[j]))

        return comparison_results
