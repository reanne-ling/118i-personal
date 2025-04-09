import streamlit as st
import pandas as pd 
import numpy as np
import openai

# for it to pop up on the sidebar
st.sidebar.markdown("# Home 🏠")

# title
st.title('SafeStay San Jóse (SS-SJ)')

# introduction
message = "Hi! Welcome to Our-program-name!" \
"We are here to aid you in your EIH needs."
message += "Please come and explore our applications for your needs!"
st.write(message)

# for table of contents
st.subheader('Table of Contents', divider= 'blue')
message = "Come explore our many resources! We aim to help streamline ur EIH process." 
col1, col2 = st.columns(2)
with col1:
   st.page_link("main_page.py", label="Home", icon="🏠", disabled=True)
   st.page_link("pages/page_1.py", label="Eligibility & Requirements", icon="📋")
   st.page_link("pages/page_2.py", label="Page 2", icon="🔒")
   st.page_link("pages/page_3.py", label="Page 3", icon="🔒")

with col2:
   st.page_link("pages/page_4.py", label="Resources & Help", icon="🆘")
   st.page_link("pages/page_5.py", label="Translator", icon="🌍")
   st.page_link("pages/page_5-6.py", label="Language & Communication Tools", icon="💬")
   st.page_link("pages/page_6.py", label="SpeechBot", icon="🔊")

# button to apply for emergency housing or directed to it
# Clear call-to-action: “Apply for Emergency Housing”

# general crisis hotline or emergency contacts displayed prominently
st.subheader('Emergency Contacts', divider= 'blue')
message = "If you are seeking emergency hotlines, here are some contacts!"
message += " If you want to see more tailored resources, check out our resources page!"
st.write(message)

st.page_link("pages/page_4.py", label="Resources & Help", icon="🆘")

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team 💎")
