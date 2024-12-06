import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write('### View All User Tags')

# Get the data from the backend
response = requests.get('http://api:4000/user_tags/user_tags').json()

df = st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)

# st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)  
  
@st.dialog("Create New User Tag")
def add_user_tag_dialog():
    st.write('Create a user tag')
    tag_name = st.text_input('Tag Name')
    category = st.text_input('Category')
    submitted = st.button('Submit')

    user_tag_data = {
        "tagName": tag_name,
        "category": category
    }
    
    if submitted:
      # If the middle name is empty, set it to None
      if (user_tag_data["category"] == ""):
        user_tag_data["category"] = None
        
        # Log the data to the console
        logger.info(f'Add User Tag submitted with data: {user_tag_data}')
      
      # Send the data to the backend
      try:
        response = requests.post('http://api:4000/user_tags/user_tags', json=user_tag_data)
        if (response.status_code == 200):
          st.success("User tag created")
        else:
          st.error("Error created user tag")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")

@st.dialog("Delete User Tag")
def delete_user_tag_dialog():
    st.write('Delete a user tag')
    user_tag_id = st.number_input('User Tag ID', min_value=1, step=1, placeholder='Enter the user tag ID')
    submitted = st.button('Submit')

    if submitted:
      # Log the data to the console
      logger.info(f'Delete User Tag submitted with data: {user_tag_id}')
      
      # Send the data to the backend
      try:
        response = requests.delete(f'http://api:4000/user_tags/user_tags/{user_tag_id}')
        if (response.status_code == 200):
          st.success("User tag deleted successfully")
        else:
          st.error("Error deleting user tag")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")
        
if (st.button('Add User Tag')):
  add_user_tag_dialog()
if (st.button('Delete User Tag')):
  delete_user_tag_dialog()
if (st.button('Refresh')):
  st.rerun()