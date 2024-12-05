from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

user = Blueprint('user', __name__)

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
  elif request.method == 'POST':
    theData = request.json
    current_app.logger.info(theData)
    
    firstName = theData['firstName']
    middleName = theData['middleName']
    lastName = theData['lastName']
    phone = theData['phone']
    email = theData['email']
    roleID = theData['roleID']
    
    query = f'''
        INSERT INTO user (firstName, lastName, email, phone, roleID)
        VALUES ('{firstName}', '{middleName}', '{lastName}', '{phone}', '{email}', '{roleID}')
    '''
    
    current_app.logger.info(f'Added new user {firstName} {middleName} {lastName} POST /users query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
  
#------------------------------------------------------------
# Profile routes - return details about a specific user
#------------------------------------------------------------
# Return a user's profile by their ID
@user.route('/users/<int:userID>', methods=['GET', 'PUT', 'DELETE'])
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
  elif request.method == 'PUT': # Update a user's profile
    theData = request.json
    current_app.logger.info(theData)
    
    firstName = theData['firstName']
    middleName = theData['middleName']
    lastName = theData['lastName']
    phone = theData['phone']
    email = theData['email']
    
    #TODO: can update roleID?
    # roleId = theData['roleID']
    
    query = f'''
        UPDATE user
        SET firstName = '{firstName}', middleName = '{middleName}', lastName = '{lastName}', phone = '{phone}', email = '{email}'
        WHERE userId = {userId}
    '''
    
    current_app.logger.info(f'Updated user {userId} PUT /users/{userId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
  elif request.method == 'DELETE': # Delete a user
    query = f'''
      DELETE
      FROM user
      WHERE userId = {userId}
    '''
  
    current_app.logger.info(f'Deleted user {userId} DELETE /users/{userId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
  return response