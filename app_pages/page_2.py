import streamlit as st
import os
import random
import shutil
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

# Function to move a random subset of images to a smaller folder
def move_images_to_subset(validation_folder, output_folder, num_images_to_select):
    os.makedirs(output_folder, exist_ok=True)
    image_files = [f for f in os.listdir(validation_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    random.shuffle(image_files)
    selected_images = image_files[:num_images_to_select]
    
    for img in selected_images:
        img_path = os.path.join(validation_folder, img)
        output_img_path = os.path.join(output_folder, img)
        shutil.move(img_path, output_img_path)
    
    return selected_images  # Return the selected images for confirmation

# Streamlit Page Setup
def page2_body():
    st.write("### Visualizations")
    st.info(
        f"* The client is interested in having a study that visually "
        f"differentiates a parasitised from an uninfected cell.")
    
    version = 'v13'
    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        st.image(avg_powdery_mildew, caption='Diseased Leaf - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average parasitised and average uninfected cells"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        my_data_dir = 'inputs/leaves_dataset/cherry-leaves/processed_images'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        
        # New option to move images before creating montage
        if st.button("Create Montage with Subset"):
            # Move a subset of validation images to a new smaller folder
            validation_folder = my_data_dir + '/validation'
            output_folder = "static/validation_small"
            selected_images = move_images_to_subset(validation_folder, output_folder, num_images_to_select=10)
            st.write(f"Moved {len(selected_images)} images to {output_folder}.")
            
            # Create montage with images from the subset folder
            image_montage(dir_path=output_folder, label_to_display=label_to_display, nrows=8, ncols=3, figsize=(10,25))
        st.write("---")

# Image Montage Function
def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)
    selected_folder = os.path.join(dir_path, label_to_display)
    
    # Get all images in the selected folder
    image_files = [f for f in os.listdir(selected_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Set up grid
    rows = (len(image_files) + ncols - 1) // ncols
    fig, axes = plt.subplots(rows, ncols, figsize=figsize)
    axes = axes.flatten()

    for i, ax in enumerate(axes):
        if i < len(image_files):
            img_path = os.path.join(selected_folder, image_files[i])
            img = Image.open(img_path)
            ax.imshow(img)
            ax.axis("off")
            ax.set_title(image_files[i], fontsize=8)
        else:
            ax.axis("off")

    st.pyplot(fig)
