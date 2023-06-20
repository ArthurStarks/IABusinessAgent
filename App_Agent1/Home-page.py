#Importation des librairies
import streamlit as st
from streamlit_option_menu import option_menu

#Configuration des pages
st.set_page_config(
    page_title="Bienvenue chez Flex IA Business",
    page_icon="👋",
)


 #Menu principal
#with st.sidebar : 
selected = option_menu(
        menu_title="Agent Flex IA",
        options=["Agent Assistant", "Agent Mailing", "Agent Fitgap"],
        icons=["chat-left-dots-fill", "magic","robot"],
        #menu-icon="cast",
        orientation="horizontal",
    )
if selected == "Home" :
    st.title(f"Bienvenue au {selected}")
if selected == "Agent Mailing" :
    st.title(f"Je suis l'{selected} à votre service")
if selected == "Agent Fitgap" :
    st.title(f"Je suis l' {selected} à votre service")



#Page principale
st.title("Flex IA")
#st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Que puis-je faire pour vous ?", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)