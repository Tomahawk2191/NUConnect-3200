import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks(show_home=True)

st.write('### Manage all Roles')

# Get the data from the backend
response = requests.get('http://api:4000/roles/role').json()

df = st.dataframe(response, column_order=["roleId", "name", "canPost", "canApprove", "canAssignProf", "canApply", "canRetract", 
                                          "canEditOwn", "canEditAll", "canDelteOwn", "canDeleteAll", "canUpdateAccess"], hide_index=True)

# st.dataframe(response, column_order=["name", "canPost", "canApprove", "canAssignProf", "canApply", "canRetract", 
#                                          "canEditOwn", "canEditAll", "canDelteOwn", "canDeleteAll", "canUpdateAcess", "roleId"], hide_index=True)

@st.dialog("Add Role")
def add_user_dialog():
    st.write('Add a new role')
    name = st.text_input('Role Name')
    post = st.checkbox(label="Can Post?", value=False)
    approve = st.checkbox(label="Can Approve?", value=False)
    assign_prof = st.checkbox(label="Can Assign?", value=False)
    apply = st.checkbox(label="Can Apply?", value=False)
    retract = st.checkbox(label="Can Retract?", value=False)
    edit_own = st.checkbox(label="Can Edit Own?", value=False)
    edit_all = st.checkbox(label="Can Edit All?", value=False)
    delete_own = st.checkbox(label="Can Delete Own?", value=False)
    delete_all = st.checkbox(label="Can Delete All?", value=False)
    update_access = st.checkbox(label="Can Update Access?", value=False) 
    submitted = st.button('Submit')

    role_data = {
        "name": name,
        "canPost": post,
        "canApprove": approve,
        "canAssignProf": assign_prof,
        "canApply": apply,
        "canRetract": retract,
        "canEditOwn": edit_own,
        "canEditAll": edit_all,
        "canDeleteOwn": delete_own,
        "canDeleteAll": delete_all,
        "canUpdateAccess": update_access
    }
    
    if submitted:
      # Log the data to the console
      logger.info(f'Add Role submitted with data: {role_data}')
      
      # Send the data to the backend
      try:
        response = requests.post('http://api:4000/roles/role', json=role_data)
        if (response.status_code == 200):
          st.success("New Role Created")
        else:
          st.error(f"Error Creating Role {response.status_code} - {response.text}")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")

@st.dialog("Delete Role")
def delete_user_dialog():
    st.write('Delete a Role')
    role_id = st.number_input('roleId', min_value=1, step=1, placeholder='Enter the role ID')
    submitted = st.button('Submit')

    if submitted:
      # Log the data to the console
      logger.info(f'Delete Role submitted with data: {role_id}')
      
      # Send the data to the backend
      try:
        response = requests.delete(f'http://api:4000/roles/role/{role_id}')
        if (response.status_code == 200):
          st.success("Role deleted successfully")
        else:
          st.error(f"Error deleting role")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")
        
if (st.button('Add role')):
  add_user_dialog()
if (st.button('Delete role')):    
  delete_user_dialog()
if (st.button('Refresh')):
  st.rerun()