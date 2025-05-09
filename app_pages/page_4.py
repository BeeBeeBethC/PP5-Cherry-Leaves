import streamlit as st


def page4_body():
    st.markdown("## Project Hypothesis")

    st.info("""
    ### Hypothesis
    I hypothesize that a **Convolutional Neural Network (CNN)**-based
            image classifier can accurately distinguish between **healthy**
            and **powdery mildew-infected** cherry leaves by learning and
            identifying **distinct visual features** (biological markers)
            associated with the powdery mildew infection.
            """)

    st.success("""
    ### Validation
    A convolutional neural network based image classifier,
        machine learning model was created and trained as prototype
        to see if the desired outcome of 97% minimum accuracy was
        generated. 
               
    Overall, the model has 98% acccuracy when when
        distinguishing between healthy and powdery mildew leaves.
        """)
