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
    roleId = theData['roleId']
    
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
    query = f'''
      DELETE
      FROM user
      WHERE userId = {userId}
    '''
  
    current_app.logger.info(f'Deleted user {userId} DELETE /users/{userId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'User {userId} deleted')
    response.status_code = 200
    return response
  
#Returns a list of all posts created by a user  
@user.route('/users/<int:userId>/posts', methods=['GET'])
def get_user_posts(userId):
    query = f'''
        SELECT *
        FROM post
        WHERE userId = {userId}
    '''
    current_app.logger.info(f'GET /{userId}/posts query = {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# return all tags for a given user
# TODO
# add to REST API matrix 
@user.route('/users/<int:userId>/user_tags', methods = ['GET', 'POST', 'DELETE'])
def get_user_tags(userId):
  if (request.method == 'GET'):
    current_app.logger.info(f'trying GET')
    query = f'''
        SELECT utp.category, utp.tagName, utp.userTagId
        FROM userTag AS ut 
        JOIN userTagParent AS utp
        ON ut.userTagId = utp.userTagId
        WHERE ut.userId = {userId}
        '''
    current_app.logger.info(f'GET /{userId}/user_tags query = {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
  elif (request.method == 'POST'):
    current_app.logger.info(f'trying POST')
    theData = request.json
    userTagId = theData['userTagId']

    query = f'''
        INSERT INTO userTag
        VALUES ('{userId}', '{userTagId}')
      '''

    current_app.logger.info('made change, added user tag for user')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
      
    response = make_response(f'tag made for {userId}')
    response.status_code = 200
    return response
  elif (request.method == 'DELETE'):
    current_app.logger.info(f'trying DELETE')
    theData = request.json
    userTagId = theData['userTagId']

    query = f'''
        DELETE
        FROM userTag
        WHERE userId = {userId} AND userTagId = {userTagId}
      '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'tag deleted for {userId}')
    response.status_code = 200
    return response


# return programs related to a user
# TODO add to REST API Matrix  
@user.route('/users/<int:userId>/programs', methods = ['GET', 'DELETE'])
def get_programs(userId):

  if request.method == 'GET':

    query = f'''
      SELECT p.title, p.description, p.location, p.professorId, a.applicationId
      FROM program p
      JOIN application a
      ON p.programId = a.programId
      WHERE a.userId = {userId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
  
  # unenroll in a program
  elif request.method == 'DELETE':
    theData = request.json
    current_app.logger.info(theData)
    applicationId = theData['applicationId']

    query = f'''
      DELETE
      FROM application
      WHERE applicationId = {applicationId} AND userId = {userId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'User {userId} deleted')
    response.status_code = 200
    return response


# TODO make route in REST API matrix
@user.route('/users/programs/<int:professorId>', methods = ['GET', 'PUT','DELETE'])
def get_professor_programs(professorId):

  if request.method == 'GET':

    query = f'''
    SELECT p.title, p.description, p.location, p.programId
    FROM program p
    WHERE p.professorId = {professorId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
  
  elif request.method == 'PUT':
    theDataOne = request.json
    current_app.logger.info(theDataOne)
    title = theDataOne['title']
    description = theDataOne['description']
    location = theDataOne['location']
    programId = theDataOne['programId']

    query = f'''
      UPDATE program 
      SET title = '{title}', description = '{description}', location = '{location}'
      WHERE professorId = {professorId} AND programId = {programId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'for {professorId} updated')
    response.status_code = 200
    return response


  
  elif request.method == 'DELETE':
    theDataTwo = request.json
    current_app.logger.info(theDataTwo)
    programId = theDataTwo['programId']


    query = f'''
      DELETE 
      FROM PROGRAM
      WHERE professorId = {professorId} AND programId = {programId}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'for {professorId} deleted')
    response.status_code = 200
    return response
  
# returns all applications for a user, route also allows for rescinding 
# TODO add to REST API matrix 
@user.route('/users/applications/<int:userId>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def filter_program_posts(userId):

  if request.method == 'GET':
    query = f'''
      SELECT a.userId, a.applicationId, p.title, p.location, a.applied, a.accepted, a.denied
      FROM application AS a
      JOIN program AS p 
      ON a.programId = p.programId
      WHERE a.userId = {userId};
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

  elif request.method == 'PUT':
    theData = request.json
    current_app.logger.info(theData)
    applicationId = theData['applicationId']
    applied = theData['applied']

    query = f'''
      UPDATE application
      SET applied = '{applied}'
      WHERE applicationId = '{applicationId}'
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'for {applicationId} updated')
    response.status_code = 200
    return response

  elif request.method == 'POST':
    theData = request.json
    current_app.logger.info(theData)
    programId = theData['programId']
    applied = 1
    
    extract = f'''
      INSERT INTO application (userId, programId, applied)
      VALUES ('{userId}', '{programId}', '{applied}')
    '''

    cursor = db.get_db().cursor()
    cursor.execute(extract)
    db.get_db().commit()
      
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    
  elif request.method == 'DELETE':
    theData = request.json
    current_app.logger.info(theData)
    applicationId = theData['applicationId']
    

    query = f'''
      DELETE
      FROM application
      WHERE applicationId = {applicationId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'for {applicationId} deleted')
    response.status_code = 200
    return response

# route to get all applicants for a particular professor
# TODO add to REST API matrix 
@user.route('/users/applications/students/<int:professorId>', methods = ['GET'])
def get_applicants(professorId):
  query = f'''
    SELECT u.userId, u.firstName, u.middleName, u.lastName, u.phone, u.email
    FROM user AS u 
    JOIN application AS a
    ON u.userId = a.userId
    JOIN program  AS p
    ON p.programId = a.programId
    WHERE p.professorId = {professorId}
  '''

  cursor = db.get_db().cursor()
  cursor.execute(query)
  theData = cursor.fetchall()
    
  response = make_response(jsonify(theData))
  response.status_code = 200
  return response