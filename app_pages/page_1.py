import streamlit as st


def page1_body():
    st.success("Project Summary" \
    "Data source:'https://www.kaggle.com/codeinstitute/cherry-leaves'"
    "Readme Link: 'https://github.com/BeeBeeBethC/PP5-Cherry-Leaves'"
    )
    st.write("For the purpose of this project, A fictional business was " \
    "created. Farmy & Foods, a company in the agricultural " \
    "sector, produces and harvests different types of food. " \
    "Recently, they are facing a challenge where their cherry plantations " \
    "have been presenting with powdery mildew." \
    )
    st.write(
    "Powdery Mildew is a fungal disease which affects plants and crops. " \
    "The cherry plantation belonging to Farmy and Foods, is one of their " \
    "finest products in their portfolio." \
    "Farmy and Foods are concerned about supplying the market with a " \
    "product of compromised quality. "
    )
    st.write(
    "Currently, the process is to manually verify if a given cherry tree " \
    "contains powdery mildew. " \
    "As a result, this manual process is not scalable due to it being a " \
    "lengthy process. " \
    "To save time in this process, the IT team suggested an Machine Learning " \
    "system that is capable of detecting Powdery Mildews in Cherry Leaves. " \
    "Using a tree leaf image, to identify if the leaf is healthy or has " \
    "powdery mildew present. "
    )
    
    st.success("Business Requirements")
    st.write(
    "1. The client is interested in conducting a study " \
    "to visually differentiate a cherry leaf that is healthy from one that " \
    "contains powdery mildew." \
    )
    st.write(
    "2. The client is interested in predicting if a cherry leaf is healthy " \
    "or contains powdery mildew.")