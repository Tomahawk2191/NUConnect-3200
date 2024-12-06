import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
import pydeck as pdk
from urllib.error import URLError
from modules.nav import SideBarLinks
import requests

import matplotlib.pyplot as plt
import numpy as np

from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('My Programs')
if st.session_state['role'] == 'student':
    st.write(st.session_state['role'])
    response = requests.get('http://api:4000/users/users/4/programs').json()
    logger.info(f'data {response}')

    df = st.dataframe(response, column_order=["title", "description", "location", "programId", "professorId", "applicationId"], hide_index=True)

    @st.dialog("Unenroll in a Program")
    def unenroll_program():
        st.write('Unenroll in a Program')
        applicationId = st.text_input('applicationId')
        submitted = st.button('Submit')

        user_data = {
            "applicationId": applicationId
        }

        if submitted:
            try:
                response = requests.delete('http://api:4000/users/users/4/programs', json=user_data)
                if (response.status_code == 200):
                    st.success("Program Unenrolled")
                    response = requests.get('http://api:4000/users/users/4/programs').json()
                    df = st.dataframe(response, column_order=["title", "description", "location", "programId", "professorId", "applicationId"], hide_index=True)
                else:
                    st.error("Error editing user")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with requests: {e}")

    if (st.button('Unenroll in a Program')):
        unenroll_program()
    if (st.button('Refresh')):
        st.rerun()


elif st.session_state['role'] == 'professor':
    st.write(st.session_state['role'])

