import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def page3_body():
    st.info(
        "* The client is interested in conducting a study\n"
        "to visually differentiate a cherry leaf that is healthy\n"
        "from one that contains powdery mildew."
    )

    st.write("* Here you can test your own images on the model.")
    st.write("---")

    images_buffer = st.file_uploader(
        label='Upload leaf samples.',
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )

    if images_buffer is not None:
        df_report = pd.DataFrame([])

        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Leaf: **{image.name}**")

            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=(
                    f"Image Size: {img_array.shape[1]}px width x "
                    f"{img_array.shape[0]}px height"
                )
            )

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version
            )
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report._append(
                {"Name": image.name, "Result": pred_class},
                ignore_index=True
            )

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)

            st.markdown(
                download_dataframe_as_csv(df_report),
                unsafe_allow_html=True
            )
            