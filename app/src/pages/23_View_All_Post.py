import logging
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout = 'wide')

SideBarLinks(show_home=True)

# Add Northeastern logo
add_logo("assets/logo.png", height=400)

# Set up the page
st.markdown("# Posts")
st.sidebar.header("View Posts")
st.write('View Posts')

# Get the data from the backend


if st.session_state['role'] == 'student':
  

  response = requests.get(f'http://api:4000/posts/posts').json()

  df = st.dataframe(response, column_order=["postId", "postAuthor", "title", "body", "userId", "programId", "published", "favorited", "createdAt", "lastEdited"], hide_index=True)

  @st.dialog("Filter Posts")
  def filter_posts():
    st.write('Filter Posts')
    userId = st.text_input('Author Id')
    submitted = st.button("Submit")

    if submitted:
      response = requests.get(f'http://api:4000/posts/posts/{userId}').json()
      df = st.dataframe(response, column_order=["postId", "postAuthor", "title", "body", "userId", "programId", "published", "favorited", "createdAt", "lastEdited"], hide_index=True)

  if (st.button('Filter Posts')):
      filter_posts()
  if (st.button('Refresh')):
      st.rerun()

else:

  response = requests.get(f'http://api:4000/posts/posts').json()

  df = st.dataframe(response, column_order=["postId", "postAuthor", "title", "body", "userId", "programId", "published", "favorited", "createdAt", "lastEdited"], hide_index=True)



  @st.dialog("Add Post")
  def add_user_dialog():
      st.write('Add a new Post'),
      author = st.text_input('Post Author'),
      title = st.text_input('Post Title'),
      body = st.text_input('Body'),
      user_id = st.number_input('User Id', min_value=1, step=1),
      program = st.number_input('Program Id', min_value=1, step=1),
      submitted = st.button("Submit")

      posts_data = {
          "postAuthor": author,
          "title": title,
          "body": body,
          "userId": user_id,
          "programID": program,
      }
      
      if submitted:
        # Log the data to the console
        logger.info(f'Add Post submitted with data: {posts_data}')
        
        # Send the data to the backend
        try:
          response = requests.post('http://api:4000/posts/posts', json=posts_data)
          if (response.status_code == 200):
            st.success("New Post Created")
          else:
            st.error(f"Error Creating Post {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
          st.error(f"Error with requests: {e}")

  @st.dialog("Delete Post")
  def delete_user_dialog():
      st.write('Delete a Post')
      post_id = st.number_input('postId', min_value=1, step=1, placeholder='Enter the Post ID')
      submitted = st.button('Submit')

      if submitted:
        # Log the data to the console
        logger.info(f'Delete Post submitted with data: {post_id}')
        
        # Send the data to the backend
        try:
          response = requests.delete(f'http://api:4000/posts/posts/{post_id}')
          if (response.status_code == 200):
            st.success("Post deleted successfully")
          else:
            st.error(f"Error deleting Post")
        except requests.exceptions.RequestException as e:
          st.error(f"Error with requests: {e}")
          
  if (st.button('Add Post')):
    add_user_dialog()
  if (st.button('Delete Post')):    
    delete_user_dialog()
  if (st.button('Refresh')):
    st.rerun()
