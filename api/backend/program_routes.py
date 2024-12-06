from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

programs = Blueprint('programs', __name__)

#------------------------------------------------------------
# Program routes - return details about a specific program
#------------------------------------------------------------
# Return a list of all programs
@programs.route('/programs', methods=['GET', 'POST'])
def get_programs():
  if request.method == 'GET':
    query = f'''
        SELECT *
        FROM program
    '''
    
    current_app.logger.info(f'GET /programs query = {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

  elif request.method == 'POST': # Creates a new program
    theData = request.json
    current_app.logger.info(theData)
    
    title = theData['title']
    description = theData['description']
    location = theData['location']
    approved = theData['approved']
    #awaiting = theData['awaiting']
    schoolId = theData['schoolId']
    professorId = theData['professorId']
    programStart = theData['programStart']
    programEnd = theData['programEnd']
    
    #TODO: should awaiting default to false? If so, remove from query
    query = f'''
      INSERT INTO program (title, description, location, approved,  schoolId, professorId, programStart, programEnd)
      VALUES ('{title}', '{description}', '{location}', '{approved}', '{schoolId}', '{professorId}', '{programStart}', '{programEnd}')
    '''
    
    current_app.logger.info(f'Added new program {title} POST /programs query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response('Added new program')
    response.status_code = 200
    return response
  

#------------------------------------------------------------



  
#------------------------------------------------------------
# Return a program by their ID
@programs.route('/programs/<int:programId>', methods=['GET', 'PUT', 'DELETE'])
def get_program_users(programId):
  if request.method == 'GET':
    query = f'''
        SELECT *
        FROM program
        WHERE programId = {programId}
    '''
    
    current_app.logger.info(f'GET /programs/{programId} query = {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

  elif request.method == 'PUT': # Update a program
    theData = request.json
    current_app.logger.info(theData)
    
    title = theData['title']
    description = theData['description']
    location = theData['location']
    approved = theData['approved']
    schoolId = theData['schoolId']
    professorId = theData['professorId']
    
    #TODO: how to update programStart and programEnd? Maybe check in request if programStart and programEnd are valid dates?
    programStart = theData['programStart']
    programEnd = theData['programEnd']
  
    query = f'''
        UPDATE program
        SET title = '{title}', description = '{description}', location = '{location}', approved = '{approved}', schoolId = '{schoolId}', professorId = '{professorId}', programStart = '{programStart}', programEnd = '{programEnd}'
        WHERE programId = {programId}
    '''
    
    current_app.logger.info(f'Updated program {programId} PUT /programs/{programId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'Program {programId} updated')
    response.status_code = 200
    return response

  elif request.method == 'DELETE': # Delete a user
    query = f'''
      DELETE
      FROM program
      WHERE programId = {programId}
    '''
  
    current_app.logger.info(f'Deleted program {programId} DELETE /programs/{programId} query = {query}')
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(f'Program {programId} deleted')
    response.status_code = 200
    return response

#------------------------------------------------------------
# Return a list of users that have applied for a program
@programs.route('/programs/<int:programId>/users', methods=['GET'])
def get_program(programId):
  if request.method == 'GET':
    query = f'''
      SELECT p.programId, p.title, u.firstName, u.lastName, u.email
      FROM program p
      JOIN application a on p.programId = a.programId
      JOIN user u on a.userId = u.userId
      WHERE programId = {programId}
    '''
    
    current_app.logger.info(f'GET /programs/{programId}/users query = {query}')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response