import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

SideBarLinks()

# Add Northeastern logo
add_logo("assets/logo.png", height=400)

# Set up the page
st.markdown("# User Tags")
st.sidebar.header("View User Tags")
st.write('View User Tags')

# Fetches user tag data from the API
def fetch_user_tags():
  try:
      response = requests.get('http://api:4000/user_tags/user_tags').json()
      logger.info(f'data {response}')
      return response
  except requests.exceptions.RequestException as e:
      st.error(f"Error fetching user tags: {e}")
      return []

response = fetch_user_tags()

# Ensure there's data to display
if response:
  st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)
else:
  st.write("No user tags available to display.")

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
    # If the category is empty, set it to None
    if (user_tag_data["category"] == ""):
      user_tag_data["category"] = None
      logger.info(f'User tag data submitted: {user_tag_data}')
    
    # Send the data to the backend
    try:
      response = requests.post('http://api:4000/user_tags/user_tags', json=user_tag_data)
      if (response.status_code == 200):
        st.success("User tag created")
        response = fetch_user_tags()  
        st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)
      else:
        st.error("Error creating user tag")
    except requests.exceptions.RequestException as e:
      st.error(f"Error with requests: {e}")

@st.dialog("Edit User Tag")
def edit_user_tag_dialog():
  response = fetch_user_tags()

  st.write('Which user tag would you lke to edit?')
  userTagId_to_edit = st.number_input('User Tag ID to Edit', min_value=1, max_value=len(response), step=1)

  user_tag_data = next((user_tag for user_tag in response if user_tag["userTagId"] == userTagId_to_edit), None)

  if user_tag_data:
    st.write('You are editing program:', userTagId_to_edit)
    tag_name = st.text_input('Tag Name', value=user_tag_data["tagName"])
    category = st.text_input('Category', value=user_tag_data["category"])
    submitted = st.button('Submit')

    if submitted:
      updated_user_tag_data = {
        "tagName": tag_name,
        "category": category
      }

      logger.info(f'Edited Program Data: {updated_user_tag_data}')
      
      try:
        response = requests.put(f'http://api:4000/user_tags/user_tags/{userTagId_to_edit}', json=user_tag_data)
        if response.status_code == 200:
          st.success("User tag updated successfully")
          response = fetch_user_tags()  
          st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)
        else:
          st.error(f"Error editing user tag")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")

@st.dialog("Delete User Tag")
def delete_user_tag_dialog():
  st.write('Delete a user tag')
  user_tag_id = st.number_input('User Tag ID', min_value=1, step=1, placeholder='Enter the user tag ID')
  submitted = st.button('Submit')

  if submitted:
    # Log the data to the console
    logger.info(f'Delete User Tag submitted with ID: {user_tag_id}')
    
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

if st.button('Edit User Tag'):
  edit_user_tag_dialog()

if (st.button('Delete User Tag')):
  delete_user_tag_dialog()

if (st.button('Refresh')):
  st.rerun()