import streamlit as st

st.title("Simple Hello App 👋")

with st.form("name_form"):
    name = st.text_input("Enter your name:")
    submitted = st.form_submit_button("Say Hello")

    if submitted:
        st.success(f"Hello, {name}!")
