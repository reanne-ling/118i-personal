# SmartHaven – Emergency Interim Housing Support Platform  
BUS4-118i, Spring '25 – San José State University

**Deployed App**: [smarthaven.streamlit.app](https://smarthaven.streamlit.app)  
**Demo Video**: [Google Drive Demo](https://docs.google.com/file/d/1t693dj6CqUlb_MUc_4iyYmRMWd4ZfAUk/preview)

## 📌 Overview
SmartHaven is a generative AI-powered platform built to support Emergency Interim Housing (EIH) users in Santa Clara County. The application provides case managers and vulnerable populations with real-time housing resources, a sentiment analysis tool, and a chatbot assistant to improve service delivery, transparency, and efficiency.

## 👨‍💻 My Role: DevOps Engineer (Justin)
As DevOps Engineer, I was responsible for:
- Hosting and deploying the multi-page Streamlit application
- Standardizing code across the team to ensure compatibility
- Auditing and merging teammate contributions in GitHub
- Leading prompt engineering using OpenAI's API and ChatGPT
- Resolving environment inconsistencies across Python and OpenAI API versions
- Contributing 23 commits related to deployment, formatting, debugging, and integration

## 🛠️ Tools & Technologies
- Python, Streamlit, GitHub
- OpenAI API, ChatGPT
- Reddit API (sentiment analysis)
- Agile Methodology, Prompt Engineering

## 🔐 API Key Management
Screenshots confirming API key revocation and auto-recharge deactivation are included in the `/security/` directory per course guidelines.

## 📂 Repo Structure
- `/pages/` – modular Streamlit pages for different features
- `/archive/` – previous prototype version
- `/documentation/` – internal goals and planning
- `main_page.py` – unified entry point for app
- `*.py` files – individual features: assistant, housing chatbot, service recommender, budget, stakeholder input
- `requirements.txt` – dependencies for deployment
- `setup.sh` – streamlined setup for dev environment

## 🚀 How to Run
1. Clone the repo  
2. Run `pip install -r requirements.txt`  
3. Launch with `streamlit run main.py`  

---
