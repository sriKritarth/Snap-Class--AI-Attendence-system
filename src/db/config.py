import streamlit as st

from supabase import create_client , Client

#instance of db 
supabase : Client = create_client(
    st.secrets['SUPABASE_URL'],
    st.secrets['SUPABASE_API_KEY']
)