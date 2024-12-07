import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks(show_home=True)

st.write("# About NUConnect")

st.markdown(
    """
    NUConnect is a centralized platform designed to simplify the dialogue application process between students, faculty, and universities.

    This project aims to address the ambiguity and inefficiencies present in the traditional study abroad process, offering an easy-to-use interface for students, professors, and administrators to manage and apply for dialogues.

    Some key features for Student in NUConnect include:

    - **User Application Management**: Users can easily apply for programs, track their application status, and even delete applications if needed.
    - **Profile Management**: Update your personal information, academic preferences, and track your participation history.
    - **Streamlined Application Tracking**: Keep track of your applications, receive status updates, and manage deadlines all in one place.
    
    Additionally, Teachers in NUConnect can:
    
    - **School and Role Management**: Administrators can add new schools, manage roles, and assign appropriate permissions to different users.
    - **User Roles and Permissions**: Different roles such as students, professors, and administrators are provided with specific functionalities to enhance usability and security.
    - **Admin Dashboard**: University administrators can manage programs, approve applications, and oversee participant activities efficiently.
    - **Post Creation and Management**: Teachers and Admins can create, edit, and delete posts related to different programs.

    """)

st.write("## Meet the Team")
team_members = [
    {"name": "Isaac Polite", "email": "polite.i@northeastern.edu"},
    {"name": "Pierre Dang", "email": "dang.pi@northeastern.edu"},
    {"name": "Catherine Zhou", "email": "zhou.cat@northeastern.edu"}
    {"name": "Toby Chan", "email": "chan.to@northeastern.edu"},
    {"name": "Alen Ganopolsky", "email": "ganopolsky.a@northeastern.edu"},
]
for member in team_members:
    st.write(f"- **{member['name']}**: {member['email']}")
