import os
import pandas as pd
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

    def display_classification_report():
        # Path to the classification report CSV file
        csv_path = "/workspaces/PP5-Cherry-Leaves/outputs/saved_results/classification_report.csv"

        # Check if the CSV file exists
        if os.path.exists(csv_path):
            # Load the CSV file into a pandas DataFrame
            class_report_df = pd.read_csv(csv_path)

            # Display the classification report as a table in Streamlit
            st.markdown("### Classification Report")
            st.dataframe(class_report_df, use_container_width=True)
        else:
            # If the file doesn't exist, show an info message
            st.info("Classification report not yet available _Coming soon..._")

    display_classification_report()

    # ROC Curve and AUC Score
    st.header("ROC Curve & AUC Score")
    roc_img_path = "/workspaces/PP5-Cherry-Leaves/outputs/training_plots/roc_curve.png"
    if os.path.exists(roc_img_path):
        roc_img = Image.open(roc_img_path)
        st.image(roc_img, caption="ROC Curve", use_container_width=True)
    else:
        st.info("ROC Curve image not yet available _Coming soon..._")

    st.markdown("""
                AUC: 0.9984
                The AUC (Area Under the Curve) score indicates the model's 
                ability to distinguish between the two classes. 
                An AUC closer to 1.0 signifies excellent performance.
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

    st.success(f"Overall, the model is highly accurate (98% acccuracy) with \n"
               f"very few misclassifications, and it performs well in \n"
               f"distinguishing between healthy and powdery mildew leaves \n"
               f"on unseen data.")
