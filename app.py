from pathlib import Path
# import pyperclip
import streamlit as st
from PIL import Image
import os
current_directory = os.path.dirname(__file__)




# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ayoub Taouabi"
PAGE_ICON = ":wave:"
NAME = "Ayoub Taouabi"
DESCRIPTION = """
Junior Data Scientist | Dedicated to harnessing data for impactful insights and innovation 📊
"""
EMAIL = "ayoubtaouabi6@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ayoub-taouabi/",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://www.linkedin.com/in/ayoub-taouabi/",
    "🏆 Football Performance Analysis – analyze team and player performance ": "https://my-score.onrender.com/",
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

## description 
# st.write("Data analyst student enthusiastic about extracting insights from data to inform decisions.")
## phone number
# a='+212621720681'
# if st.button('Phone number'):
#     pyperclip.copy(a)
#     st.success('number copied successfully!')

    
    
# EDUCATION
st.write('\n')
st.subheader("EDUCATION")
col1,col2=st.columns(2)
col1.write("🎓 ECOLE SUPERIEURE DE TECHNOLOGIE")
col2.caption("DUT en Informatique Décisionnelle et Statistiques")
col1.write("🎓 LYCEE ABOU ELKACEM ZAYANI")
col2.caption("Baccalauréat en sciences physique 2020-2021")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qulifications")
st.write(
    """
- ✔️ Solid understanding of statistical principles for data analysis.
- ✔️ Skilled in data visualization and machine learning basics.
- ✔️ Quick learner and adaptable to new tools and technologies.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: PowerBi, Excel
- 📚 Modeling: Logistic regression, linear regression, clustring
- 🗄️ Databases: MySQL, Oracle 
"""
)
#---- langues----
st.write('\n')
st.subheader("Langues")
st.write(
    """
- ⭐ English B2
- ⭐ Francais B1
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience & Work History")
st.write("---")

# --- JOB 1
st.caption("Internship")
st.write("🚧", "**Software Developer | Lumnex** ")
st.write("04/2024 - present - 4 mo")
st.write(
    """
- ► Developed a REST API for Gateway Control
- ► Advanced Control Systems
- ► Generated a simulation on Raspberry Pi
"""
)

st.caption("Internship")
st.write("🚧", "**Data Analyst | Office Chérifien des Phosphates (OCP)** ")
st.write("07/2023 - 1 mo")
st.write(
    """
- ► Organisasion et analyse des données
- ► Détection des motifs et des anomalies dans les données 
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
c1,c2,c3=st.columns((1,2,1))
i = 0
img_1 = os.path.join(current_directory, 'assets', 'image1_resized.png')
img_2 = os.path.join(current_directory, 'assets', 'myscore.png')
for project, link in PROJECTS.items():
    if i == 0:
        c1,c2=st.columns((1,1))
        c1.write(f"[{project}]({link})")
        c1.image(img_1, width=330)
        i+=1
    elif i == 1:
        c2.write(f"[{project}]({link})")
        c2.image(img_2, width=330)
