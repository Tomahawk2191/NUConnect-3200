import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Northeastern Student, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Programs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_View_Programs.py')

if st.button('View Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Profile.py')

if st.button('Track Application Status', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Application_Stat.py')
  
if st.button('View All Users', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/18_Uni_All_Profile.py')

if st.button('View All User Tags', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/user_tag.py')

if st.button('View All Users Roles', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_View_All_Roles.py')