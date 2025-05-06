import streamlit as st


def page1_body():

    st.write(
        f"(For the purpose of this project, a fictional business was created.) \n\n"
        f"Farmy & Foods, a fictional company in the agricultural sector, produces and harvests various types of food. "
        f"Recently, they have been facing a challenge: their cherry plantations are affected by powdery mildew."
    )
    st.write(
        f"Powdery mildew is a fungal disease that affects plants and crops. "
        f"The cherry plantation at Farmy & Foods is one of their most prized products, and they are concerned about its "
        f"quality due to this disease."
    )
    st.write(
        f"Currently, the process of detecting powdery mildew is manual and time-consuming, with each tree taking about 30 minutes to inspect. "
        f"This process is not scalable, especially given the large number of trees in the plantation. \n\n"
        f"To solve this problem, the IT team suggested implementing a Machine Learning system capable of automatically detecting "
        f"powdery mildew in cherry leaves by analyzing images of the leaves to classify them as either healthy or infected."
    )

    st.success("### Business Requirements\n\n"
               f"1. The client wants to conduct a study to visually differentiate healthy cherry leaves from those affected by powdery mildew.\n\n"
               f"2. The client seeks a solution that can predict whether a cherry leaf is healthy or infected with powdery mildew."
               )

    st.info("### More Information\n\n"
            f"Further details can be found in this README file: [link](https://github.com/BeeBeeBethC/PP5-Cherry-Leaves)\n"
            )
