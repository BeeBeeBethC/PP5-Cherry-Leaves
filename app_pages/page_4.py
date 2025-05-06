import streamlit as st


def page4_body():
    st.markdown("## Project Hypothesis")

    st.success("""
    ### Hypothesis
    I hypothesize that a **Convolutional Neural Network (CNN)**-based image 
             classifier can accurately distinguish between **healthy** 
             and **powdery mildew-infected** cherry leaves by learning and 
             identifying **distinct visual features** (biological markers) 
             associated with the powdery mildew infection.
    """)
