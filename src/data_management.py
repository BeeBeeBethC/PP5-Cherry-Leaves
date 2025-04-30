
import os
import shutil
import random
import pandas as pd
import streamlit as st
from tensorflow import keras
from keras.preprocessing.image import load_img, img_to_array
import numpy as np

class DataManager:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.image_shape = (100, 100)  # Standard size for leaf images
        
    def process_image(self, image_path):
        """Load and preprocess a single image"""
        img = load_img(image_path, target_size=self.image_shape)
        img_array = img_to_array(img)
        img_array = img_array / 255.0  # Normalize
        return img_array
        
    def create_dataframe(self, subset_dir):
        """Create DataFrame for a dataset subset (train/validation/test)"""
        data = {'file': [], 'label': []}
        for label in os.listdir(subset_dir):
            label_dir = os.path.join(subset_dir, label)
            if os.path.isdir(label_dir):
                for file in os.listdir(label_dir):
                    file_path = os.path.join(label_dir, file)
                    data['file'].append(file_path)
                    data['label'].append(label)
        return pd.DataFrame(data)
        
    def split_dataset(self, train_ratio=0.7, validation_ratio=0.15):
        """Split dataset into train, validation, and test sets"""
        test_ratio = 1 - train_ratio - validation_ratio
        
        for label in ['healthy', 'powdery_mildew']:
            files = os.listdir(os.path.join(self.data_dir, label))
            random.shuffle(files)
            
            n_files = len(files)
            n_train = int(n_files * train_ratio)
            n_validation = int(n_files * validation_ratio)
            
            train_files = files[:n_train]
            validation_files = files[n_train:n_train + n_validation]
            test_files = files[n_train + n_validation:]
            
            # Move files to respective directories
            for subset, file_list in [('train', train_files), 
                                    ('validation', validation_files),
                                    ('test', test_files)]:
                subset_dir = os.path.join(self.data_dir, subset, label)
                os.makedirs(subset_dir, exist_ok=True)
                for file in file_list:
                    src = os.path.join(self.data_dir, label, file)
                    dst = os.path.join(subset_dir, file)
                    shutil.move(src, dst)


def download_dataframe_as_csv(df, filename="data.csv"):
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download data as CSV",
        data=csv,
        file_name=filename,
        mime="text/csv",
    )