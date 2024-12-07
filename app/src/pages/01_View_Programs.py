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
SideBarLinks(show_home=True)

# set the header of the page
st.header('My Programs')
if st.session_state['role'] == 'student':
    st.write("View all available programs")
    response = requests.get('http://api:4000/posts/posts').json()
    logger.info(f'data {response}')

    df = st.dataframe(response, column_order=["applicationId", "title", "description", "location", "programId", "professorId"], hide_index=True)

    @st.dialog("Unenroll in a Program")
    def unenroll_program():
        st.write('Unenroll in a Program')
        applicationId = st.text_input('Application ID')
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

    
    @st.dialog("Enroll")
    def add_application():
        st.write("Enroll")
        programId = st.text_input("programId")
        submitted = st.button('Submit')
        application_data = {
        "programId": programId
        }

        if submitted:
            try:
                response = requests.post('http://api:4000/users/users/applications/5', json=application_data)
                if (response.status_code == 200):
                    st.success("Application Submitted Successfully")
                    
                    # Refresh the dataframe
                    response = requests.get('http://api:4000/users/users/applications/5').json()
                    df = st.dataframe(response, column_order=["userId", "programId", "title", "location", "applied", "accepted", "denied"], hide_index=True)
                else:
                    st.error("Error Submitting Application")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with requests {e}")

    if(st.button('Enroll')):
        add_application() 

    if (st.button('Unenroll in a Program')):
        unenroll_program()

    if (st.button('Refresh')):
        st.rerun()


elif st.session_state['role'] == 'professor':
    st.write(st.session_state['role'])
    response = requests.get('http://api:4000/users/users/programs/1').json()
    logger.info(f'data {response}')
    df = st.dataframe(response, column_order=["title", "description", "location", "programId"], hide_index=True)

    @st.dialog("Update a Program")
    def update_program():
        st.write("Update a Program")
        title = st.text_input("title")
        description = st.text_input("description")
        location = st.text_input("location")
        programId = st.text_input("programId")
        submitted = st.button('Submit')


        program_data = {
            "title": title,
            "description": description,
            "location": location,
            "programId": programId 
        }

        if submitted:
            try:
                response = requests.put('http://api:4000/users/users/programs/1', json=program_data)
                if (response.status_code == 200):
                    st.success("Program Updating")
                    response = requests.get('http://api:4000/users/users/programs/1').json()
                    df = st.dataframe(response, column_order=["title", "description", "location", "programId"], hide_index=True)
                else:
                    st.error("Error editing program")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with requests: {e}")


    @st.dialog("Submit Program")
    def add_program():
        pass

        title = st.text_input("title")
        description = st.text_input("description")
        location = st.text_input("location")
       
        schoolId = st.text_input("schoolId")
        professorId = st.text_input("professorId")
        programStart = st.text_input("programStart")
        programEnd = st.text_input("programEnd")
        approved = 0
        submitted = st.button('Submit')

        program_data = {
            "title": title,
            "description": description,
            "location": location,
            "schoolId": schoolId,
            "professorId": professorId,
            "programStart": programStart,
            "programEnd": programEnd,
            "approved": approved

        }

        if submitted:
            try:
                response = requests.post('http://api:4000/programs/programs', json=program_data)
                if (response.status_code == 200):
                    st.success("Creating Program...")
                    response = requests.get('http://api:4000/users/users/programs/1').json()
                    df = st.dataframe(response, column_order=["title", "description", "location", "programId"], hide_index=True)
                else:
                    st.error("Error making program")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with requests: {e}")




    @st.dialog("Delete a Program")
    def delete_program():
        st.write("Delete a Program")
        programId = st.text_input("programId")
        submitted = st.button('Submit')

        delete_data = {
            "programId": programId
        }

        if submitted:
            try:
                response = requests.delete('http://api:4000/users/users/programs/1', json=delete_data)
                if (response.status_code == 200):
                    st.success("Program Deleted")
                    response = requests.get('http://api:4000/users/users/programs/1').json()
                    df = st.dataframe(response, column_order=["title", "description", "location", "programId"], hide_index=True)
                else:
                    st.error("Error deleting program")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with requests: {e}")

    if (st.button('Update a Program')):
        update_program()

    if (st.button('Submit Program')):
        add_program()

    if (st.button('Delete a Program')):
        delete_program()
    
    if (st.button('Refresh')):
        st.rerun()