
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

class ModelEvaluator:
    def __init__(self, model):
        self.model = model
        
    def evaluate_model(self, X_test, y_test):
        """Evaluate model performance"""
        predictions = self.model.predict(X_test)
        pred_classes = (predictions > 0.5).astype(int)
        
        metrics = {
            'accuracy': accuracy_score(y_test, pred_classes),
            'precision': precision_score(y_test, pred_classes),
            'recall': recall_score(y_test, pred_classes),
            'f1': f1_score(y_test, pred_classes)
        }
        
        return metrics
        
    def plot_training_history(self, history):
        """Plot training metrics"""
        plt.figure(figsize=(12, 4))
        
        plt.subplot(1, 2, 1)
        plt.plot(history.history['accuracy'], label='Training Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        
        plt.subplot(1, 2, 2)
        plt.plot(history.history['loss'], label='Training Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        
        plt.tight_layout()
        plt.savefig('outputs/training_plots/model_training_metrics.png')
        plt.close()
