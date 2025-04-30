import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


# This will be used to keep track of counts for each class to avoid duplication in keys.
class Counter:
    def __init__(self):
        self.counts = {}

    def get_count(self, label):
        if label not in self.counts:
            self.counts[label] = 0
        else:
            self.counts[label] += 1
        return self.counts[label]

counter = Counter()

def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
    data=[0.0, 0.0],  # Use floats instead of integers to avoid FutureWarning
    index={'Healthy': 0, 'Powdery Mildew': 1}.keys(),
    columns=['Probability']
)

    # Explicitly cast pred_proba to float to avoid dtype warning
    prob_per_class.loc[pred_class] = float(pred_proba)

    # Handle the other class (if not already assigned)
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
            
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    # Create a unique key using class label and a counter to handle duplicates
    unique_count = counter.get_count(pred_class)
    unique_key = f"plot_{pred_class}_{unique_count}_{int(time.time())}"

    # Plot the results with a dynamic key to avoid duplication issues
    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn'
    )
    st.plotly_chart(fig, key=unique_key)


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"/workspaces/PP5-Cherry-Leaves/outputs/image_shape_2.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images
    """

    model = load_model(f"/workspaces/PP5-Cherry-Leaves/outputs/cherry_leaf_model.h5")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'Healthy': 0, 'Powdery Mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the leaf is "
        f"**{pred_class.lower()}**."
    )

    return pred_proba, pred_class