import streamlit as st
import pandas as pd 
import numpy as np
import openai

st.markdown("# Resources & Help 🆘 ")
st.sidebar.markdown("# Resources & Help 🆘 ")

# page title
st.title('Resources & Help 🆘 ')
st.subheader('For individuals seeking emergency interim housing and support services in San Jose, CA!')

# title for san jose resources
st.header('Resource Locations', divider='color')
message = 'These reosurces are mainly listed for the San Jose/Santa Clara County area.'

# for shelter locations
st.subheader('Emergency Shelters', divider= 'color')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.33, -121.88],
    columns=['lat', 'lon'])
st.map(df)
st.link_button("Click for more map examples", "https://docs.streamlit.io/develop/api-reference/charts/st.map")

st.markdown("""
- **[HomeFirst Services](https://www.homefirstscc.org/)**  
  Emergency shelters, transitional housing, outreach  
- **[Bill Wilson Center](https://www.billwilsoncenter.org/)**  
  Youth & young adults, emergency shelter, family support  
- **[CityTeam San Jose](https://www.cityteam.org/san-jose)**  
  Food, shelter, addiction recovery, and transitional housing
""")

# for local food banks
st.subheader('Local Food Banks', divider= 'color')
st.markdown("""
- **[Second Harvest of Silicon Valley](https://www.shfb.org/)**  
  Free groceries, food pantries  
- **[Sacred Heart Community Service](https://sacredheartcs.org/)**  
  Clothing, food, financial assistance, case management
""")

#for legal aid services
st.subheader('Legal Aid', divider= 'color')


# for medical care resources
st.subheader('Medical Care', divider= 'color')
st.markdown("""
- **[Gardner Health Services](https://gardnerhealthservices.org/)**  
  Primary care, behavioral health, substance use treatment  
- **[Santa Clara Valley Medical Center](https://www.scvmc.org/)**  
  Emergency medical, clinics, urgent care
""")

# for crisis resources
st.subheader('Crisis Lines', divider= 'color')
st.subheader('Domestic Violence & Safety')
st.markdown("""
- **[Next Door Solutions](https://nextdoorsolutions.org/)**  
  24/7 Hotline: (408) 279-2962  
- **[YWCA Silicon Valley](https://www.ywca-sv.org/)**  
  Safe housing, advocacy, counseling
""")
st.subheader('Veterans Crisis Line')
st.markdown("""
- **[Veterans Crisis Line](https://www.veteranscrisisline.net/)**  
  Dial 988 then press 1  
  Text: 838255
""")
st.subheader('Human Trafficking Hotline')
st.markdown("""
- **[Human Trafficking Hotline](https://humantraffickinghotline.org/)**  
  Call: 1-888-373-7888  
  Text: “HELP” to 233733
""")

# for transportation support
st.subheader('Transportation Support', divider= 'color')

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team")