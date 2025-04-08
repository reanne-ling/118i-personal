import streamlit as st
import pandas as pd 
import numpy as np
import openai

st.markdown("# Eligibility & Requirement 📋")
st.sidebar.markdown("# Eligibility & Requirements 📋")

# page title
st.title('Eligibility & Requirement 📋')
st.subheader('Learn about who qualifies for emergency interim housing,' \
' what documents you will need, and how to prepare for the application process.')

# introduction
st.write(
'Welcome to the Emergency Interim Housing (EIH) program information page. Here, you ' \
'will find details on eligibility criteria, the application process, and resources ' \
'available for individuals and families experiencing homelessness in San José and Santa Clara County.')

# for the qualifications
st.subheader('Qualifications for EIH', divider= 'color')
st.markdown(
'''To qualify for the EIH program, applicants must meet the following requirements:

- **Residency**: Must be a resident of Santa Clara County.
- **Homeless Status**: Must be currently experiencing homelessness.
- **Assessment**: Completion of the Vulnerability Index-Service Prioritization Decision Assistance Tool (VI-SPDAT) to determine housing and service needs. [Learn more about Coordinated Entry and VI-SPDAT](https://osh.sccgov.org/continuum-care/coordinated-entry)
- **Special Populations**: Certain programs may prioritize specific groups, such as:
  - Transition-aged youth (16 to 24 years old)
  - Domestic violence survivors
  - Individuals in recovery from substance use disorders
  - Persons exiting the criminal justice system
  - [More information on targeted populations](https://osh.sccgov.org/solutions-homelessness/interim-solutions/transitional-housing)
''')

# for the req documents
st.subheader('Required Documents', divider= 'color')

# for the app process
st.subheader('Application Process', divider= 'color')
st.markdown(
'''1. **Initial Contact**:
   - **Here4You Hotline**: Call **(408) 385-2400** between 9:00 AM and 7:00 PM, seven days a week, to connect with a representative who can assist with shelter placements. [More details](https://osh.sccgov.org/solutions-homelessness/interim-solutions/emergency-shelters)
   - **Coordinated Entry Assessment**: Schedule an appointment to complete the VI-SPDAT assessment.
2. **Documentation**: Prepare necessary documents, which may include:
   - Identification (e.g., driver's license, state ID)
   - Proof of Santa Clara County residency
   - Any relevant medical or legal documents
3. **Program Referral**: Based on assessment results, you may be referred to an appropriate housing program that fits your needs.

*Note*: Availability is limited, and placement is not guaranteed. It's essential to maintain communication with your case manager and explore multiple housing options.
''')

# for the faq
st.subheader('FAQs for common situations', divider= 'color')


# for the references they can press/websites
st.subheader('Additional References', divider= 'color')
st.markdown(
'''- **Homeless Resource Guide**: A comprehensive guide to services available for individuals experiencing homelessness in San José.
  - [English Guide](https://www.sanjoseca.gov/your-government/departments-offices/housing/homelessness-response/homeless-families-individuals)
  - [Guía en español](https://www.sanjoseca.gov/your-government/departments-offices/housing/homelessness-response/homeless-families-individuals)
  - [Tài liệu hướng dẫn bằng tiếng Việt](https://www.sanjoseca.gov/your-government/departments-offices/housing/homelessness-response/homeless-families-individuals)
- **Office of Supportive Housing**: Provides information on various housing programs and services in Santa Clara County. [Visit their website](https://osh.sccgov.org/)
- **Emergency Shelters**: For immediate shelter needs, contact the Here4You Hotline at **(408) 385-2400**. [More information](https://osh.sccgov.org/solutions-homelessness/interim-solutions/emergency-shelters)
''')

# for contact info for the shelter hotline
st.subheader('Contact Information')
st.markdown(
'''For further assistance or inquiries:

- **Here4You Shelter Hotline**: **(408) 385-2400** (Available daily from 9:00 AM to 7:00 PM)
- **Email**: [homewardbound@sanjoseca.gov](mailto:homewardbound@sanjoseca.gov)
- **Address**: 200 E. Santa Clara St., San José, CA 95113
- **TTY**: **(800) 735-2922**
''')