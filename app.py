import streamlit as st

def main():
    st.header("This is title")
    name  = st.text_input("Enter your name")
    col1,col2 = st.columns(2, gap = "xsmall")
    with col1:

        if st.button("hi",type = "primary",key = "btn1",width = "stretch"):
           print('hi', name)
    with col2:

        if st.button('bye', type = "secondary",key = "btn2",width = "stretch"):
           print('bye', name)

    st.markdown("""
        

        <div>
             <p> "Hey this is princi."</p>
        </div>
        <style>
           button{
               background:#778da9 !important;
             }

             </style>

    """,unsafe_allow_html = True)


main()