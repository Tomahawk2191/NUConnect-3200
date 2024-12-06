from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

school = Blueprint('school', __name__)

#------------------------------------------------------------
# School routes
#------------------------------------------------------------
# Return a list of all schools
@school.route('/school', methods=['GET'])
def get_schools():
  if request.method == 'GET':
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

  elif request.method == 'POST': #Enters a new school into the database
        theData = request.json
        current_app.logger.info(theData)
    
        schoolName = theData['name']
        bio = theData['bio'] 
    
        query = f'''
            INSERT INTO role (name, bio)
            VALUES ('{schoolName}, {bio})
        '''
    
        current_app.logger.info(f'Added new school {schoolName} POST /school query = {query}')
    
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
    
        response = make_response('Added new school')
        response.status_code = 200
        return response

#------------------------------------------------------------
# Return a school's profile by their ID
@school.route('/school/<int:schoolId>', methods=['GET', 'PUT', 'DELETE'])
def get_school(schoolId):
  if request.method == 'GET':
    query = f'''
        SELECT *
        FROM school
        WHERE schoolId = {schoolId}
    '''
    
    current_app.logger.info(f'GET /school/{schoolId} query = {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

  elif request.method == 'PUT': #Update a school's info
    theData = request.json
    current_app.logger.info(theData)
    
    name = theData['name']
    bio = theData['bio']
    
    query = f'''
        UPDATE school
        SET name = '{name}', bio = '{bio}'
        WHERE schoolId = {schoolId}
    '''
    
    current_app.logger.info(f'Updated school {schoolId} PUT /school/profile/{schoolId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'School {schoolId} updated')
    response.status_code = 200
    return response

  elif request.method == 'DELETE': #Delete a school
    query = f'''
        DELETE FROM school
        WHERE schoolId = {schoolId}
    '''
    
    current_app.logger.info(f'Deleted school {schoolId} DELETE /school/profile/{schoolId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'School {schoolId} deleted')
    response.status_code = 200
    return response
  