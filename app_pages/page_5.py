import os
from PIL import Image
import streamlit as st

def page5_body():
    st.title("Model Evaluation Metrics")
    st.markdown("---")

    # Confusion Matrix
    st.markdown("### Confusion Matrix")
    cm_path = "/workspaces/PP5-Cherry-Leaves/outputs/figures/confusion_matrix.png"
    if os.path.exists(cm_path):
        cm_img = Image.open(cm_path)
        st.image(cm_img, caption="Confusion Matrix", use_container_width=True)
    else:
        st.info("Confusion matrix image not yet available _Coming soon..._")

    # Display Classification Report
    def display_file_content(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            st.error(f"File not found: {file_path}")
            return None

    st.markdown("### Classification Report")
    file_path = '/workspaces/PP5-Cherry-Leaves/outputs/reports/classification_report.txt'  # Adjust if needed
    file_content = display_file_content(file_path)
    if file_content:
        st.text(file_content)
    else:
        st.info("Classification report not yet available _Coming soon..._")

    # ROC Curve and AUC Score
    st.header("ROC Curve & AUC Score")
    roc_img_path = "/workspaces/PP5-Cherry-Leaves/outputs/training_plots/roc_curve.png"
    if os.path.exists(roc_img_path):
        roc_img = Image.open(roc_img_path)
        st.image(roc_img, caption="ROC Curve", use_container_width=True)
    else:
        st.info("ROC Curve image not yet available _Coming soon..._")

    st.markdown("""
    The AUC (Area Under the Curve) score indicates the model's ability to 
    distinguish between the two classes. An AUC closer to 1.0 signifies excellent performance.
    """)

    # Sample Predictions on Unseen Data
    st.header("Sample Predictions on Unseen Data")
    st.markdown("""
    Below is a sample batch of images along with predictions to see how the 
    model would perform on unseen data.
    """)
    sample_img_path = "/workspaces/PP5-Cherry-Leaves/outputs/figures/sample_predictions.png"
    if os.path.exists(sample_img_path):
        sample_img = Image.open(sample_img_path)
        st.image(sample_img, caption="Test Samples", use_container_width=True)
    else:
        st.info("Sample prediction images not yet available _Coming soon..._")

    st.success("Model performance looks promising based on these metrics and predictions.")
