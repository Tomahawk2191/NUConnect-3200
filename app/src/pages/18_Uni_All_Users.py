import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks(show_home=True)

def fetch_users():
    try:
        if (st.session_state['role'] == 'administrator'):
            response = requests.get('http://api:4000/users/users').json()
            logger.info(f'Fetched users: {response}')
            return response
        else:
            # Hardcoded example: schoolId=32 for Harvard University
            response = requests.get('http://api:4000/users/users/school/32').json()
            logger.info(f'Fetched users: {response}')
            return response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching users: {e}")
        return []

# fetch users and store in a variable (Global variable)
users = fetch_users()

if (st.session_state['role'] == 'administrator' or st.session_state['role'] == 'outside_administrator'):
    st.write('### Manage all Users')
else:
    st.write('### View all Users')
if users:
    st.dataframe(users, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)

if (st.session_state['role'] == 'administrator'):
    @st.dialog("Edit User")
    def edit_user_dialog():
        global users
        if not users:
            st.write("No users available to edit.")
            return
        
        st.write('Which user would you like to edit?')
        userId_to_edit = st.number_input('User ID to Edit', min_value=1, max_value=len(users), step=1)

        user_data = next((user for user in users if user["userId"] == userId_to_edit), None)

        if user_data:
            st.write('You are editing user:', userId_to_edit)
            first_name = st.text_input('First Name', value=user_data["firstName"])
            middle_name = st.text_input('Middle Name', value=user_data["middleName"] if user_data["middleName"] else "")
            last_name = st.text_input('Last Name', value=user_data["lastName"])
            phone = st.text_input('Phone Number', value=user_data["phone"])
            email = st.text_input('Email', value=user_data["email"])
            school_id = st.number_input('School ID', value=user_data["schoolId"], min_value=1, step=1)
            role_id = st.number_input('Role ID', value=user_data["roleId"], min_value=1, step=1)
            submitted = st.button('Submit')

            if submitted:
                updated_user_data = {
                    "firstName": first_name,
                    "middleName": middle_name if middle_name else None,
                    "lastName": last_name,
                    "phone": phone,
                    "email": email,
                    "schoolId": school_id,
                    "roleId": role_id
                }

                logger.info(f'Edited User Data: {updated_user_data}')
                try:
                    response = requests.put(f'http://api:4000/users/users/{userId_to_edit}', json=updated_user_data)
                    if response.status_code == 200:
                        st.success("User edited successfully")
                        users = fetch_users() 
                        st.dataframe(users, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)
                    else:
                        st.error(f"Error editing user: {response.status_code} - {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error with request: {e}")
        else:
            st.write("User not found.")

    @st.dialog("Delete User")
    def delete_user_dialog():
        st.write('Delete a user')
        user_id = st.number_input('User ID', min_value=1, step=1, placeholder='Enter the user ID')
        submitted = st.button('Submit')

        if submitted:
            logger.info(f'Delete User submitted with data: {user_id}')
            try:
                response = requests.delete(f'http://api:4000/users/users/{user_id}')
                if response.status_code == 200:
                    st.success("User deleted successfully")
                else:
                    st.error("Error deleting user")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with requests: {e}")

    if st.button('Add User'):
        add_user_dialog()

    if st.button('Edit User'):
        edit_user_dialog()

    if st.button('Delete User'):
        delete_user_dialog()

    if st.button('Refresh'):
        st.rerun()
if (st.session_state['role'] == 'outside_administrator'):
    @st.dialog("Edit User")
    def edit_user_dialog():
        st.write('Which user would you like to edit?')
        userId = st.number_input('User ID to Edit', min_value=1, step=1)
        first_name = st.text_input('First Name')
        middle_name = st.text_input('Middle Name')
        last_name = st.text_input('Last Name')
        phone = st.text_input('Phone Number')
        email = st.text_input('Email')
        school_id = 32
        role_id = st.number_input('Role ID', min_value=1, step=1)
        submitted = st.button('Submit')

        if submitted:
            updated_user_data = {
                "firstName": first_name,
                "middleName": middle_name if middle_name else None,
                "lastName": last_name,
                "phone": phone,
                "email": email,
                "schoolId": school_id,
                "roleId": role_id
            }

            logger.info(f'Edited User Data: {updated_user_data}')
            try:
                response = requests.put(f'http://api:4000/users/users/{userId}', json=updated_user_data)
                if response.status_code == 200:
                    st.success("User edited successfully")
                    users = fetch_users() 
                    st.dataframe(users, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)
                else:
                    st.error(f"Error editing user: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with request: {e}")
        else:
            st.write("User not found.")
    
    @st.dialog("Add User")
    def add_user_dialog():
        st.write('Add a new user')
        first_name = st.text_input('First Name')
        middle_name = st.text_input('Middle Name')
        last_name = st.text_input('Last Name')
        phone = st.text_input('Phone Number')
        email = st.text_input('Email')
        role_Id = st.number_input('Role ID', min_value=1, step=1)
        submitted = st.button('Submit')

        user_data = {
            "firstName": first_name,
            "middleName": middle_name,
            "lastName": last_name,
            "phone": phone,
            "email": email,
            "schoolId": 32,
            "roleId": role_Id
        }

        if submitted:
            if (user_data["middleName"] == ""):
                user_data["middleName"] = None

            logger.info(f'Add User submitted with data: {user_data}')

            try:
                response = requests.post('http://api:4000/users/users', json=user_data)
                if response.status_code == 200:
                    st.success("User added successfully")
                    users = fetch_users()  
                    st.dataframe(users, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)
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
            logger.info(f'Delete User submitted with data: {user_id}')
            try:
                response = requests.delete(f'http://api:4000/users/users/{user_id}')
                if response.status_code == 200:
                    st.success("User deleted successfully")
                else:
                    st.error("Error deleting user")
            except requests.exceptions.RequestException as e:
                st.error(f"Error with requests: {e}")