import streamlit as st
import pandas as pd 
import numpy as np
import openai

# for it to pop up on the sidebar
st.sidebar.markdown("# Resources & Help 🆘 ")

# page title
st.title('Resources & Help 🆘 ')
st.write('For individuals seeking emergency interim housing and support services in San Jose, CA!')

# title for san jose resources
st.subheader('Resource Locations', divider='blue')
message = 'These resources are mainly listed for the San Jose/Santa Clara County area.'
st.write(message)

# ----------------------------------------------------------------
# for shelter locations
st.subheader('Emergency Shelters', divider= 'blue')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.33, -121.88],
    columns=['lat', 'lon'])
st.map(df)
st.link_button("Click for more map examples", "https://docs.streamlit.io/develop/api-reference/charts/st.map")
   
   # for ___ housing
st.markdown('''
- **[HomeFirst Services](https://www.homefirstscc.org/)**  
  Services: Emergency shelters, transitional housing, outreach''')
   # for ___ housing
st.markdown('''
- **[Bill Wilson Center](https://www.billwilsoncenter.org/)**  
  Services: Youth & young adults, emergency shelter, family support''')
   # for ___ housing
st.markdown('''
- **[CityTeam San Jose](https://www.cityteam.org/san-jose)**  
  Services: Food, shelter, addiction recovery, and transitional housing''')
# ----------------------------------------------------------------

# for local food banks and basic needs
st.subheader('Local Food Banks & Basic Needs', divider= 'blue')
st.markdown('''
- **[Second Harvest of Silicon Valley](https://www.shfb.org/)**  
  Services: Free groceries, food pantries  
- **[Sacred Heart Community Service](https://sacredheartcs.org/)**  
  Services: Clothing, food, financial assistance, case management
''')

# ----------------------------------------------------------------
#for legal aid services
st.subheader('Legal Aid', divider= 'blue')
# ----------------------------------------------------------------

# for medical care resources
st.subheader('Medical Care', divider= 'blue')
st.markdown('''
- **[Gardner Health Services](https://gardnerhealthservices.org/)**  
  Services: Primary care, behavioral health, substance use treatment  
- **[Santa Clara Valley Medical Center](https://www.scvmc.org/)**  
  Services: Emergency medical, clinics, urgent care
''')

# for crisis resources
st.subheader('Crisis Lines', divider= 'blue')
st.subheader('Domestic Violence & Safety')
st.markdown('''
- **[Next Door Solutions](https://nextdoorsolutions.org/)**  
  24/7 Hotline: (408) 279-2962  
- **[YWCA Silicon Valley](https://www.ywca-sv.org/)**  
  Services: Safe housing, advocacy, counseling
''')
st.subheader('Mental Health Support')
st.markdown('''
- **[988 Suicide & Crisis Lifeline]**
  Website:   (https://www.988lifeline.org/)  
  Call/Text: 988 (24/7, Free, Confidential)
- **[NAMI (National Alliance on Mental Illness)]**
  Website:   (https://www.nami.org/)  
  Helpline:  1-800-950-NAMI (6564)
''')
st.subheader('Veterans Crisis Line')
st.markdown('''
- **[Veterans Crisis Line]**
  Website: (https://www.veteranscrisisline.net/)  
  Call:    Dial 988 then press 1  
  Text:    838255
''')
st.subheader('Human Trafficking Hotline')
st.markdown('''
- **[Human Trafficking Hotline]**
  Website: (https://humantraffickinghotline.org/)  
  Call:    1-888-373-7888  
  Text:    “HELP” to 233733
''')

# ----------------------------------------------------------------
# for transportation support
st.subheader('Transportation Support', divider= 'blue')
# ----------------------------------------------------------------

# footer
st.markdown("---")
st.caption("Provided by the Sapphire Team")