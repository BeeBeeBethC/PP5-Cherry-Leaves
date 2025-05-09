import streamlit as st


def page1_body():
    st.write("""
    A fictional business was created for the purpose of this project.
    """)

    st.write("""
    Farmy & Foods produces and harvests various types of food.
    Recently, they have been facing a challenge: their cherry
    plantations are affected by powdery mildew.

    Powdery mildew is a fungal disease that affects plants and crops.
    The cherry plantation at Farmy & Foods is one of their most prized
    products, and they are concerned about its quality due to this disease.
    """)

    st.write("""
    Currently, the process of detecting powdery mildew is manual and
    time-consuming, with each tree taking about 30 minutes to inspect.
    This process is not scalable,
    especially given the large number of trees in the plantation.

    To solve this problem, the IT team suggested implementing a Machine
    Learning system capable of automatically detecting powdery mildew
    in cherry leaves by analyzing images of the leaves to classify them as
    either healthy or infected.
    """)

    st.success("""
    ### Business Requirements

    1. The client wants to conduct a study to visually differentiate healthy
    cherry leaves from those affected by powdery mildew.

    2. The client seeks a solution that can predict whether a cherry leaf is
    healthy or infected with powdery mildew.
    """)

    st.info("""
    ### More Information

    Further details can be found in this
    [README](https://github.com/BeeBeeBethC/PP5-Cherry-Leaves)
    """)