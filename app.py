from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic-bw.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ugo Piqueras"
PAGE_ICON = ":wave:"
NAME = "Ugo Piqueras"
DESCRIPTION = """
Senior Data Scientist

Assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "ugo.piqueras@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/UgoDS",
    "Linkedin": "https://www.linkedin.com/in/ugo-piqueras-3686447/",
}
PROJECTS = [
    "🏆 Recommendation engine for videos",
    "🏆 Image segmentation for road damages",
    "🏆 Content creation and animation of trainings on Pandas, git, Streamlit and SQL, for more than 50 Data scientists",
    "🏆 Internal Q&A based on LLM models",
    "🏆 Data parsing using LLM models",
    "🏆 Customer segmentation",
    "🏆 Timeseries for anomaly detection",
]
CERTIFICATIONS = {
    "Coursera, Andrew Ng, Machine Learning Specialization": "https://www.deeplearning.ai/courses/machine-learning-specialization/?utm_medium=referral&utm_source=andrew-website",
    "Coursera, Andrew Ng, Deep Learning Specialisation": "https://www.deeplearning.ai/courses/deep-learning-specialization/?utm_medium=referral&utm_source=andrew-website",
    "Coursera, Discrete Optimization": "https://www.coursera.org/learn/discrete-optimization?utm_medium=email&utm_source=other&utm_campaign=opencourse.course_complete.discrete-optimization.~opencourse.course_complete.THkzKaBPEeWm9xJA1YXcWQ.",
    "Databricks Certified Developer - Apache Spark 2.x for Python": "https://www.databricks.com/learn/certification/apache-spark-developer-associate",
    "Snowflake Pro Certification": "https://www.credly.com/badges/ad15c1fd-8d49-4083-8414-1d22eb7b8eae/linked_in_profile",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 10 Years experience Data Scientist extracting actionable insights from data
- ✔️ Strong hands-on experience in Python, git, SQL, Azure and Excel
- ✔️ Deep understanding of ML models and their respective applications
- ✔️ Team-player and sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Streamlit, Langchain), SQL, git, chatGPT
- 📊 Data Visualization: Plotly, MS Excel
- 📚 Modeling: Segmentation, Recommendation, Timeseries, Computer Vision, NLP
- 🗄️ Databases: Snowflake, Deltalake
- ⚙ IDE: VScode, iTerm
- 💯 Everything else: Notion
"""
)


# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Scientist | Pernod Ricard**")
st.write("12/2020 - 08/2023")
st.write(
    """
- ► Founded and oversaw ephemeral data innovation teams, involving 40 people and delivering direct business benefits.
- ► Successfully implemented an internal chatbot using LLM to answer all employees' questions.
- ► Enhanced a recommendation engine for an internal Data Portal, resulting in a 35% increase in Click Rate.
- ► Provided support for over 50 Data Analysts and Data Scientists, including conducting training on data best practices.
"""
)

# --- JOB 2
st.write("\n")
st.write("🚧", "**Senior Data Scientist | Openvalue**")
st.write("04/2016 - 11/2020")
st.write(
    """
- ► Consultant for different clients: Banking sector, Retail, Television, Civil Engineering
- ► Constructed a customer segmentation model for a major Television channel.
- ► Launched a recommendation engine into production for video replay, utilizing users' past activity as the basis.
- ► Executed a computer vision program to detect and geolocate road damages.
- ► Segmented outlets based on social media content analysis.
"""
)

# --- JOB 3
st.write("\n")
st.write("🚧", "**Data Analyst | Energies Demain**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Creation of a bottom-up water demand tool in France, used by French Ministry of Environment
- ► Elaboration of a national prospective scenario on electric demand
- ► Collaborated with governmental agencies and work presentation at international forums
"""
)


# --- Projects & Accomplishments ---
st.write("\n")
st.subheader("ML skills")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")


# --- Certifications ---
st.write("\n")
st.subheader("Certifications")
st.write("---")
for certification, url_certication in CERTIFICATIONS.items():
    st.write(f"[{certification}]({url_certication})")
