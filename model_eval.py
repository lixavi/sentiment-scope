
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class ModelEvaluation:
    def __init__(self):
        pass

    def evaluate_model(self, true_labels, predicted_labels):
        accuracy = accuracy_score(true_labels, predicted_labels)
        precision = precision_score(true_labels, predicted_labels, average='weighted')
        recall = recall_score(true_labels, predicted_labels, average='weighted')
        f1 = f1_score(true_labels, predicted_labels, average='weighted')

        evaluation_results = {
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1 Score': f1
        }

        return evaluation_results
