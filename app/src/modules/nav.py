# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def MainNav():
    st.sidebar.page_link("Home.py", label="Main", icon="🔗")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


#### ------------------------ Role of Dao Student ------------------------
def StuHomeNav():
    st.sidebar.page_link(
        "pages/00_Student_Home.py", label="Home", icon="🏠"
    )

def StuProfileNav():
    st.sidebar.page_link(
        "pages/02_Profile.py", label="Profile", icon="👤"
    )

def StuProgramsNav():
    st.sidebar.page_link(
        "pages/01_View_Programs.py", label="Programs", icon="📝"
    )

def StuAppStatNav():
    st.sidebar.page_link(
        "pages/03_Application_Stat.py", label="Application Status", icon="📊"
    )

## ------------------------ Role of Cooper Professor ------------------------
def ProfHomeNav():
    st.sidebar.page_link("pages/10_Professor_Home.py", label="Professor Home", icon="🏠")

def ProfProgramsNav():
    st.sidebar.page_link(
        "pages/11_EditPost_Programs.py", label="Programs", icon="📝"
    )

def ProfProfileNav():
    st.sidebar.page_link(
        "pages/12_Prof_Profile.py", label="Profile", icon="👤"
    )

def ProfAppNav():
    st.sidebar.page_link(
        "pages/13_Applications.py", label="Applications", icon="📊"
    )

## ------------------------ Role of Jennie Harvard University ------------------------
def UniHomeNav():
    st.sidebar.page_link("pages/15_University_Home.py", label="Havard Home", icon="🏠")

def UniAllProgamsNav():
    st.sidebar.page_link(
        "pages/16_Uni_All_Programs.py", label="Programs", icon="📝"
    )

def UniProfileNav():
    st.sidebar.page_link(
        "pages/12_Prof_Profile.py", label="Profile", icon="👤"
    )

def UniAllUsersNav():
    st.sidebar.page_link(
        "pages/18_Uni_All_Users.py", label="Applications", icon="📊"
    )
#### ------------------------ Role of Lisa NEU Admin ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/15_University_Home.py", label="System Admin", icon="🖥️")
    st.sidebar.page_link("pages/21_Manage_My_Programs.py", label="ML Model Management", icon="🏢")


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        MainNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # If user is Student show Student Sidebar Links 
        if st.session_state['role'] == 'student':
            StuHomeNav(),
            StuProfileNav(),
            StuProgramsNav(),
            StuAppStatNav()

        # If user is Professor show Professor Sidebar Links 
        if st.session_state['role'] == 'professor':
            ProfHomeNav(),
            ProfProfileNav(),
            ProfProgramsNav(),
            ProfAppNav()
        
        # If user is University show University Sidebar Links 
        if st.session_state['role'] == 'school':
            UniHomeNav(),
            UniProfileNav(),
            UniAllProgamsNav(),
            UniAllUsersNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'admin':
            AdminPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py") 