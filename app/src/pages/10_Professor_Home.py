import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Northeastern Professor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Edit/Post Programs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_EditPost_Programs.py')

if st.button("View Applications",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Applications.py')

if st.button('View Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Prof_Profile.py')