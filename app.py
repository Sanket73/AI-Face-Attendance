import streamlit as st

from src.screens.Home_screen import Home_screen
from src.screens.Teacher_screen import Teacher_screen
from src.screens.Student_screen import Student_screen

def main():
    
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
        
    match st.session_state['login_type']:
        case 'teacher':
            Teacher_screen()
        
        case 'student':
            Student_screen()
            
        case None:
            Home_screen()
            
main()