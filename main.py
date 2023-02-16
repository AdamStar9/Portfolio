import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Adam Starostik")
    content = """Hi, My name is Adam and I´m new to Python. I have successfully passed two courses in order to learn Python and 
    I´m ready to start a new path in my life working with Python on the every day basis.
    
    """
    st.info(content)