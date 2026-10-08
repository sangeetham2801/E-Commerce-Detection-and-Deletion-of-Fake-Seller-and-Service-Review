#======================== IMPORT PACKAGES ===========================
import streamlit as st
import base64
import seaborn as sns


#========================  BACKGROUND IMAGE ===========================


st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:50px;font-family:Caveat, sans-serif;">{"E-Commerce Detection and Deletion of Fake Seller and Service Review"}</h1>', unsafe_allow_html=True)
st.write("-------------------------------------------")



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



# ----------------------------------------------

import pickle

with open('model.pickle', 'rb') as f:
    hyb = pickle.load(f)
 
with open('label.pickle', 'rb') as f:
    sentiment = pickle.load(f)  
    

 
with open('vector.pickle', 'rb') as f:
    vector = pickle.load(f)  




user_input = st.text_input("Enter Message  !!!")


aa = st.button("PREDICT")



if aa:
    
    count_data = vector.transform([user_input])
    pred_rf = hyb.predict(count_data)

        
    if pred_rf == 0 :
        
        
        st.write("----------------------------------------------------------------------")
    
    
        st.markdown(f'<h1 style="color:#000000 ;font-size:24px;text-align:center;font-family:convat;;">{"Identified - Fake review"}</h1>', unsafe_allow_html=True)
    
    else: 
        
        st.write("----------------------------------------------------------------------")
    
    
        st.markdown(f'<h1 style="color:#000000 ;font-size:24px;text-align:center;font-family:convat;;">{"Identified - Real review"}</h1>', unsafe_allow_html=True)
            


