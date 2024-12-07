import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks(show_home=True)

# Northeastern Admin Home Page
st.title(f"Welcome to NUConnect, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.subheader('What would you like to do today?')

if st.button('Manage Posts', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_View_All_Post.py')

if st.button('Manage Programs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Manage_My_Programs.py')

if st.button('Manage Schools', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/View_All_Schools.py')

if st.button("Manage Users",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/18_Uni_All_Users.py')
  
if st.button('Manage Global User Roles', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_View_All_Roles.py')
