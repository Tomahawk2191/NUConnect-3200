from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

customers = Blueprint('customers', __name__)

#------------------------------------------------------------
# Creates new account in the "Student role"
@students.route('/accounts', methods=['POST'])
def create_account():
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    firstName = the_data['firstName']
    lastName = the_data['lastName']
    phone = the_data['phone']
    email = the_data['email']
    schoolID = the_data['schoolId']
    roleID = the_data['roleId'] #should be automatic?

    query = f'''
        INSERT INTO application (firstName, lastName, phone, email, schoolId, roleId)
        VALUES ('{firstName}', '{lastName}', '{phone}', '{email}', '{schoolID}', '{roleID}')
    '''

    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("New Account Created")
    response.status_code = 200
    return response

#------------------------------------------------------------
# 1.1
# Enrolls a student into a specific program using their userID
# and the program's programID
@students.route('/apply', methods=['POST'])
def apply_program():
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    userID = the_data['userId']
    programID = the_data['programId']

    query = f'''
        INSERT INTO application (userId, programId, applied, accepted, denied)
        VALUES ('{userID}', '{programID}', TRUE, FALSE, FALSE)
    '''

    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully Applied for Program")
    response.status_code = 200
    return response

#------------------------------------------------------------
# 1.2
# Rescinds/unerolls student's application from a program
@students.route('/applications', methods=['DELETE'])
def unenroll_program(userID, programID):
    query = f'''
        DELETE 
        FROM application
        WHERE userId = {str(userID)}' AND programId = {str(programID)};
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response("Program post successfully deleted")
    response.status_code = 200
    return response

#------------------------------------------------------------
# 1.3
# Filters program posts given a postTagID
@students.route('/programs', methods=['GET'])
def filter_program_posts(postTagId):
    query = f'''
        SELECT p.postAuthor, p.title, p.body, p.programId, p.userId
        FROM post AS p
            JOIN postTag AS pt ON p.postId = pt.postId
            JOIN postTagParent pTP ON pt.postTagId = pTP.postTagId
        WHERE pt.postTagId = {str(postTagId)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# 1.4
# View all submitted applications for a given user (using userID)
@students.route('/applications/<userID>', methods=['GET'])
def filter_program_posts(userID):
    query = f'''
        SELECT a.userId, p.programId, p.title, p.location, a.applied, a.accepted, a.denied
        FROM application AS a
            JOIN program AS p ON a.programId = p.programId
        WHERE a.userId = {str(userID)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# 1.5
# View the program information for a specific program, including 
# its details as well as the current number of (accepted) applicants
@students.route('/programs/<programID>', methods=['GET'])
def view_specific_program(programID):
    
    query = f'''
        SELECT p.programId, p.title, p.location, schoolId, professorId, p.programStart, p.programEnd, COUNT(a.accepted) AS totalApplications
        FROM program p
            JOIN application a on p.programId = a.programId
        GROUP BY p.programId;
        WHERE p.programId = {str(programID)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# 1.6
# Edits/updates student's profile information

# UPDATE userTag
# SET userTagId = (SELECT userTagId FROM userTagParent WHERE tagName = 'Computer Science')
# WHERE userId = 5

