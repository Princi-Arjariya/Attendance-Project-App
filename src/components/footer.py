import streamlit as st

def footer_home():
    st.markdown(f"""
               
         <div style="display:flex; gap:6px; align-items:center; justify-content:center; margin-top:30px;">
            <p style="font-weight:bold; color:white;"> Created by Princi Arjariya 😎 </p>
         </div>
               
               """,unsafe_allow_html = True)


def footer_dashboard():
    st.markdown(f"""
               
         <div style="display:flex; gap:6px; align-items:center; justify-content:center; margin-top:30px;">
            <p style="font-weight:bold; color:black;"> Created by Princi Arjariya 😎 </p>
         </div>
               
               """,unsafe_allow_html = True)