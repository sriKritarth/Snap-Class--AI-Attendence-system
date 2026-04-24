import streamlit as st
import io
import segno


@st.dialog("Share class link")
def share_subject_dialogue(subject_name , subject_code):
    app_domain = "http://localhost:8501/"
    join_url = f"{app_domain}/?join-code = {subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out , kind='png'  ,scale = 10 , border = 1)

    col1 , col2 = st.columns(2)

    with col1:
        st.markdown("### Copy link")
        st.code(join_url , language='text')
        st.code(subject_code , language='text')
        st.info("Copy this link to share on Whatsapp or Email")
    
    with col2:
        st.markdown("### Scan to join")
        st.image(out.getvalue() , caption="QRCODE for joining class")    
    