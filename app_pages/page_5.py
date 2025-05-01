import streamlit as st
import os
from PIL import Image

def page5_body():
    st.title("Model Evaluation Metrics")
    st.markdown("---")

    # st.header("Confusion Matrix")
    # cm_img = Image.open("outputs/ml_visuals/confusion_matrix.png")
    # st.image(cm_img, caption="Confusion Matrix", use_container_width=True)

    st.markdown("### Confusion Matrix")
    cm_path = "outputs/ml_visuals/confusion_matrix.png"
    if os.path.exists(cm_path):
        cm_img = Image.open(cm_path)
        st.image(cm_img, caption="Confusion Matrix", use_container_width=True)
    else:
        st.info("Confusion matrix image not yet available _Coming soon..._")

    st.markdown("### Classification Report")
    # Add text or link to your classification report if available
    st.info("_Coming soon..._")

    # st.header("Classification Report")
    # cr_img = Image.open("outputs/ml_visuals/classification_report.png")
    # st.image(cr_img, caption="Precision, Recall, F1-Score", use_container_width=True)

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
    sample_img = Image.open("outputs/sample_predictions.png")
    st.image(sample_img, caption="Test Samples", use_container_width=True)

    st.success("Model performance looks promising based on these metrics and predictions.")
    