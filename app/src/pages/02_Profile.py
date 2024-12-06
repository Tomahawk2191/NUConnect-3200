import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo

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

response = requests.get('http://api:4000/users/users/5').json()
logger.info(f'data {response}')

schoolId = response[0]["schoolId"]
roleId = response[0]["roleId"]

df = st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)

@st.dialog("Edit Profile")
def add_user_dialog():
    st.write('Edit Profile')
    first_name = st.text_input('First Name')
    middle_name = st.text_input('Middle Name')
    last_name = st.text_input('Last Name')
    phone = st.text_input('Phone Number')
    email = st.text_input('Email')
    submitted = st.button('Submit')

    user_data = {
        "firstName": first_name,
        "middleName": middle_name,
        "lastName": last_name,
        "phone": phone,
        "email": email,
        "schoolId": schoolId,
        "roleId": roleId
       
    }
    
    if submitted:
    
      if (user_data["middleName"] == ""):
        user_data["middleName"] = None
        
      logger.info(f'Profile edited {user_data}')
      
      try:
        response = requests.put('http://api:4000/users/users/5', json=user_data)
        if (response.status_code == 200):
          st.success("User edited")
          
          
          response = requests.get('http://api:4000/users/users/5').json()
          df = st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)
        else:
          st.error("Error editing user")
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

response = requests.get('http://api:4000/users/users/2/user_tags').json()
logger.info(f'data {response}')



if response and isinstance(response, list) and response[0] and "userTagId" in response[0]:
 userTagId = response[0]["userTagId"]

df = st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)

@st.dialog("Edit tag")
def edit_user_tag():
  st.write('Edit Tag')
  tagName = st.text_input('tag name')
  category = st.text_input('category')
  submitted = st.button('Submit')
  
  tag_data = {

    "userTagId": userTagId,
    "tagName": tagName,
    "category": category
  }

  if submitted:

    logger.info(f'{tag_data}')


    try:
      response = requests.put('http://api:4000/user_tags/user_tags/2', json=tag_data)
      if (response.status_code == 200):
        st.success("Tag edited")
        response = requests.get('http://api:4000/user_tags/user_tags/2').json()
        df = st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)
      else:
          st.error("Error editing Tag")
    except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")

@st.dialog("Delete tag")
def delete_user_tag():
   st.write("Delete tag")
   tagName = st.text_input('tag name')
   category = st.text_input('category')
   submitted = st.button('Submit')

   tag_data = {

    "userTagId": userTagId,
    "tagName": tagName,
    "category": category
  }
  
  
   if submitted:

        logger.info(f'{tag_data}')
   try:
      response = requests.delete('http://api:4000/user_tags/user_tags/2', json=tag_data)
      if (response.status_code == 200):
        st.success("Tag deleted")
        response = requests.get('http://api:4000/user_tags/user_tags/2').json()
        df = st.dataframe(response, column_order=["userTagId", "tagName", "category"], hide_index=True)
      else:
          st.error("Error deleting Tag")
   except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")
   
  
@st.dialog("Add tag")
def delete_user_tag():
   pass


if (st.button('Edit tag')):
        edit_user_tag()





if (st.button('Delete tag')):
        delete_user_tag()

if (st.button('Refresh tag')):
        st.rerun()
  