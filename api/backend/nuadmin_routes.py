from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

nuadmin = Blueprint('nuadmin', __name__)

#------------------------------------------------------------
# Creates new account in the "NU Admin role"
@nuadmin.route('/accounts', methods=['POST'])
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
# 3.1
# View all programs on the platform
@nuadmin.route('/programs', methods=['GET'])
def view_all_programs():
    query = f'''
        SELECT *
        FROM program
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# 3.2
# Deletes a program from the database
@nuadmin.route('/programs', methods=['DELETE'])
def delete_program(programID):
    query = f'''
        DELETE 
        FROM program
        WHERE userId = {str(programID)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response("Program successfully deleted")
    response.status_code = 200
    return response

# Deletes a program post from the database
@nuadmin.route('/posts', methods=['DELETE'])
def delete_program_posts(postID):
    query = f'''
        DELETE 
        FROM post
        WHERE userId = {str(postID)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response("Program post successfully deleted")
    response.status_code = 200
    return response

#------------------------------------------------------------
# 3.3
# View all users on the platform
@nuadmin.route('/users', methods=['GET'])
def view_all_users():
    query = f'''
        SELECT *
        FROM user
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# 3.4
# Update permissions for a specific role, given their roleID

# UPDATE role
# SET canAssignProf = TRUE
# WHERE roleId = (SELECT r.roleId
# FROM (SELECT roleId FROM role WHERE name = 'Professor') AS r)

#------------------------------------------------------------
# 3.5
# Deletes a user from the database
@nuadmin.route('/users', methods=['DELETE'])
def delete_user(userID):
    query = f'''
        DELETE 
        FROM user
        WHERE userId = {str(userID)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response("User successfully deleted")
    response.status_code = 200
    return response

#------------------------------------------------------------
# 3.6
# Edits/updates contents of an offered program

# UPDATE program
# SET description = 'Updated program details for new courses'
# WHERE programId = 2;


