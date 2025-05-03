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
resume_file = current_dir / "assets" / "AYOUB_TAOUABI_CV.pdf"
profile_pic = current_dir / "assets" / "picofme.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ayoub Taouabi"
PAGE_ICON = ":wave:"
NAME = "Ayoub Taouabi"
DESCRIPTION = """
Junior Data Analyst | Dedicated to harnessing data for impactful insights and innovation 📊
"""
EMAIL = "ayoubtaouabi6@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ayoub-taouabi/",
    "Github" : "https://github.com/ayoubmori" ,
    "Portfolio" : "https://ayoubmori.github.io/portfolio_v1/",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://www.linkedin.com/in/ayoub-taouabi/",
    "🏆 Football Performance Analysis – analyze team and player performance ": "https://my-score.onrender.com/",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

st.markdown("""
    <style>
    div[data-testid="stMainBlockContainer"] {
        padding-top: 2rem !important; } 
        </style> """,
        unsafe_allow_html=True)

current_dir = Path(__file__).parent
styles_file = current_dir / "styles" / "styles.css"
assets_dir = current_dir / "assets" / "imgs"

# --- Helper Function ---
def into_img(path):
    """Convert an image to a base64-encoded string."""
    with open(path, "rb") as file_:
        contents = file_.read()
    return base64.b64encode(contents).decode("utf-8")

def local_css(file_path):
    """Load a local CSS file."""
    with open(file_path) as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
_,col1,col2,__ = st.columns([6,4,5,6], gap="small")
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
    
    # --- SOCIAL LINKS ---
    
    # Email
    mailto_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={EMAIL}"
    st.markdown(f"[📫 {EMAIL}]({mailto_link})", unsafe_allow_html=True)

    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA)+1)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


## description 
# st.write("Data analyst student enthusiastic about extracting insights from data to inform decisions.")
## phone number
# a='+212621720681'
# if st.button('Phone number'):
#     pyperclip.copy(a)
#     st.success('number copied successfully!')

sc1, sc2, sc3 = st.columns(3)
with sc1 :
    # EDUCATION
    st.write('\n')
    st.subheader("EDUCATION")
    st.write("---")
    
    st.write("🎓 Bachelor of Excellence in DataAnalytics and Artificial Intelligence")
    col1,col2=st.columns([0.3,10])
    col2.caption("University Ibn Zohr - Agadir | 2024 – Present")

    st.write("🎓 University Diploma of Technology inDecision Support and Statistics")
    col1,col2=st.columns([0.3,10])
    col2.caption("École Supérieure de Technologie FBS | 2022 - 2024")

    
    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Experience & Work History")
    st.write("---")

    # --- JOB 1
    st.caption("Internship")
    st.write("🚧", "**Software Developer | Lumnex** ")
    st.write("04/2024 - 07/2024 - 4 months")
    st.write(
        """
    - ► Developed a REST API for Gateway Control
    - ► Advanced Control Systems
    - ► Generated a simulation on Raspberry Pi
    """
    )

    st.caption("Internship")
    st.write("🚧", "**Data Analyst | Office Chérifien des Phosphates (OCP)** ")
    st.write("07/2023 - 1 month")
    st.write(
        """
    - ► Organisasion et analyse des données
    - ► Détection des motifs et des anomalies dans les données 
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives
    """
    )
    
    

with sc2 :
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write("---")
    st.write(
        """
    - 👩‍💻 **Programming** : Python (Scikit-learn, Pandas), SQL
    - 📊 **Data Visulization** : PowerBi, Excel
    - 📚 **Modeling** : Logistic regression, linear regression, clustring
    - 🗄️ **Databases** : MySQL, Oracle 
    """
    )
    
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Qulifications")
    st.write("---")
    st.write(
        """
    - ✔️ Solid understanding of statistical principles for data analysis.
    - ✔️ Skilled in data visualization and machine learning basics.
    - ✔️ Quick learner and adaptable to new tools and technologies.
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )
    
    #---- langues----
    st.write('\n')
    st.subheader("Langues")
    st.write("---")
    st.write(
        """
    - ⭐ Arabic C1
    - ⭐ English B2
    - ⭐ Francais B1
    """
    )

with sc3 :
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
    local_css("styles/styles.css")


    st.html(f"""
    <body>
        <main class="portfolio">
            <div class="project">
                <span>Web App</span>
                <h4>My score - Football Analysis Application</h4>
                <a href="https://www.linkedin.com/feed/update/urn:li:activity:7209570700792115200/" target="_blank">
                    <img src="data:image/gif;base64,{into_img(assets_dir / 'my-score.png')}" alt="Web App">
                </a>
            </div>

            <div class="project">
                <span>TMDB Api Project</span>
                <h4>Movie & TV Show Explorer with TMDB"</h4>
                <a href="https://github.com/ayoubmori/Movies-App" target="_blank">
                    <img src="data:image/gif;base64,{into_img(assets_dir / 'movie_app_demo.png')}" alt="Mobile App">
                </a>
            </div>

            <div class="project">
                <span>Fornt-End App</span>
                <h4>Frontend app- Coffee Shop</h4>
                <a href="https://github.com/ayoubmori/coffee-shop-site" target="_blank">
                    <img src="data:image/gif;base64,{into_img(assets_dir / 'coffe-site.jpg')}" alt="Data Analysis Dashboard">
                </a>
            </div>

            <div class="project">
                <span>Data Analysis Dashboard</span>
                <h4>Power Bi Dashboard - Coffee Shop Sales</h4>
                <a href="https://github.com/ayoubmori/coffee_shop_dashboard_sales" target="_blank">
                    <img src="data:image/gif;base64,{into_img(assets_dir / 'coffe-shop-sales.png')}" alt="IoT Solution">
                </a>
            </div>

            <div class="project">
                <span>Forecast Api App</span>
                <h4>Weather Forecast App</h4>
                <a href="https://github.com/ayoubmori/weather-app" target="_blank">
                    <img src="data:image/gif;base64,{into_img(assets_dir / 'forcast-app.png')}" alt="Machine Learning Model">
                </a>
            </div>

            <div class="project">
                <span>Machine Learning Model</span>
                <h4>Predict Weather model</h4>
                <a href="https://github.com/ayoubmori/predect-weather---mini-projet" target="_blank">
                    <img src="data:image/gif;base64,{into_img(assets_dir / 'predict_weather_model.jpg')}" alt="Mobile App">
                </a>
            </div>
        </main>
    </body>
    </html>

            """)
