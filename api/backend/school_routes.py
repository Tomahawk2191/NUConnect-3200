from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

school = Blueprint('school', __name__)

#------------------------------------------------------------
# Return a list of all schools
@school.route('/school', methods=['GET'])
def get_schools():
    query = f'''
        SELECT *
        FROM school
    '''
    
    current_app.logger.info(f'GET /school query = {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# School routes - return details about a specific school
#------------------------------------------------------------
# Return a school's profile by their ID
@school.route('/school/profile/<schoolId>', methods=['GET', 'PUT', 'DELETE'])
def get_school(schoolId):
  if request.method == 'GET':
    query = f'''
        SELECT *
        FROM school
        WHERE schoolId = {str(schoolId)}
    '''
    
    current_app.logger.info(f'GET /school/profile/{schoolId} query = {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
  elif request.method == 'PUT':
    theData = request.json
    current_app.logger.info(theData)
    
    name = theData['name']
    bio = theData['bio']
    
    query = f'''
        UPDATE school
        SET name = '{name}', bio = '{bio}'
        WHERE schoolId = {str(schoolId)}
    '''
    
    current_app.logger.info(f'Updated school {schoolId} PUT /school/profile/{schoolId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
  elif request.method == 'DELETE':
    query = f'''
        DELETE FROM school
        WHERE schoolId = {str(schoolId)}
    '''
    
    current_app.logger.info(f'Deleted school {schoolId} DELETE /school/profile/{schoolId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
  