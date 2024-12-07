import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks


logger = logging.getLogger(__name__) 
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

if (st.session_state['role'] == 'student'):
    st.header('Posted Programs')
    response = requests.get('http://api:4000/posts/posts').json()
    df = st.dataframe(response, column_order=["postId", "title", "body", "location", "programStart", "programEnd", "postAuthor", "professorId"], hide_index=True)
    
    @st.dialog("View Post")
    def view_post_dialog():
        st.write('View Post')
        post_id = st.number_input('Post ID', min_value=1, step=1, placeholder='Enter the post ID')
        submitted = st.button('Submit')

        if submitted:
            if post_id:
                # Log the data to the console
                logger.info(f'View Post submitted with data: {post_id}')
                
                # Send the data to the backend
                try:
                    response = requests.get(f'http://api:4000/posts/posts/{post_id}').json()
                    if response:
                        st.write(response)
                    else:
                        st.error("Error fetching post")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error with requests: {e}")
            else:
                st.error("Please fill in all the fields.")
else:
    st.header('All Harvard Programs')
    # Get the data from the backend (List all programs for Jennie)
    # Hardcoded example: schoolId=32 for Harvard University
    response = requests.get('http://api:4000/programs/programs/schools/32').json()

    df = st.dataframe(response, column_order=["programId", "title", "description", "approved", "schoolId", "professorId", "programStart", "programEnd", "location"], hide_index=True)

    harvard_school_id = 32

    @st.dialog("Add Program")
    def add_program_dialog():
        st.write('Add a new program')
        title = st.text_input('Title')
        description = st.text_input('Description')
        approved = st.checkbox('Approved?', value=False)
        school_id = st.number_input('School ID', value=harvard_school_id)
        professor_id = st.number_input('Professor ID', min_value=1, step=1)
        program_start = st.date_input('Program Start')
        program_end = st.date_input('Program End')
        location = st.text_input('Location')
        submitted = st.button('Submit')

        # Convert dates to string in 'YYYY-MM-DD' format
        program_start_str = program_start.strftime('%Y-%m-%d') if program_start else None
        program_end_str = program_end.strftime('%Y-%m-%d') if program_end else None
        
        approved = int(approved)
        program_data = {
            "title": title,
            "description": description,
            "approved": approved,
            "schoolId": school_id,
            "professorId": professor_id,
            "programStart": program_start_str,
            "programEnd": program_end_str,
            "location": location
        }

        if submitted:
            if not all(value != "" for value in program_data.values()):
                st.error("Please fill in all the fields.")
            else:
                # Log the data to the console
                logger.info(f'Add Program submitted with data: {program_data}')
                
                # Send the data to the backend
                try:
                    response = requests.post('http://api:4000/programs/programs', json=program_data)
                    if response.status_code == 200:
                        st.success("Program added successfully")
                    else:
                        st.error(f"Error adding program")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error with requests: {e}")


    # Dialog for editing a program at Harvard University
    @st.dialog("Edit Program")
    def edit_program_dialog():
        response = requests.get('http://api:4000/posts/posts').json()

        st.write('Edit an existing program')
        program_id = st.number_input('Program ID', min_value=1, step=1, placeholder='Enter the program ID')
        title = st.text_input('Title')
        description = st.text_input('Description')
        approved = st.checkbox('Approved?', value=False)
        school_id = st.number_input('School ID', value=1, step=1)
        professor_id = st.number_input('Professor ID', min_value=1, step=1)
        program_start = st.date_input('Program Start')
        program_end = st.date_input('Program End')
        location = st.text_input('Location')
        submitted = st.button('Submit')

        # Convert dates to string in 'YYYY-MM-DD' format
        program_start_str = program_start.strftime('%Y-%m-%d') if program_start else None
        program_end_str = program_end.strftime('%Y-%m-%d') if program_end else None

        approved = int(approved)
        
        program_data = {
            "programId": program_id,
            "title": title,
            "description": description,
            "approved": approved,
            "schoolId": school_id,
            "professorId": professor_id,
            "programStart": program_start_str,
            "programEnd": program_end_str,
            "location": location
        }

        if submitted:
            if program_id and not all(value != "" for value in program_data.values()):
                st.error("Please fill in all the fields.")
            else:
                # Log the data to the console
                logger.info(f'Edit Program submitted with data: {program_data}')
                
                # Send the data to the backend
                try:
                    response = requests.put(f'http://api:4000/programs/programs/{program_id}', json=program_data)
                    if response.status_code == 200:
                        st.success("Program updated successfully")
                    else:
                        st.error("Error editing program")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error with requests: {e}")

    @st.dialog("Delete Program")
    def delete_program_dialog():
      st.write('Delete a Program')
      program_id = st.number_input('Program ID', min_value=1, step=1, placeholder='Enter the program ID')
      submitted = st.button('Submit')

      if submitted:
        # Log the data to the console
        logger.info(f'Delete Program submitted with data: {program_id}')
        
        # Send the data to the backend
        try:
          response = requests.delete(f'http://api:4000/programs/programs/schools/32/{program_id}')
          if (response.status_code == 200):
            st.success("Program deleted successfully")
          else:
            st.error("Error deleting user")
        except requests.exceptions.RequestException as e:
          st.error(f"Error with requests: {e}")
          
    # Buttons to trigger actions
    if st.button('Add Program'):
        add_program_dialog()

    if st.button('Edit Program'):
        edit_program_dialog()

    if st.button('Delete Program'):
        delete_program_dialog()

    if st.button('Refresh'):
        st.rerun()
