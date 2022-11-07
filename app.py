from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
 

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mohit Kumar"
PAGE_ICON = ":wave:"
NAME = "Mohit Kumar"
DESCRIPTION = """
Machine Learning Engineer, Intelligent data extraction from any document.
"""
EMAIL = "mohit.iiitb@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mohit-kumar-aaa464149/",
    "GitHub": "https://github.com/themohitkumar",
    "Twitter": "https://twitter.com/2it2mohit",
}
PROJECTS = {
    "🏆 TableDataExtraction - Intelligent Table Data extraction system and data export in Excel": "",
    "🏆 FaceMatching - Face Detection and matching using Python": "https://medium.com/@themohitkumar/face-detection-and-matching-using-python-cc99e25febb",
    "🏆 OCR - Custom Ocr and digit recognition using Yolo and Tr-Ocr": "",
    "🏆 Sale Forecasting - Forecasting and model serving using FastApi": "https://github.com/themohitkumar/FastApi",
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
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1.5+ Years expereince intelligent data extraction from unstructured and structured documents
- ✔️ Strong hands on experience and knowledge in Python and neural netowrks
- ✔️ Good understanding of different ocr engines and custom training of ocr engines
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Advance oops) 
- 📊 Deep Learning Frameworks: Tensorflow ,Pytorch
- 📚 OCREngines: PaddleOcr,Tesseract,Keras-Ocr,Tr-Ocr
- 🗄️ Object Detection Frameworks: Detectron2,Yolo(Yolov5,Yolov7)
- 👁️ Computer Vision:Opencv(Descriptors) ,Opencv with gpu
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Machine Learning Engineer| AutomationEdge Technologies**")
st.write("02/2021 - Present")
st.write(
    """
- ► End to end intelligent Table Data extraction system with text extcation using three different ocr engines and export data in csv
- ► RTGS-NEFT Form Data Extraction
- ► Finetuning of ocr Engine on differnt documents
- ► Opencv Gpu compillation ,Configuring ocr engines model loading mechanism,Exploration of deep learning Algorithm and frameworks
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Web Developement Intern | Codecrux**")
st.write("06/2019 - 07/2019")
st.write(
    """
- ► Web development using Ruby On rails
- ► Development of leadership skills
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst Intern **")
st.write("05/2018 - 06/2018")
st.write(
    """
- ► Advance Training of machine learning algorithm
- ► Development of Leadership skills
- ► Hands on the machine Learning Algorithm and framework(Scikit-Learn,Tensorflow)
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
