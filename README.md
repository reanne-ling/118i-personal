# SmartHaven – Emergency Interim Housing Support App

**Deployed App**:  
- [smarthaven.streamlit.app](https://smarthaven.streamlit.app) – Primary development version hosted and maintained by me  
- [118i-sapphire-team.streamlit.app](https://118i-sapphire-team.streamlit.app) – Final version hosted by José after deployment hurdles

**Course**: BUS4-118i: AI for Social Good – San José State University  
**Term**: Spring 2025  
**Role**: DevOps Engineer  
**Team**: 118i-Sapphire-Team

---

## 🔍 Project Overview

SmartHaven is a generative AI-powered platform designed to support Emergency Interim Housing (EIH) navigation in Santa Clara County. The application assists both the public and case managers by providing real-time access to local housing resources, sentiment analysis through Reddit data, and a conversational assistant to answer housing-related questions. Our goal was to reduce friction and promote digital equity for vulnerable communities.

---

## 👨‍💻 Justin's Role and Contributions: DevOps Engineer

- Brainstorming early concepts including mapping unused building sites and using the Nextdoor API for sentiment analysis (pivoted to Reddit due to API restrictions)
- Managing prompt engineering and OpenAI API integration
- Auditing and standardizing all team contributions to ensure multi-page Streamlit app functionality
- Hosting and maintaining the primary deployment via Streamlit Cloud
- Resolving environment inconsistencies (Python versioning, API compatibility)
- Finalizing structure and deliverables for presentation and stakeholder review
- Pushed 23 commits related to deployment, integration, formatting, and debugging

---

## ⚙️ Technologies & Tools

- **Languages**: Python, HTML/CSS (Streamlit elements)
- **Libraries & APIs**: Streamlit, OpenAI API, Reddit API, requests, folium
- **Tools**: Git, GitHub, Streamlit Cloud, VS Code
- **Methods**: Prompt Engineering, Agile Methodology, DevOps

---

## 🔐 API Key Management

All API keys were stored locally via environment variables and were never pushed to GitHub.  
For billing and security protection:
- OpenAI API keys were revoked
- Auto-recharge billing was disabled

📎 Screenshots confirming both actions are available in the `screenshots/` folder.

---

## 📂 Repo Structure

- `/pages/` – Streamlit pages for individual app features
- `/archive/` – Previous version prototype
- `/documentation/` – Planning and stakeholder content
- `main_page.py` – Unified entry point for deployment
- `requirements.txt` – Environment dependencies
- `setup.sh` – Script for local setup
- `/screenshots/` – API key revocation and billing protection proof

---

## ✅ How to Run Locally

1. Clone the repository  
2. Install dependencies:  
   `pip install -r requirements.txt`  
3. Run the app:  
   `streamlit run main_page.py`
