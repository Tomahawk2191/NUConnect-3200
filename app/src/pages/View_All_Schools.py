import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks(show_home=True)

st.markdown("# Schools")
st.sidebar.header("View All Schools")
st.write('View All Schools')

# Get the data from the backend
response = requests.get('http://api:4000/schools/school').json()

df = st.dataframe(response, column_order=["schoolId", "name", "bio"], hide_index=True)

# st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)  
  
@st.dialog("Add a new school")
def add_school_dialog():
    st.write('Add a new school')
    name = st.text_input('School Name')
    bio = st.text_input('School Bio')
    submitted = st.button('Submit')

    school_data = {
        "name": name,
        "bio": bio
    }
    
    if submitted:
      # If the bio is empty, set it to None
      if (school_data["bio"] == ""):
        school_data["bio"] = None
        
        # Log the data to the console
        logger.info(f'Add School submitted with data: {school_data}')
      
      # Send the data to the backend
      try:
        response = requests.post('http://api:4000/schools/school', json=school_data)
        if (response.status_code == 200):
          st.success("School added")
        else:
          st.error(f"Error adding school {response.status_code} - {response.text}")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")

@st.dialog("Delete School")
def delete_school_dialog():
    st.write('Delete a school')
    school_id = st.number_input('School ID', min_value=1, step=1, placeholder='Enter the user tag ID')
    submitted = st.button('Submit')

    if submitted:
      # Log the data to the console
      logger.info(f'Delete School submitted with data: {school_id}')
      
      # Send the data to the backend
      try:
        response = requests.delete(f'http://api:4000/schools/school/{school_id}')
        if (response.status_code == 200):
          st.success("School deleted successfully")
        elif (response.status_code == 500):
          st.error("School cannot be deleted, as there are still users on this platform that belong to this school")
        else:
          st.error(f"Error deleting school {response.status_code} - {response.text}")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")
        
if (st.button('Add School')):
  add_school_dialog()
if (st.button('Delete School')):
  delete_school_dialog()
if (st.button('Refresh')):
  st.rerun()