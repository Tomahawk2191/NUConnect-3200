import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo

import pydeck as pdk
from urllib.error import URLError
from modules.nav import SideBarLinks
import requests


SideBarLinks(show_home=True)

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Profile")
st.sidebar.header("Profile")
st.write('View Profile')


userId = 5

if st.session_state['role'] == 'professor':
  userId = 101
  
response = requests.get(f'http://api:4000/users/users/{userId}').json()
logger.info(f'data {response}')

schoolId = response[0]["schoolId"]
roleId = response[0]["roleId"]

df = st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)

@st.dialog("Edit Profile")
def add_user_dialog():
    st.write('Edit Profile')
    first_name = st.text_input('First Name', value="")
    middle_name = st.text_input('Middle Name', value="")
    last_name = st.text_input('Last Name', value="")
    phone = st.text_input('Phone Number', value="")
    email = st.text_input('Email', value="")
    submitted = st.button('Submit')

    if submitted:
        if not first_name.strip():
            st.error("First Name is required.")
            return
        if not last_name.strip():
            st.error("Last Name is required.")
            return

        user_data = {
            "firstName": first_name.strip(),
            "middleName": middle_name.strip() if middle_name.strip() else None,
            "lastName": last_name.strip(),
            "phone": phone.strip(),
            "email": email.strip(),
            "schoolId": schoolId,
            "roleId": roleId
        }

        logger.info(f'Profile edited {user_data}')

        try:
            response = requests.put(f'http://api:4000/users/users/{userId}', json=user_data)
            if response.status_code == 200:
                st.success("User edited successfully")
                updated_response = requests.get(f'http://api:4000/users/users/{userId}').json()
                st.dataframe(updated_response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)
            else:
                st.error(f"Error editing user: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error with requests: {e}")

        
if (st.button('Edit Profile')):
  add_user_dialog()
if (st.button('Refresh')):
  st.rerun()

st.write('')
st.write('')
st.write('')
st.write('View All Tags')

response = requests.get(f'http://api:4000/users/users/{userId}/user_tags').json()
logger.info(f'data {response}')

if response and isinstance(response, list) and response[0] and "userTagId" in response[0]:
  userTagId = response[0]["userTagId"]

df = st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)

@st.dialog("Delete tag")
def delete_user_tag():
  st.write("Delete tag")
  userTagId = st.number_input('userTagId', min_value=1, max_value=65, step=1)
  submitted = st.button('Submit')

  tag_data = {
    "userTagId": userTagId
  }

  if submitted:
    logger.info(f'{tag_data}')
    try:
      response = requests.delete(f'http://api:4000/users/users/{userId}/user_tags', json=tag_data)
      if (response.status_code == 200):
        st.success("Tag deleted")
      else:
          st.error("Error deleting Tag")
    except requests.exceptions.RequestException as e:
          st.error(f"Error with requests: {e}")
  
@st.dialog("Add tag")
def add_user_tag():
  st.write("Add tag")
  userTagId = st.number_input('userTagId', min_value=1, max_value=65, step=1)
  response = requests.get(f'http://api:4000/user_tags/user_tags/{userTagId}').json()
  dataframe = st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)

  
  submitted = st.button('Submit')

  tag_data = {
    "userTagId": userTagId
  }
  
  if submitted:
    logger.info(f'{tag_data}')
    try:
      response = requests.post(f'http://api:4000/users/users/{userId}/user_tags', json=tag_data)
      if (response.status_code == 200):
        st.success("Tag added")
      else:
        st.error("Error adding Tag")
    except requests.exceptions.RequestException as e:
      st.error(f"Error with requests: {e}")

if (st.button('Add tag')):
        add_user_tag()

if (st.button('Delete tag')):
        delete_user_tag()

if (st.button('Refresh tag')):
        st.rerun()
  