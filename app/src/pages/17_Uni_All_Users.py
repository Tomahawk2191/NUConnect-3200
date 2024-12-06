import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write('### Manage all Uni Users')

# Get the data from the backend
response = requests.get('http://api:4000/users/users').json()

df = st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)

# st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)  
  
@st.dialog("Add User")
def add_user_dialog():
    st.write('Add a new user')
    first_name = st.text_input('First Name')
    middle_name = st.text_input('Middle Name')
    last_name = st.text_input('Last Name')
    phone = st.text_input('Phone Number')
    email = st.text_input('Email')
    school_Id = st.number_input('School ID')
    role_Id = st.number_input('Role ID')
    submitted = st.button('Submit')

    user_data = {
        "firstName": first_name,
        "middleName": middle_name,
        "lastName": last_name,
        "phone": phone,
        "email": email,
        "schoolId": school_Id,
        "roleId": role_Id
    }
    
    
    if submitted:
      # If the middle name is empty, set it to None
      if (user_data["middleName"] == ""):
        user_data["middleName"] = None
        
      # Log the data to the console
      logger.info(f'Add User submitted with data: {user_data}')
      
      # Send the data to the backend
      try:
        response = requests.post('http://api:4000/users/users', json=user_data)
        if (response.status_code == 200):
          st.success("User added successfully")
          
          # Refresh the dataframe
          response = requests.get('http://api:4000/users/users').json()
          df = st.dataframe(response.json(), column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)
        else:
          st.error("Error adding user")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")

@st.dialog("Delete User")
def delete_user_dialog():
    st.write('Delete a user')
    user_id = st.number_input('User ID', min_value=1, step=1, placeholder='Enter the user ID')
    submitted = st.button('Submit')

    if submitted:
      # Log the data to the console
      logger.info(f'Delete User submitted with data: {user_id}')
      
      # Send the data to the backend
      try:
        response = requests.delete(f'http://api:4000/users/users/{user_id}')
        if (response.status_code == 200):
          st.success("User deleted successfully")
          
          # Refresh the dataframe
          response = requests.get('http://api:4000/users/users').json()
          df = st.dataframe(response.json(), column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)
        else:
          st.error("Error deleting user")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")



if (st.button('Add User')):
  add_user_dialog()
if (st.button('Delete User')):
  delete_user_dialog()
if (st.button('Refresh')):
  st.rerun()