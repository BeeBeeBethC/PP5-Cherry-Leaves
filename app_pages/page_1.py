import streamlit as st


def page1_body():
    
    st.write(
        f"(For the purpose of this project, A fictional business \n"
        f"was created.) \n\n"
        f"Farmy & Foods, a fictional company in the agricultural \n"
        f"sector, produces and harvests different types of food. \n"
        f"Recently, they are facing a challenge where their cherry \n"
        f"plantations have been presenting with powdery mildew."
    )
    st.write(
        f"Powdery Mildew is a fungal disease which affects plants and crops. \n"
        f"The cherry plantation belonging to Farmy and Foods, is one of \n"
        f"their finest products in their portfolio. \n"
        f"Farmy and Foods are concerned about supplying the market with a \n"
        f"product of compromised quality."
    )
    st.write(
        f"Currently, the process is to manually verify if a given cherry \n"
        f"tree contains powdery mildew. \n"
        f"As a result, this manual process is not scalable due to it being \n"
        f"time consuming (30 minutes per tree). \n\n"
        f"To save time in this process, The IT team suggested an Machine \n"
        f"Learning system that is capable of detecting Powdery Mildews in \n"
        f"Cherry Leaves. \n"
        f"Using a tree leaf image, to identify if the leaf is healthy or \n"
        f"has powdery mildew present."
    )
    
    st.success("### Business Requirements\n\n"
        f"1. The client is interested in conducting a study \n"
        f"to visually differentiate a cherry leaf that is healthy from one \n"
        f"that contains powdery mildew.\n\n"
        f"2. The client is interested in predicting if a cherry leaf is \n"
        f"healthy or contains powdery mildew."
    )
    
    st.info("### Data source and more information\n\n"
        f"* Data source: https://www.kaggle.com/codeinstitute/cherry-leaves \n"
        f"* Readme Link: https://github.com/BeeBeeBethC/PP5-Cherry-Leaves \n"
    )