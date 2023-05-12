import streamlit as st
import pandas
import os

from pympler.util.bottle import app

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Adam Starostik")
    content = """Hi, My name is Adam and I´m new to Python. I have successfully 
    passed two courses in order to learn Python and 
    I´m ready to start a new path in my life working with 
    Python on the every day basis.
    
    """
    st.info(content)

content2 = """
Below you can see some of the apps I have built in Python. Fell free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:6].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[6:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))