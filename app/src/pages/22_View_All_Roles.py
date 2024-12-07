import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks(show_home=True)

st.write('### View Roles')

# Get the data from the backend
try:
    response = requests.get('http://api:4000/roles/role').json()
    # Display the roles in a dataframe
    st.dataframe(
        response,
        column_order=["roleId", "name", "canPost", "canApprove", "canAssignProf", "canApply", "canRetract",
                      "canEditOwn", "canEditAll", "canDelteOwn", "canDeleteAll", "canUpdateAccess"],
        hide_index=True
    )
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching roles: {e}")