from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

user_tags = Blueprint('user_tags', __name__)

#------------------------------------------------------------
# Return a list of all user_tags
@user_tags.route('/user_tags', methods=['GET'])
def get_user_tags():
    query = f'''
        SELECT *
        FROM userTagParent
    '''
    
    current_app.logger.info(f'GET /user_tags query = {query}')
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# User_tag routes - return details about a specific user_tag
#------------------------------------------------------------
# Return a user_tag by their ID
@user_tags.route('/user_tags/<int:userTagId>', methods=['GET', 'PUT', 'DELETE'])
def get_user_tag(userTagId):
    if request.method == 'GET': # Get a user_tag
        query = f'''
            SELECT *
            FROM userTagParent
            WHERE userTagId = {userTagId}
        '''
        
        # Log the query
        current_app.logger.info(f'GET /user_tags/{userTagId} query = {query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    elif request.method == 'PUT': # Update a user_tag
        theData = request.json
        current_app.logger.info(theData)
        
        tagName = theData['tagName']
        category = theData['category'] 
    
        query = f'''
            UPDATE userTagParent`
            SET tagName = '{tagName}', category = '{category}'
            WHERE userTagId = {userTagId}
        '''
        
        current_app.logger.info(f'Updated user_tag {userTagId} PUT /user_tags/{userTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        
        response = make_response(f'User_tag {userTagId} updated')
        response.status_code = 200
        return response
    elif request.method == 'DELETE': # Delete a user
        query = f'''
        DELETE
        FROM userTagParent
        WHERE userTagId = {userTagId}
        '''
    
        current_app.logger.info(f'Deleted user_tag {userTagId} DELETE /user_tags/{userTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(f'user_tag {userTagId} deleted')
        response.status_code = 200
        return response