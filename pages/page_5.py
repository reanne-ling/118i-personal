import streamlit as st
import pandas as pd 
import numpy as np
import openai

st.markdown("# Resources & Help")
st.sidebar.markdown("# Resources & Help")

st.header('Resource Locations', divider='color')

st.subheader('Shelters', divider= 'color')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.33, -121.88],
    columns=['lat', 'lon'])
st.map(df)
st.link_button("Click for more map examples", "https://docs.streamlit.io/develop/api-reference/charts/st.map")

st.subheader('Local Food Banks', divider= 'color')

st.subheader('Legal Aid', divider= 'color')

st.subheader('Medical Care', divider= 'color')

st.subheader('Crisis Lines', divider= 'color')

# domestic violence, suicide prevention

st.subheader('Transportation Support', divider= 'color')
