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



# ---

uploaded_file = st.file_uploader("Upload Data",['csv','xlsx'])

if uploaded_file is None:
    
    st.text("Kindly Upload Data")


else:
    
    import pandas as pd
    
    try:
    
        df = pd.read_csv(uploaded_file)
        st.table(df.head(20))
        
        
        
        fake = df[df['label'] == 'CG']
        
        fake_count = len(fake)
        
        st.write("Length of Fake Count", fake_count)
        
        
        
        aa = st.button("Delete Fake Reviews")
        
        if aa:
            
        
            df_filtered = df[df['label'] != 'CG']
            df_filtered.to_csv('filtered_file.csv', index=False)
            
            
            # fake = df[df['Label'] == 'CG']
            
            # fake_count = len(fake)
            
            # st.write("Length of Fake Count", fake_count)
            
            
            
            
            
            st.table(df_filtered.head(20))
            
            df1 = pd.read_csv("filtered_file.csv")
            
            fake = df1[df1['label'] == 'CG']
            
            fake_count = len(fake)
            
            st.write("Length of Fake Count", fake_count)
            
        
    except:
        
        df = pd.read_excel(uploaded_file)
        st.table(df.head(20))
        
        aa = st.button("Delete Fake Reviews")
         
        if aa:
             
         
             df_filtered = df[df['label'] != 'CG']
             df_filtered.to_csv('filtered_file.csv', index=False)
             
             
             st.table(df_filtered.head(20))


             # fake = df[df['Label'] == 'CG']
            
            
             # fake_count = len(fake)
            
            
             # st.write("Length of Fake Count", fake_count)



