from pathlib import Path
# import pyperclip
import streamlit as st
from PIL import Image
import os
import streamlit.components.v1 as components
import base64

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



def intoImg(PATH):
    file_ = open(PATH, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    current_directory = os.path.dirname(__file__)
    return data_url

def local_css(file_name):
    with open(file_name) as f:
        css_content = f.read()
        st.markdown(f'''<style>{css_content}</style>''', unsafe_allow_html=True)


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
# c1,c2,c3=st.columns((1,2,1))
# i = 0
# img_1 = os.path.join(current_directory, 'assets', 'image1_resized.png')
# img_2 = os.path.join(current_directory, 'assets', 'myscore.png')
# for project, link in PROJECTS.items():
#     if i == 0:
#         c1,c2=st.columns((1,1))
#         c1.write(f"[{project}]({link})")
#         c1.image(img_1, width=330)
#         i+=1
#     elif i == 1:
#         c2.write(f"[{project}]({link})")
#         c2.image(img_2, width=330)




# Show in webpage
local_css(r"C:\Users\hp\Desktop\analyse\digital-CV\styles\styles.css")


st.html(f"""
<body>
    <main class="portfolio">
        <div class="project">
            <span>Web App</span>
            <h4>My score - Football Analysis Application</h4>
            <a href="https://www.linkedin.com/feed/update/urn:li:activity:7209570700792115200/" target="_blank">
                <img src="data:image/gif;base64,{intoImg(r"C:\Users\hp\Desktop\analyse\digital-CV\assets\imgs\my-score.png")}" alt="Web App">
            </a>
        </div>

        <div class="project">
            <span>Data Analysis Dashboard</span>
            <h4>Frontend app : Coffee Shop</h4>
            <a href="https://github.com/ayoubmori/coffee-shop-site" target="_blank">
                <img src="data:image/gif;base64,{intoImg(r"C:\Users\hp\Desktop\analyse\digital-CV\assets\imgs\coffe-site.jpg")}" alt="Data Analysis Dashboard">
            </a>
        </div>

        <div class="project">
            <span>Dashboard Sales</span>
            <h4>Power Bi Dashboard - Coffee Shop Sales</h4>
            <a href="https://github.com/ayoubmori/coffee_shop_dashboard_sales" target="_blank">
                <img src="data:image/gif;base64,{intoImg(r"C:\Users\hp\Desktop\analyse\digital-CV\assets\imgs\coffe-shop-sales.png")}" alt="IoT Solution">
            </a>
        </div>

        <div class="project">
            <span>Forecast Api App</span>
            <h4>Weather Forecast App</h4>
            <a href="https://github.com/ayoubmori/weather-app" target="_blank">
                <img src="data:image/gif;base64,{intoImg(r"C:\Users\hp\Desktop\analyse\digital-CV\assets\imgs\forcast-app.png")}" alt="Machine Learning Model">
            </a>
        </div>

        <div class="project">
            <span>Machine Learning Model</span>
            <h4>Predict Weather model</h4>
            <a href="https://github.com/ayoubmori/predect-weather---mini-projet" target="_blank">
                <img src="data:image/gif;base64,{intoImg(r"C:\Users\hp\Desktop\analyse\digital-CV\assets\imgs\predict_weather_model.jpg")}" alt="Mobile App">
            </a>
        </div>
    </main>
</body>
</html>

        """)
