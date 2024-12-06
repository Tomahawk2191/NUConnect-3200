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

