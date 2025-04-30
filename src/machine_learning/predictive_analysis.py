
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

class PredictiveAnalysis:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.image_shape = (256, 256)  # Standard size for leaf images
        
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