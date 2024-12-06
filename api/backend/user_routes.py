from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
import pymysql

user = Blueprint('user', __name__)

#------------------------------------------------------------
# User routes
#------------------------------------------------------------
# Return a list of all users
@user.route('/users', methods=['GET', 'POST'])
def get_users():
  if request.method == 'GET':
    query = f'''
        SELECT *
        FROM user
    '''
    
    current_app.logger.info(f'GET /users query = {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

  elif request.method == 'POST': #Creates a new user
    theData = request.json
    current_app.logger.info(theData)
    
    firstName = theData['firstName']
    middleName = theData['middleName']
    lastName = theData['lastName']
    phone = theData['phone']
    email = theData['email']
    schoolId = theData['schoolId']
    roleId = theData['roleId']
    
    query = f'''
        INSERT INTO user (firstName, middleName, lastName, phone, email, schoolId, roleId)
        VALUES ('{str(firstName)}', '{str(middleName)}', '{str(lastName)}', '{str(phone)}', '{str(email)}', '{int(schoolId)}', '{int(roleId)}')
    '''
    
    current_app.logger.info(f'Added new user {firstName} {middleName} {lastName} POST /users query = {query}')
    
    try:
      cursor = db.get_db().cursor()
      cursor.execute(query)
      db.get_db().commit()

    except pymysql.Error as e:
      current_app.logger.error(f'Error adding new user: {e}')
      response = make_response('Error adding new user')
      response.status_code = 500
      return response
    
    response = make_response('Added new user')
    response.status_code = 200
    return response
  
#------------------------------------------------------------
# Return a user's profile by their ID
@user.route('/users/<int:userId>', methods=['GET', 'PUT', 'DELETE'])
def get_user(userId):
  if request.method == 'GET': # Get a user's profile
    query = f'''
        SELECT *
        FROM user
        WHERE userId = {userId}
    '''
    
    # Log the query
    current_app.logger.info(f'GET /users/{userId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

  elif request.method == 'PUT': # Update a user's profile
    theData = request.json
    current_app.logger.info(theData)
    
    firstName = theData['firstName']
    middleName = theData['middleName']
    lastName = theData['lastName']
    phone = theData['phone']
    email = theData['email']
    schoolId = theData['schoolId']
    roleId = theData['roleID']
    
    query = f'''
        UPDATE user
        SET firstName = '{firstName}', middleName = '{middleName}', lastName = '{lastName}', phone = '{phone}', email = '{email}', schoolId = '{schoolId}', roleId = '{roleId}'
        WHERE userId = {userId}
    '''
    
    current_app.logger.info(f'Updated user {userId} PUT /users/{userId} query = {query}')
    
    try:
      cursor = db.get_db().cursor()
      cursor.execute(query)
      db.get_db().commit()
    except pymysql.Error as e:
      current_app.logger.error(f'Error updating user {userId}: {e}')
      response = make_response(f'Error updating user {userId}')
      response.status_code = 500
      return response
    
    response = make_response(f'User {userId} updated')
    response.status_code = 200
    return response

  elif request.method == 'DELETE': # Delete a user
    # theData = request.json
    # current_app.logger.info(theData)
    # userId = theData['userId']
    
    query = f'''
      DELETE
      FROM user
      WHERE userId = {userId}
    '''
  
    current_app.logger.info(f'Deleted user {userId} DELETE /users/{userId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(f'User {userId} deleted')
    response.status_code = 200
    return response
  
#Returns a list of all posts created by a user  
@user.route('/users/<int:userID>/posts', methods=['GET'])
def get_user_posts(userId):
    query = f'''
        SELECT *
        FROM posts
        WHERE userId = {userId}
    '''
    current_app.logger.info(f'GET /users/{userId}/posts query = {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

