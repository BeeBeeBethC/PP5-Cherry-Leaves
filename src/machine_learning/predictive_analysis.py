import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.preprocessing.image import load_img, img_to_array

class PredictiveAnalysis:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.image_shape = (100, 100)  # Standard size for leaf images
        
    def process_image(self, image_path):
        """Process image for prediction"""
        img = load_img(image_path, target_size=self.image_shape)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize
        return img_array
        
    def predict(self, image_path):
        """Predict if leaf has powdery mildew"""
        processed_image = self.process_image(image_path)
        prediction = self.model.predict(processed_image)
        return prediction[0][0]  # Return probability

# helper function for Streamlit use
def load_model_and_predict(img, version='v1'):
    model = tf.keras.models.load_model('/workspaces/PP5-Cherry-Leaves/outputs/v13/cherry_leaf_model.keras')

    # Resize and normalize image
    img = img.resize((100, 100))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Predict
    pred_proba = model.predict(img_array)[0][0]
    pred_class = "healthy" if pred_proba < 0.5 else "powdery_mildew"
    
    return pred_proba, pred_class

def resize_input_image(img, version='v1'):
    """Resize image based on version (e.g., for different input sizes)"""
    if version == 'v1':
        img_resized = img.resize((100, 100))  # Standard size for v1
    else:
        img_resized = img.resize((150, 150))  # Change size for other versions
    return img_resized

def plot_predictions_probabilities(pred_proba, pred_class):
    """Plot the predictions and probabilities"""
    labels = ['Healthy', 'Powdery Mildew']
    probabilities = [1 - pred_proba, pred_proba]
    
    # Plot the bar chart for the probabilities
    plt.bar(labels, probabilities, color=['green', 'red'])
    plt.title(f"Prediction: {pred_class.capitalize()} (Probability: {pred_proba*100:.2f}%)")
    plt.ylabel("Probability")
    plt.ylim([0, 1])
    plt.show()