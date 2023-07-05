import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

st.markdown(hide_github_icon, unsafe_allow_html=True)
page = st.sidebar.selectbox("Predict/Contributors", ("Predict", "Contributors"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
