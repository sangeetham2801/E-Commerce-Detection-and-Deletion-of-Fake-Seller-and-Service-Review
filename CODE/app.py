import streamlit as st

import base64
import cv2
import sqlite3
from streamlit_option_menu import option_menu

# ================ Background image ===

st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:50px;font-family:Caveat, sans-serif;">{"E-Commerce Detection and Deletion of Fake Seller and Service Review"}</h1>', unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.jpg')

# ----------------------



selected = option_menu(
    menu_title=None, 
    options=["Detection", "Deletion"],  
    orientation="horizontal",
)


st.markdown(
    """
    <style>
    .option_menu_container {
        position: fixed;
        top: 20px;
        right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if selected == 'Detection':
    
    
    
    
    
        import subprocess
        subprocess.run(['streamlit','run','Prediction.py'])
        
        
if selected == 'Deletion':
    
        import subprocess
        subprocess.run(['streamlit','run','Delete.py'])      
        
        
        
        
        
        
        
        
        
        
        