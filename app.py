import streamlit as st
st.set_page_config(
    page_title="Mildew Detection in Cherry Leaves",
    layout="wide",
    page_icon=":fallen_leaf:"
)

st.title("Mildew Detection in Cherry Leaves")

from app_pages.multipage_app import MultiPage
from app_pages.page_1 import page1_body
from app_pages.page_2 import page2_body
from app_pages.page_3 import page3_body
from app_pages.page_4 import page4_body
from app_pages.page_5 import page5_body



app = MultiPage(app_name="Mildew Detection in Cherry Leaves")

app.app_page("Project Summary", page1_body)
app.app_page("Visualizations", page2_body)
app.app_page("Mildew Detection", page3_body)
app.app_page("Hypothesis and Validation", page4_body)
app.app_page("Metrics and Evaluation", page5_body)

app.run()
