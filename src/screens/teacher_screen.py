import streamlit as st
import time
from src.ui.base_layout import style_background_dashboard , style_base_layout
from src.components.subject_card import subject_card
from src.components.dialog_share_subject import share_subject_dialogue
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.db.db import create_teacher , check_teacher_exists , teacher_login , get_teacher_subject 
from src.components.dialog_create_subject import create_subject_dialogue

def teacher_screen():
    style_background_dashboard()
    style_base_layout()


    if "teacher_data" in st.session_state:
        teacher_dashboard()

    elif 'teacher_login_type' not in st.session_state or st.session_state['teacher_login_type'] == 'login':
        teacher_screen_login()

    elif st.session_state['teacher_login_type'] == 'register':
        teacher_screen_register()




def teacher_dashboard():
    teacher_data =st.session_state['teacher_data']

    c1 , c2 = st.columns(2 , vertical_alignment="center" , gap="xxlarge")

    with c1:
        header_dashboard()

    
    with c2:
        st.subheader(f"""Welcome , {teacher_data['name']}""")
        if st.button("Logout" , type="secondary" , key="loginbackbtn" , shortcut="control+backspace"):
            st.session_state["is_loggedin"] = False
            del st.session_state['teacher_data']
            st.rerun()

    st.space()

    if "current_teacher_tab" not in st.session_state:
        st.session_state["current_teacher_tab"] = "take_attendance"

    tab1 , tab2 , tab3 = st.columns(3)

    with tab1 :
        type1 = "primary" if st.session_state["current_teacher_tab"] == "take_attendance" else "tertiary"
        if st.button("Take attendance" ,type=type1 ,  width="stretch" , icon=":material/ar_on_you:"):
            st.session_state["current_teacher_tab"] = "take_attendance"
            st.rerun()

    with tab2 :
        type2 = "primary" if st.session_state["current_teacher_tab"] == "manage_subject" else "tertiary"
        if st.button("Manage subject" ,type=type2, width="stretch" , icon=":material/book_ribbon:"):
            st.session_state["current_teacher_tab"] = "manage_subject"
            st.rerun()
    
    with tab3 :
        type3 = "primary" if st.session_state["current_teacher_tab"] == "attendance_records" else "tertiary"
        if st.button("Attendance records" , width="stretch" , type=type3 ,icon=":material/cards_stack:"):
            st.session_state["current_teacher_tab"] = "attendance_records"
            st.rerun()

    st.divider()
    

    if st.session_state["current_teacher_tab"] == "take_attendance":
        teacher_tab_take_attendance()

    if st.session_state["current_teacher_tab"] == "manage_subject":
        teacher_tab_manage_subject()

    if st.session_state["current_teacher_tab"] == "attendance_records":
        teacher_tab_attendance_records()

    

    footer_dashboard()

def teacher_tab_take_attendance():
    st.header('Take AI Attendance')

def teacher_tab_manage_subject():
    teacher_id = st.session_state.teacher_data["teacher_id"]
    col1 , col2 = st.columns(2)
    with col1:
        st.header('Manage subjects' , width = "stretch")
    
    with col2 :
        if st.button("Create New Subject" , width="stretch"):
            create_subject_dialogue(teacher_id)

    #List all subjects
    subjects = get_teacher_subject(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("🫂", "Students", sub['total_students']),
                ("🕰️", "Classes", sub['total_classes']),
            ]
        
        def share_btn():
            if st.button(f"Share code : {sub['name']}" , key = f"share_{sub['subject_code']}" , icon = ":material/share:"):
                #use in QR generation task
                share_subject_dialogue(sub['name'] , sub['subject_code'])

        subject_card(
            name = sub['name'],
            code = sub['subject_code'],
            section = sub['section'],
            stats = stats,
            footer_callback = share_btn
        )
    else:
        st.info("NO SUBJECT FOUND. CREATE ONE ABOVE")

    




def teacher_tab_attendance_records():
    st.header('Attendance records')




def login_teacher(username , password):
    if not username or not password:
        return False
    
    teacher = teacher_login(username , password)


    if teacher:
        st.session_state['user_role'] = 'teacher'
        st.session_state['teacher_data'] = teacher
        st.session_state['is_loggedin'] = True
        return True
    
    return False



def register_teacher(teacher_username , teacher_name , teacher_pass , teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False , "All fields are required"
    
    if check_teacher_exists(teacher_username):
        return False , "Username already taken"

    if teacher_pass != teacher_pass_confirm:
        return False , "Password doesn't match"
    
    try:
        create_teacher(teacher_username , teacher_pass , teacher_name)
        return True , "Succesfully Created! Login Now"
    except Exception as e:
        return False , "Unexpected Error"


def teacher_screen_login():

    c1 , c2 = st.columns(2 , vertical_alignment="center" , gap="xxlarge")

    with c1:
        header_dashboard()

    
    with c2:
        if st.button("Go back to Home" , type="secondary" , key="loginbackbtn" , shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Login using password" , text_alignment="center")
    st.space()
    st.space()

    teacher_username = st.text_input("Enter your username" , placeholder="srikritarth")

    teacher_pass = st.text_input("Enter your password" , type="password" , placeholder="Enter Password")

    st.divider()

    btncl1 ,btncl2 = st.columns(2)

    with btncl1:
        if st.button("Login" , icon=':material/passkey:' , shortcut="control+enter" , width="stretch"):
            if login_teacher(teacher_username , teacher_pass):
                st.toast("Welcome back !" , icon = "👋")
                time.sleep(1)
                st.rerun()

            else:
                st.error("Invalid username and password combination")

    with btncl2:
        if st.button("Register Instead" ,type="primary" , icon=':material/passkey:'  , width="stretch"):
            st.session_state['teacher_login_type'] = 'register'

    footer_dashboard()


def teacher_screen_register():

    c1 , c2 = st.columns(2 , vertical_alignment="center" , gap="xxlarge")

    with c1:
        header_dashboard()

    
    with c2:
        if st.button("Go back to Home" , type="secondary" , key="loginbackbtn" , shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
    
    st.header("Register your teacher profile")

    st.space()
    st.space()

    teacher_username = st.text_input("Enter your username" , placeholder="srikritarth")

    teacher_name = st.text_input("Enter your name" , placeholder="Kritarth Srivastava")

    teacher_pass = st.text_input("Enter your password" , type="password" , placeholder="Enter Password")

    teacher_pass_confirm = st.text_input("Confirm your password" , type="password" , placeholder="Enter Password")

    st.divider()

    btncl1 ,btncl2 = st.columns(2)

    with btncl1:
        if st.button("Register now" , icon=':material/passkey:' , shortcut="control+enter" , width="stretch"):
            success , message = register_teacher(teacher_username , teacher_name , teacher_pass , teacher_pass_confirm)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state['teacher_login_type'] = 'login'
                st.rerun()
            else:
                st.error(message)

    with btncl2:
        if st.button("Login Instead" ,type="primary" , icon=':material/passkey:'  , width="stretch"):
            st.session_state['teacher_login_type'] = "login"

    footer_dashboard()