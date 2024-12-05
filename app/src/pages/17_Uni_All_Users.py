import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write('### Manage all Uni Users')

# Get the data from the backend
response = requests.get('http://api:4000/users/users').json()

st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId", "createdAt", "lastLogin"], hide_index=True)