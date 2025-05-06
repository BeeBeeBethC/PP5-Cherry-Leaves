import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


def page5_body():
    st.title("Model Evaluation Metrics")
    st.markdown("---")

    st.markdown("### Confusion Matrix")
    cm_path = "/workspaces/PP5-Cherry-Leaves/outputs/figures/confusion_matrix.png"
    if os.path.exists(cm_path):
        cm_img = Image.open(cm_path)
        st.image(cm_img, caption="Confusion Matrix", use_container_width=True)
    else:
        st.info("Confusion matrix image not yet available _Coming soon..._")

    st.markdown("### Classification Report")
    # Path to the classification report text file
    file_path = "/workspaces/PP5-Cherry-Leaves/outputs/reports/classification_report.txt"

    # Read the .txt file content
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
        st.text(file_content)  # You can use st.markdown if you'd like to keep formatting
    except FileNotFoundError:
        st.error(f"❌ The file {file_path} was not found.")

    st.header("ROC Curve & AUC Score")
    roc_img = Image.open("outputs/training_plots/roc_curve.png")
    st.image(roc_img, caption="ROC Curve", use_container_width=True)

    st.markdown("""
    The AUC (Area Under the Curve) score indicates the model's ability to 
                distinguish between the two classes.
    An AUC closer to 1.0 signifies excellent performance.
    """)

    st.header("Sample Predictions on Unseen Data")
    st.markdown("""
    Below is a sample batch of images along with predicitions to see how the 
                model would perform on unseen data.
    """)
    sample_img = Image.open("/workspaces/PP5-Cherry-Leaves/outputs/figures/sample_predictions.png")
    st.image(sample_img, caption="Test Samples", use_container_width=True)

    st.success("Model performance looks promising based on these metrics and predictions.")
    