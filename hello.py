import streamlit as st

st.write("Hello World")
st.write("## This is a H2 Title!")
x = st.text_input("Movie", "Star Wars")

if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")
