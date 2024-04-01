import streamlit as st
from annotated_text import annotated_text

st.title("😝 Hi, I'm Grace (Jinyu) Rao，")

annotated_text(
    ("UXUI Designer", "", "#faf"),
    " | ",
    ("Artist", "", "#8ef"),
    " | ",
    ("Chinese", "", "#faa"),
    " | ",
    ("Pet lover", "", "#fea"),
    " | ",
    ("Food lover", "", "#afa"),
)

# Image and About
col1, col2 = st.columns(2)

with col1:
    st.image('/Users/jinyurao/Downloads/Me.jpg')

with col2:
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader(" ")
    st.subheader("""
        Skilled in :blue[user research], :blue[interaction], and :blue[visual design], I excel at developing impactful features quickly in :orange[fast-paced] environments.
    """
    )

st.divider()

# Education
st.header("Education")
st.subheader("**University of California, San Diego**")
st.markdown("""
2018 - 2022 | San Diego
- ***B.S.*** in Cognitive Science (HCI) 
- ***B.A.*** in Speculative Design  
"""
)
st.markdown(" ")
st.subheader("**University of Washington**")
st.markdown("""
2023 - 2025 | Seattle
- M.S. in Technology Innovation   
"""
)

st.divider()

# Work Experience
st.header("Work Experience")
st.subheader("Trickle | UXUI Designer")
st.markdown("""
Jul.2022 - Present | Shenzhen, China
1. Standardized design system for components, text, and layout when the senior designer resigned; bridged the collaboration between design, product, and front-end teams, improving team efficiency by 25%.
2. Redesigned screenshot upload feature, enhancing user navigation and information access, leading to increased signups and securing the #1 rank on Product Hunt with over 1000 upvotes.
3. Spearheaded the development of an AI assistant feature, significantly boosting user productivity, engagement, and enhancing brand visibility.
4. Shipped 12 features by analyzing user feedback for root causes, designing variant solutions, and resolving early-stage inconsistencies in prototyping.
5. Streamlined product design strategy by conducting user research, including 3 executive interviews and 100 user surveys, while collaborating on budgeting and setting up survey protocols.
"""
)
st.markdown(" ")
st.subheader("GoKunming | Visual Design Intern")
st.markdown("""
Jul.2019 - Aug.2019 | Kunming, China
1. Designed 3 gift box packages and bags based on company branding and identity, selected for batch production for business purposes.
2. Illustrated over 5 posters for business promotion, and communicated with the managers to customize posters to meet client requirements.
3. Collaborated with design leader to create the GoKunming website prototype, and expedited travel section design for the business.
"""
)

st.divider()

# Interesting Projects
st.header("My Projects")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    st.image('/Users/jinyurao/Downloads/Portfolio/Thumbnail/Mindbud_Thumbnail.jpg')
    st.subheader("MindBud")
    st.markdown("**Mental Health| Mobile Design | UX Research**")
    st.markdown("An app that leverages AI assistance to help users form supportive friendships and guide users through interactive, science-based, personalized lessons about mental health.")
with col2:
    st.image('/Users/jinyurao/Downloads/Portfolio/Thumbnail/Sania_Thumbnail.jpg')
    st.subheader("Sania's Bakery")
    st.markdown("**Client Project | Leadership | UX Design**")
    st.markdown("A UIUX project that led a team of 4 to create the online platform for the client, Sania’s Bakery, facilitating customers to order desserts and customize cakes online. ")

col3, col4 = st.columns(2)
with col3:
    st.image('/Users/jinyurao/Downloads/Portfolio/Thumbnail/Mysophobia_Thumbnail.jpg')
    st.subheader("Mysophobia VR Game")
    st.markdown("**VR Game | Health | Personal Project**")
    st.markdown("An HCI project that designed gamified exposure therapy for Mysophobia patients in VR.")
with col4:
    st.image('/Users/jinyurao/Downloads/Portfolio/Thumbnail/PlantinO2_Thumbnail.jpg')
    st.subheader("PlantinO2")
    st.markdown("**Speculative Design | Installation Art**")
    st.markdown("A project that designed a portable plant-based oxygen cylinder, PlantinO2, which sustainably provides oxygen for humans to breathe in the air-polluted future (in 2060).")

st.divider()

# Hobbies and Interest
st.header("Hobbies and Interest")

# Art
annotated_text(
    ("Art", "", "#8ef"),
)
col1, col2, col3 = st.columns(3)
with col1:
    st.image('/Users/jinyurao/Downloads/art.jpg')
with col2:
    st.image('/Users/jinyurao/Downloads/art 2.jpg')
with col3:
    st.image('/Users/jinyurao/Downloads/art 3.jpg')

# Pet
annotated_text(
    ("Pet lover", "", "#fea")
)
col4, col5, col6 = st.columns(3)
with col4:
    st.image('/Users/jinyurao/Downloads/pet.jpg')
with col5:
    st.image('/Users/jinyurao/Downloads/pet 2.jpg')
with col6:
    st.image('/Users/jinyurao/Downloads/pet 3.jpg')

# Food
annotated_text(
    ("Food lover", "", "#afa"),
)
col7, col8, col9 = st.columns(3)
with col7:
    st.image('/Users/jinyurao/Downloads/food.jpg')
with col8:
    st.image('/Users/jinyurao/Downloads/food 2.jpg')
with col9:
    st.image('/Users/jinyurao/Downloads/food 3.jpg')



