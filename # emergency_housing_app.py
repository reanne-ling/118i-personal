# emergency_housing_app.py

import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "your-api-key-here"

# Feature 1: Emergency Housing Guidance (Text Completion)
def generate_housing_guidance(situation, zip_code, urgency):
    prompt = f"""
    You are an emergency housing assistant. A user is facing the following housing crisis:
    Situation: {situation}
    ZIP Code: {zip_code}
    Urgency Level: {urgency}/5
    Based on this information, provide:
    1. Immediate housing options or shelters nearby
    2. Necessary documentation to apply
    3. Action steps they should take in the next 48 hours
    4. Community resources or support services they can contact
    """
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an empathetic AI that helps users navigate emergency housing."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

# Feature 2: Housing Space Visualization (Image Generation)
def generate_shelter_image():
    response = openai.images.generate(
        model="dall-e-2",
        prompt="A safe, clean, temporary shelter for a single parent and child. Warm lighting, basic amenities, calming colors.",
        n=1,
        size="1024x1024"
    )
    return response.data[0].url

# Feature 3: Application Preparation Assistance (Text Completion)
def generate_application_help():
    prompt = """
    Explain in simple steps how someone can prepare their documentation to apply for emergency housing.
    Include:
    1. Identification documents
    2. Proof of income or unemployment
    3. Childcare verification (if applicable)
    4. How to organize and submit these files
    Make this beginner-friendly and anxiety-free.
    """
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a calm, friendly assistant helping users prepare their documents."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("Emergency Housing Assistance App")
st.write("This AI-powered app helps you navigate urgent housing needs, visualize shelter options, and prepare your application.")

# User inputs
situation = st.text_area("Describe Your Current Housing Situation", 
                         "I just lost my job and may be evicted soon. I have a daughter and no savings.")
zip_code = st.text_input("Your ZIP Code", "95112")
urgency = st.slider("Urgency Level", 1, 5, 4)

if st.button("Get Housing Assistance"):
    with st.spinner("Finding emergency options..."):
        guidance = generate_housing_guidance(situation, zip_code, urgency)
        st.subheader("🛏️ Emergency Housing Guidance")
        st.write(guidance)

    with st.spinner("Visualizing potential shelter..."):
        image_url = generate_shelter_image()
        st.subheader("🏠 Visual Representation of a Shelter")
        st.image(image_url, caption="Example of Temporary Shelter", use_container_width=True)

    with st.spinner("Preparing your application..."):
        prep_help = generate_application_help()
        st.subheader("📄 Application Preparation Help")
        st.write(prep_help)

# Feature Community Resources and Support
# Sample community resources data (you can replace this with a database or an API)
data = {
    'Resource': ['Food Assistance', 'Mental Health Counseling', 'Job Training', 'Transitional Housing Support'],
    'Description': [
        'Provides food to individuals and families in need through local food banks and distribution centers.',
        'Offers counseling services, including support groups and therapy for those experiencing mental health challenges.',
        'Job training programs to help individuals gain skills for new careers, resume building, and interview preparation.',
        'Temporary housing assistance for individuals and families experiencing homelessness or housing instability.'
    ],
    'Contact': [
        'Local Food Bank: 555-1234',
        'Mental Health Support: 555-5678',
        'Job Training Center: 555-9101',
        'Transitional Housing: 555-1122'
    ],
    'Location': [
        '123 Main St, San José, CA',
        '456 Elm St, San José, CA',
        '789 Oak St, San José, CA',
        '101 Pine St, San José, CA'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Title of the app
st.title("Community Resources and Support")

# Introductory Text
st.write("""
This platform provides community resources and support that you can connect with, such as food assistance, mental health counseling, job training, and transitional housing support.
Select a resource below to find more information.
""")

# Dropdown menu for selecting a resource
resource_option = st.selectbox("Select a resource", df['Resource'])

# Display the selected resource details
resource_info = df[df['Resource'] == resource_option].iloc[0]
st.subheader(resource_info['Resource'])
st.write(f"**Description:** {resource_info['Description']}")
st.write(f"**Contact Information:** {resource_info['Contact']}")
st.write(f"**Location:** {resource_info['Location']}")

# Adding a button for more detailed contact options (for demo purposes)
if st.button('Request More Information'):
    st.write(f"Please contact {resource_info['Contact']} for further assistance with {resource_info['Resource']}.")



st.caption("Created by the Sapphire Team • Powered by OpenAI & Streamlit")
