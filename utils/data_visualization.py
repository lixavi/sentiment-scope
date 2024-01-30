import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self):
        pass

    def plot_sentiment_distribution(self, sentiments):
        # Count the occurrences of each sentiment
        sentiment_counts = {sentiment: sentiments.count(sentiment) for sentiment in set(sentiments)}

        # Plotting the distribution
        labels = sentiment_counts.keys()
        counts = sentiment_counts.values()

        plt.figure(figsize=(8, 6))
        plt.bar(labels, counts, color=['green', 'blue', 'red'])
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.show()
