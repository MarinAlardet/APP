import streamlit as st

# CSS code as a string
css_style = """
/* Background gradient */
body {
    background: linear-gradient(135deg, #6E44FF, #9B88FF);
    color: #ffffff;
    font-family: Arial, sans-serif;
}

h1, h2 {
    text-align: center;
    color: #ffffff;
    font-weight: bold;
}

/* Navigation bar container */
.navbar {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    gap: 15px;
}

/* Navigation buttons */
.nav-button {
    background-color: #ffffff;
    color: #6E44FF;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
}

.nav-button:hover {
    background-color: #6E44FF;
    color: #ffffff;
}

.active {
    background-color: #6E44FF;
    color: #ffffff;
}
"""

# Apply CSS
st.markdown(f"<style>{css_style}</style>", unsafe_allow_html=True)

# Header
st.markdown("<h1>Mon Site de Skateboard</h1>", unsafe_allow_html=True)
st.markdown("<h2>Explorez les différentes sections</h2>", unsafe_allow_html=True)

# Navigation bar
st.markdown("<div class='navbar'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

# Define the active page
if "page" not in st.session_state:
    st.session_state.page = "Homepage"

# Buttons for navigation
if col1.button("Homepage"):
    st.session_state.page = "Homepage"
if col2.button("Statistiques"):
    st.session_state.page = "Statistiques"
if col3.button("Liste des Skateurs"):
    st.session_state.page = "Liste des Skateurs"

# Display the active page content
if st.session_state.page == "Homepage":
    st.markdown("<div class='content active'>Bienvenue sur la page d'accueil !</div>", unsafe_allow_html=True)
elif st.session_state.page == "Statistiques":
    st.markdown("<div class='content active'>Section Statistiques</div>", unsafe_allow_html=True)
elif st.session_state.page == "Liste des Skateurs":
    st.markdown("<div class='content active'>Section Liste des Skateurs</div>", unsafe_allow_html=True)
