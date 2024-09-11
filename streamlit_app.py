import streamlit as st
from PIL import Image

# Configuration de la page avec un emoji et un layout large
st.set_page_config(page_title="🌟 My Virtual Profile Page", layout="wide")


# Style coloré avec emojis et couleurs joyeuses
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>👾 Bienvenue dans le monde d'Eugénie🌟</h1>", unsafe_allow_html=True)

# Ajouter une phrase d'introduction joyeuse
st.markdown("<h3 style='text-align: center; color: #00BFFF;'>Plongeons dans l'univers 3D et de la réalité virtuelle ensemble !</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2.3, 2, 1])

with col2:
    st.image("img/IMG_7092.jpg", caption="C'est moi, Eugénie !", width=200)

# Section d'information personnelle centrée

# CSS pour animer le bouton en 3D
st.markdown("""
    <style>
    .button-3d {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        color: black;
        background-color: #002ebf;
        border: none;
        border-radius: 5px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease;
    }

    .button-3d:hover {
        transform: translateY(-5px) scale(1.05);
        background-color: #462f9e;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }

    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center;">
    <h2 style='color: #FF6347;'>✨ Informations personnelles</h2>
    <ul style="list-style-type: none;">
        <li>Eugénie Nakouzi</li>
        <li>21 ans et toute ses dents!</li>
        <li>Paris, France</li>
    </ul>
</div>
""", unsafe_allow_html=True)
# Ajouter un bouton 3D avec redirection vers le CV
st.markdown("""
<div style="text-align: center; margin-top: 20px;">
    <a href="https://www.canva.com/design/DAGDy6g7xkg/2IuG5tRiMry9-rHYy9iYPw/view?utm_content=DAGDy6g7xkg&utm_campaign=designshare&utm_medium=link&utm_source=editor" target="_blank" class="button-3d">💼 Voir mon CV</a>
</div>
""", unsafe_allow_html=True)

# Section compétences en développement centrée
st.markdown("""
<div style="text-align: center;">
    <h2 style='color: #FF6347;'>🔧 Mes compétences en développement 💻</h2>
    <ul style="list-style-type: none;">
        <li>🐍 <strong>Python</strong></li>
        <li>📶 <strong>Création et gestion des bases de données SQL</strong></li>
        <li>🌐 <strong>Développement web en Vue.js, HTML & CSS, Javascript, Java</strong></li>
        <li>✨ <strong>Développement Réalité Virtuelle avec Unity C#</strong></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Section qualités humaines centrée
st.markdown("""
<div style="text-align: center;">
    <h2 style='color: #FF6347;'>🌟 Mes qualités humaines 💡</h2>
    <ul style="list-style-type: none;">
        <li>📢 <strong>Communication</strong></li>
        <li>🕰️ <strong>Ponctualité</strong></li>
        <li>🧍‍♀️ <strong>Autonomie</strong></li>
        <li>🤝 <strong>Esprit d'équipe</strong></li>
        <li>⭐ <strong>Créative</strong></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Section des projets récents avec les détails des projets
st.markdown("<h2 style='text-align: center; color: #FF6347;'>🚀 Projets récents</h2>", unsafe_allow_html=True)

# Projet Flappy Bird
st.markdown("""
    <div style='text-align: center;'>
        <h3 style='color: #1E90FF; font-size: 24px; font-weight: bold;'> Flappy Bird</h3>
        <p style='font-size: 16px;'>L'un des jeux les plus connus en 2D, l'incontournable Flappy Bird! 🪽<br> 
        Réalisé avec Unity en C#.</p>
    </div>
""", unsafe_allow_html=True)

# Projet Combattack
st.markdown("""
    <div style='text-align: center;'>
        <h3 style='color: #32CD32; font-size: 24px; font-weight: bold;'>Combattack</h3>
        <p style='font-size: 16px;'>Un jeu en 3D en cours de développement. Le joueur, vue en troisième personne, affronte un monstre. ⚔️<br> 
        Développé avec Unity en C#.</p>
    </div>
""", unsafe_allow_html=True)

# Projet Locomotive
st.markdown("""
    <div style='text-align: center;'>
        <h3 style='color: #1E90FF; font-size: 24px; font-weight: bold;'>Locomotive</h3>
        <p style='font-size: 16px;'>Site web permettant de rechercher un itinéraire d'un point A à un point B, avec un aperçu sur la consommation de CO2 🍃 et sans utiliser de cookies 🍪 !<br>
        Conçu avec Vue.js, JavaScript, Java, et Python.</p>
    </div>
""", unsafe_allow_html=True)

# Projet Lifebrary
st.markdown("""
    <div style='text-align: center;'>
        <h3 style='color: #32CD32; font-size: 24px; font-weight: bold;'>Lifebrary</h3>
        <p style='font-size: 16px;'>Librairie en ligne.<br> Côté client : réservation de livres avec suivi de rendu et des retards. <br> 
        Côté administrateur : gestion des stocks et informations clients.<br>
        Fait avec Vue.js, JavaScript, et MySQL.</p>
    </div>
""", unsafe_allow_html=True)



# Section des réseaux sociaux avec des emojis pour chaque réseau
st.markdown("<h2 style ='text-align: center;'> 📱 Retrouvez-moi sur les réseaux</h2>" ,unsafe_allow_html=True )
st.markdown("<h3 style = 'text-align: center;'><a href=https://www.linkedin.com/in/eugénie-nakouzi>LinkedIn</a href></h3> <h3 style = 'text-align: center;'><a href=https://github.com/Eugenienakouzi> Github </a href></h3>", unsafe_allow_html=True)


st.markdown("""
<div style="text-align: center;">
    <h2 style='color: #FFFFFF;'>📬 Me contacter</h2>
    <ul style="list-style-type: none;">
        <li>📞 06.52.49.44.87</li>
        <li>📩 eugenie_nakouzi@outlook.fr</li>
        <p>Hâte d'échanger avec vous 😊</p>
    </ul>
</div>
""", unsafe_allow_html=True)


# Section finale avec un rappel à la 3D et la réalité virtuelle
st.markdown("""
<hr>
<h3 style='text-align: center; color: #8A2BE2;'>🎮 Merci d'avoir visité mon profil ! J'adore explorer de nouveaux horizons, en particulier dans le domaine de la 3D et de la réalité virtuelle. 🕶️</h3>
""", unsafe_allow_html=True)
