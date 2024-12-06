import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome NUConnect, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Manage Available Programs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/16_Uni_All_Programs.py')

if st.button("Manage All Users",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/17_Uni_All_Users.py')

if st.button('View All Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/18_Uni_All_Profile.py')