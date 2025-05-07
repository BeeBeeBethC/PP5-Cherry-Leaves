import streamlit as st
import os
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns


# Streamlit Page Setup
def page2_body():
    st.write("### Visualizations")
    st.info(
        "* The client is interested in having a study that visually "
        "differentiates a healthy leaf from an unhealthy leaf."
    )

    version = 'v13'

    # Radio for single-selection "accordion"
    section = st.radio("Choose a section:", [
        "Average & Variability Images",
        "Average Differences",
        "Image Montage"
    ], index=0)

    if section == "Average & Variability Images":
        avg_healthy_path = f"outputs/figures/avg_var_healthy.png"
        avg_powdery_path = f"outputs/figures/avg_var_powdery_mildew.png"

        if os.path.exists(avg_healthy_path) and os.path.exists(avg_powdery_path):
            avg_healthy = plt.imread(avg_healthy_path)
            avg_powdery_mildew = plt.imread(avg_powdery_path)

            st.warning(
                " The different images highlight subtle variations.\n"
                "On its own, this may not be visually intuitive enough \n"
                "for classification purposes."
            )

            st.image(
                avg_healthy,
                caption='Healthy Leaf - Average and Variability'
            )
            st.image(
                avg_powdery_mildew,
                caption='Diseased Leaf - Average and Variability'
            )
        else:
            st.error("One or more visualization images could not be found.")
        st.write("---")

    elif section == "Average Differences":
        avg_diff_path = f"outputs/figures/avg_diff.png"

        if os.path.exists(avg_diff_path):
            diff_between_avgs = plt.imread(avg_diff_path)

            st.warning(
                "The difference image highlights subtle variations. \n"
                "Standalone, these may not be visually intuitive enough \n"
                "for classification."
            )

            st.image(
                diff_between_avgs,
                caption='Difference between average images'
            )
        else:
            st.error("The difference image 'avg_diff.png' could not be found.")
        st.write("---")

    elif section == "Image Montage":
        st.warning("* To refresh, click on the 'Generate Example' button")

        static_dir = 'static/validation_images'
        labels = os.listdir(static_dir)

        if labels:
            label_to_display = st.selectbox(
                label="Select label",
                options=labels,
                index=0
            )
        else:
            st.error("No label folders found in 'static/validation_images'.")
            return

        if st.button("Generate Example"):
            image_folder = os.path.join(static_dir, label_to_display)
            image_files = [
                f for f in os.listdir(image_folder)
                if f.endswith(('.png', '.jpg', '.jpeg'))
            ]

            if len(image_files) < 4:
                st.warning(
                    f"* Only {len(image_files)} image(s) found in this \n"
                    f"category. \n"
                    "Consider verifying that at least 4 representative \n"
                    f" images exist."
                )

            with st.spinner("Generating image montage..."):
                image_montage(
                    dir_path=image_folder,
                    label_to_display=label_to_display,
                    nrows=2,
                    ncols=2,
                    figsize=(6, 6)
                )
        st.write("---")


# Image Montage Function
def image_montage(dir_path,
                  label_to_display,
                  nrows,
                  ncols,
                  figsize=(15, 10)
                  ):
    sns.set_style("white")

    # Get all images in the selected folder
    image_files = sorted([
        f for f in os.listdir(dir_path)
        if f.endswith(('.png', '.jpg', '.jpeg'))
    ])

    if not image_files:
        st.warning("No images found in the selected folder.")
        return

    # Set up grid
    rows = (len(image_files) + ncols - 1) // ncols
    fig, axes = plt.subplots(rows, ncols, figsize=figsize)
    axes = axes.flatten()

    for i, ax in enumerate(axes):
        if i < len(image_files):
            img_path = os.path.join(dir_path, image_files[i])
            img = Image.open(img_path)
            ax.imshow(img)
            ax.axis("off")
            ax.set_title(image_files[i], fontsize=8)
        else:
            ax.axis("off")

    st.pyplot(fig)
