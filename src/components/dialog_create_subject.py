import streamlit as st
from src.db.db import create_subject


@st.dialog("Create New Teacher")
def create_subject_dialogue(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject code" , placeholder="CS101")
    sub_name = st.text_input("Subject name" , placeholder="Introdution to C programming")
    section = st.text_input("Section" , placeholder="A")

    if st.button("Create Subject Now" , type= "primary" , width = "stretch"):
        if sub_id and sub_name and section:
            try:
                create_subject(sub_id , sub_name , section , teacher_id)
                st.toast("Subject created successfully")
                st.rerun()
            except Exception as e:
                st.error(f"Error : str{e}")
        else:
            st.warning("Please fill all the fields to proceed")