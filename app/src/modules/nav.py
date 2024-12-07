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
    st.sidebar.page_link("pages/10_Professor_Home.py", label="Home", icon="🏠")

def ProfProgramsNav():
    st.sidebar.page_link(
        "pages/16_Uni_All_Programs.py", label="Programs", icon="📝"
    )

def ProfProfileNav():
    st.sidebar.page_link(
        "pages/02_Profile.py", label="Profile", icon="👤"
    )

def ProfAppNav():
    st.sidebar.page_link(
        "pages/03_Application_Stat.py", label="Applications", icon="📊"
    )

## ------------------------ Role of Jennie Harvard University ------------------------
def UniHomeNav():
    st.sidebar.page_link("pages/15_University_Home.py", label="Home", icon="🏠")

def UniAllProgamsNav():
    st.sidebar.page_link(
        "pages/16_Uni_All_Programs.py", label="Manage Programs", icon="📝"
    )

def UniProfileNav():
    st.sidebar.page_link(
        "pages/02_Profile.py", label="Profile", icon="👤"
    )

def UniAllUsersNav():
    st.sidebar.page_link(
        "pages/18_Uni_All_Users.py", label="Manage Users", icon="📊"
    )
## ------------------------ Role of Lisa NEU Admin ------------------------
def AdHomeNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="Home", icon="🏠")

def AdProgramNav():
    st.sidebar.page_link(
        "pages/16_Uni_All_Programs.py", label="Manage Programs", icon="📝"
    )

def AdUserNav():
    st.sidebar.page_link(
        "pages/18_Uni_All_Users.py", label="Manage Users", icon="👤"
    )

def AdRolesNav():
    st.sidebar.page_link(
        "pages/22_View_All_Roles.py", label="Manage Roles", icon="👤"
    )

def AdAllPostNav():
    st.sidebar.page_link(
        "pages/23_View_All_Post.py", label="Manage Posts", icon="📝"
    )

def AdAllSchoolstNav():
    st.sidebar.page_link(
        "pages/View_All_Schools.py", label="Manage Schools", icon="🏫"
    )

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add school logo - if the user is an outside administrator, show the Harvard logo
    if st.session_state["authenticated"] and st.session_state['role'] == 'outside_administrator':
        school_image = st.sidebar.image("assets/harvard.png", width=150)
    else:
        school_image = st.sidebar.image("assets/logo.png", width=150)
        
    

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
        if st.session_state['role'] == 'outside_administrator':
            UniHomeNav(),
            UniProfileNav(),
            UniAllProgamsNav(),
            UniAllUsersNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'administrator':
            AdHomeNav(),
            AdAllPostNav(),
            AdProgramNav(),
            AdAllSchoolstNav(),
            AdUserNav(),
            AdRolesNav(),


    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py") 