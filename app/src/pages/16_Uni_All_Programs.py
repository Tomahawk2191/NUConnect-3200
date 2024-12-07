import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import datetime
import pydeck as pdk
from urllib.error import URLError
from modules.nav import SideBarLinks
import requests
import pandas as pd

SideBarLinks(show_home=True)

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Programs")
st.sidebar.header("View Programs")
st.write('View Programs')

# function to fetch program data from the API
def fetch_programs():
    try:
        response = requests.get('http://api:4000/programs/programs').json()
        logger.info(f'data {response}')
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching programs: {e}")
        return []

response = fetch_programs()

# ensure there's data to display
if response:
    st.dataframe(response, column_order=["programId", "title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)
else:
    st.write("No programs available to display.")



# edit Program Dialog
@st.dialog("Edit Programs")
def edit_program_dialog():
    response = fetch_programs()

    st.write('Which program would you like to edit?')
    programId_to_edit = st.number_input('Program ID to Edit', min_value=1, max_value=len(response), step=1)

    program_data = next((program for program in response if program["programId"] == programId_to_edit), None)

    if program_data:
        
        program_data["programStart"] = datetime.datetime.strptime(program_data["programStart"], "%a, %d %b %Y %H:%M:%S %Z").date()
        program_data["programEnd"] = datetime.datetime.strptime(program_data["programEnd"], "%a, %d %b %Y %H:%M:%S %Z").date()
        program_data["approved"] = True if program_data["approved"] == 1 else False
        
        st.write('You are editing program:', programId_to_edit)
        title = st.text_input('Title', value=program_data["title"])
        description = st.text_input('Description', value=program_data["description"])
        approved = st.checkbox('Approved?', value=program_data["approved"])
        schoolId = st.number_input('SchoolId', value=program_data["schoolId"], min_value=1, step=1)
        professorId = st.number_input('ProfessorId', value=program_data["professorId"], min_value=1, step=1)
        programStart = st.date_input('Program Start', value=program_data["programStart"])
        programEnd = st.date_input('Program End', value=program_data["programEnd"])
        location = st.text_input('Location', value=program_data["location"])
        submitted = st.button('Submit')

        if submitted:
            updated_program_data = {
              "title": title or program_data["title"],
              "description": description or program_data["description"],
              "approved": int(approved),
              "schoolId": schoolId or program_data["schoolId"],
              "professorId": professorId or program_data["professorId"],
              "programStart": str(programStart) or program_data["programStart"],
              "programEnd": str(programEnd) or program_data["programEnd"],
              "location": location or program_data["location"]
            }

            logger.info(f'Edited Program Data: {updated_program_data}')
            try:
                response = requests.put(f'http://api:4000/programs/programs/{programId_to_edit}', json=updated_program_data)
                if response.status_code == 200:
                    st.success("Program edited successfully")
                    response = fetch_programs()  
                    st.dataframe(response, column_order=["programId", "title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)
                else:
                    st.error(f"Error editing program: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with request: {e}")


@st.dialog("Add Programs")
def add_program_form():
    st.write('Add a new program')
    title = st.text_input('Title')
    description = st.text_input('Description')
    approved = st.checkbox('Approved?')
    schoolId = st.text_input('SchoolId')
    professorId = st.text_input('ProfessorId')
    programStart = st.date_input('Program Start')
    programEnd = st.date_input('Program End')
    location = st.text_input('Location')
    submitted = st.button('Submit')

    program_data = {
        "title": title,
        "description": description,
        "approved": int(approved),
        "schoolId": schoolId,
        "professorId": professorId,
        "programStart": str(programStart),
        "programEnd": str(programEnd),
        "location": location,
    }

    if submitted:
      if not all(value != "" for value in program_data.values()):
        st.error("Please fill in all the fields.")
      else:
        logger.info(f'Program Data submitted: {program_data}')
        try:
            response = requests.post('http://api:4000/programs/programs', json=program_data)
            if response.status_code == 200:
                st.success("Program added successfully")
                response = fetch_programs()  
                st.dataframe(response, column_order=["programId", "title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)
            else:
                st.error(f"Error adding program: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error with request: {e}")

@st.dialog("Delete Program")
def delete_program_dialog():
    st.write('Delete a program')
    programId = st.number_input('Program ID', min_value=1, step=1, placeholder='Enter the program ID')
    submitted = st.button('Submit')

    if submitted:
        logger.info(f'Delete Program submitted with ID: {programId}')
        try:
            response = requests.delete(f'http://api:4000/programs/programs/{programId}')
            if response.status_code == 200:
                st.success("Program deleted successfully")
            else:
                st.error("Error deleting program")
        except requests.exceptions.RequestException as e:
            st.error(f"Error with request: {e}")

if st.button('Edit Program'):
    edit_program_dialog()
if st.button('Delete Program'):
    delete_program_dialog()
if st.button('Add Program'):
    add_program_form()
if st.button('Refresh'):
    st.rerun()

# added sort functionality
st.subheader("Sort Programs")
sort_by = st.selectbox("Sort programs by", ["title", "programStart", "programEnd", "schoolId", "professorId"])
sorted_programs = sorted(response, key=lambda x: x[sort_by])
st.dataframe(sorted_programs, column_order=["programId", "title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)

