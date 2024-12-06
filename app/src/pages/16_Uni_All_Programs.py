import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import datetime
import pydeck as pdk
from urllib.error import URLError
from modules.nav import SideBarLinks
import requests

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Profile")
st.sidebar.header("Profile")
st.write('View Profile')

response = requests.get('http://api:4000/programs/programs/1').json()
logger.info(f'data {response}')

programId = response[0]["programId"]

df = st.dataframe(response, column_order=["title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)

@st.dialog("Edit Programs")
def add_program_dialog():
    st.write('Edit Programs')
    title = st.text_input('Title')
    description = st.text_input('Description')
    approved = st.text_input('Approved')
    schoolId = st.text_input('SchoolId')
    professorId = st.text_input('ProfessorId')
    programStart = st.text_input('Program Start')
    programEnd = st.text_input('Program End')
    location = st.text_input('Location')
    submitted = st.button('Submit')

    program_data = {
        "title": title,
        "description": description,
        "approved": approved,
        "schoolId": schoolId,
        "professorId": professorId,
        "programStart": programStart,
        "programEnd": programEnd,
        "location": location,
    }

    if submitted:
        if program_data["title"] == "":
         program_data["title"] = None
        if program_data["description"] == "":
         program_data["description"] = None
        if program_data["approved"] == "":
         program_data["approved"] = None
        if program_data["schoolId"] == "":
         program_data["schoolId"] = None
        if program_data["professorId"] == "":
         program_data["professorId"] = None
        if program_data["programStart"] == "":
         program_data["programStart"] = None
        if program_data["programEnd"] == "":
         program_data["programEnd"] = None
        if program_data["location"] == "":
         program_data["location"] = None

        logger.info(f'Profile edited {program_data}')

        try:
            response = requests.put('http://api:4000/programs/programs/1', json=program_data)
            if response.status_code == 200:
                st.success("Program edited")
                response = requests.get('http://api:4000/programs/programs/1').json()
                df = st.dataframe(response, column_order=["title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)
            else:
                st.error(f"Error editing Program {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error with requests: {e}")

@st.dialog("Edit Programs")
def add_program_form():
    st.write('Edit Programs')
    title = st.text_input('Title')
    description = st.text_input('Description')
    approved = st.text_input('Approved')
    schoolId = st.text_input('SchoolId')
    professorId = st.text_input('ProfessorId')
    programStart = st.text_input('Program Start')
    programEnd = st.text_input('Program End')
    location = st.text_input('Location')
    submitted = st.button('Submit')


    program_data = {
        "title": title,
        "description": description,
        "approved": approved,
        "schoolId": schoolId,
        "professorId": professorId,
        "programStart": programStart,
        "programEnd": programEnd,
        "location": location,
        
    }

    if submitted:
        if program_data["title"] == "":
         program_data["title"] = None
        if program_data["description"] == "":
         program_data["description"] = None
        if program_data["approved"] == "":
         program_data["approved"] = None
        if program_data["schoolId"] == "":
         program_data["schoolId"] = None
        if program_data["professorId"] == "":
         program_data["professorId"] = None
        if program_data["programStart"] == "":
         program_data["programStart"] = None
        if program_data["programEnd"] == "":
         program_data["programEnd"] = None
        if program_data["location"] == "":
         program_data["location"] = None

        logger.info(f'Profile edited {program_data}')

        try:
            response = requests.post('http://api:4000/programs/programs/', json=program_data)
            if response.status_code == 200:
                st.success("Program edited")
                response = requests.get('http://api:4000/programs/programs/1').json()
                df = st.dataframe(response, column_order=["title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)
            else:
                st.error(f"Error editing Program {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error with requests: {e}")

@st.dialog("Delete Program")
def delete_program_dialog():
    st.write('Delete a program')
    programId = st.number_input('programId', min_value=1, step=1, placeholder='Enter the program ID')
    submitted = st.button('Submit')

    if submitted:
        # Log the data to the console
        logger.info(f'Delete Program submitted with data: {programId}')

        # Send the data to the backend
        try:
            response = requests.delete(f'http://api:4000/programs/programs/{programId}')
            if response.status_code == 200:
                st.success("Program Deleted successfully")
            else:
                st.error("Error Deleting Program")
        except requests.exceptions.RequestException as e:
            st.error(f"Error with requests: {e}")


if st.button('Edit Program'):
    add_program_dialog()
if st.button('Delete Program'):
    delete_program_dialog()
if st.button('Add Program'):
    add_program_form()
if st.button('Refresh'):
    st.rerun()
