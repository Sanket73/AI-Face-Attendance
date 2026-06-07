import streamlit as st

from src.screens.Home_screen import Home_screen
from src.screens.Teacher_screen import Teacher_screen
from src.screens.Student_screen import Student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog
def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )
    
    st.markdown(
        '<meta http-equiv="refresh" content="1800">',
        unsafe_allow_html=True
    )
    
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
        
    match st.session_state['login_type']:
        case 'teacher':
            Teacher_screen()
        
        case 'student':
            Student_screen()
            
        case None:
            Home_screen()
            
    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
            
main()