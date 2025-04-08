import streamlit as st
import pandas as pd 
import numpy as np
import openai

st.markdown("# Home Page")
st.sidebar.markdown("# Home Page")

# title
st.title('#Name of the program')

# introduction
message = "Hi! Welcome to Our-program-name!" \
"We are here to aid you in your EIH needs."
message += "Please come and explore our applications for your needs!"
st.write(message)

# for table of contents
st.subheader('Table of Contents', divider= 'color')
col1, col2, col3 = st.columns(3)
with col1:
   st.page_link("main_page.py", label="Home", icon="🏠", disabled=True)
   st.page_link("pages/page_1.py", label="Eligibility & Requirements", icon="📋")

with col2:
   st.page_link("pages/page_2.py", label="Page 2", icon="2")
   st.page_link("pages/page_3.py", label="Page 3", icon="3")

with col3:
   st.page_link("pages/page_4.py", label="Resources & Help", icon="🆘")
   st.page_link("pages/page_5.py", label="Translator (but this is from prof's)", icon="🌍")
   st.page_link("pages/page_6.py", label="SpeechBot", icon="🔊")

# button to apply for emergency housing or directed to it
# Clear call-to-action: “Apply for Emergency Housing”

# general crisis hotline or emergency contacts displayed prominently