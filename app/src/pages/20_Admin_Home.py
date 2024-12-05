import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')

if st.button('Manage Programs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Manage_My_Programs.py')

if st.button('Manage Users', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Manage_My_Users.py')
