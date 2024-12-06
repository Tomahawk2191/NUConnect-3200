import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.write('### View All Post Tags')

# Get the data from the backend
response = requests.get('http://api:4000/post_tags/post_tags').json()

df = st.dataframe(response, column_order=["postTagId", "tagName", "category"], hide_index=True)

# st.dataframe(response, column_order=["userId", "firstName", "middleName", "lastName", "email", "roleId", "schoolId"], hide_index=True)  
  
@st.dialog("Create New Post Tag")
def add_post_tag_dialog():
    st.write('Create a post tag')
    tag_name = st.text_input('Tag Name')
    category = st.text_input('Category')
    submitted = st.button('Submit')

    post_tag_data = {
        "tagName": tag_name,
        "category": category
    }
    
    if submitted:
      # If the middle name is empty, set it to None
      if (post_tag_data["category"] == ""):
        post_tag_data["category"] = None
        
        # Log the data to the console
        logger.info(f'Add Post Tag submitted with data: {post_tag_data}')
      
      # Send the data to the backend
      try:
        response = requests.post('http://api:4000/post_tags/post_tags', json=post_tag_data)
        if (response.status_code == 200):
          st.success("Post tag created")
        else:
          st.error("Error created post tag")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")

@st.dialog("Delete Post Tag")
def delete_post_tag_dialog():
    st.write('Delete a post tag')
    post_tag_id = st.number_input('Post Tag ID', min_value=1, step=1, placeholder='Enter the post tag ID')
    submitted = st.button('Submit')

    if submitted:
      # Log the data to the console
      logger.info(f'Delete Post Tag submitted with data: {post_tag_id}')
      
      # Send the data to the backend
      try:
        response = requests.delete(f'http://api:4000/post_tags/post_tags/{post_tag_id}')
        if (response.status_code == 200):
          st.success("Post tag deleted successfully")
        else:
          st.error("Error deleting post tag")
      except requests.exceptions.RequestException as e:
        st.error(f"Error with requests: {e}")
        
if (st.button('Add Post Tag')):
  add_post_tag_dialog()
if (st.button('Delete Post Tag')):
  delete_post_tag_dialog()
if (st.button('Refresh')):
  st.rerun()