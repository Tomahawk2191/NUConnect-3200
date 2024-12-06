from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

user_tags = Blueprint('user_tags', __name__)

#------------------------------------------------------------
# User tag routes
#------------------------------------------------------------
# Return a list of all user tags
@user_tags.route('/user_tags', methods=['GET', 'POST'])
def get_user_tags():
    if (request.method == 'GET'):
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

    elif (request.method == 'POST'): #Creates a new user tag
        theData = request.json
        current_app.logger.info(theData)
        
        tagName = theData['tagName']
        category = theData['category']
        
        query = f'''
            INSERT INTO userTagParent (tagName, category)
            VALUES ('{tagName}', '{category}')
        '''
        
        current_app.logger.info(f'Added new user tag {tagName} POST /user_tags query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response('Added new user tag')
        response.status_code = 200
        return response

#------------------------------------------------------------
# Return a user tag by their ID
@user_tags.route('/user_tags/<int:userTagId>', methods=['GET', 'PUT', 'DELETE'])
def get_user_tag(userTagId):
    if request.method == 'GET': # Get a user tag
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

    elif request.method == 'PUT': # Update a user tag
        theData = request.json
        current_app.logger.info(theData)
        
        tagName = theData['tagName']
        category = theData['category'] 
    
        query = f'''
            UPDATE userTagParent`
            SET tagName = '{tagName}', category = '{category}'
            WHERE userTagId = {userTagId}
        '''
        
        current_app.logger.info(f'Updated user tag {userTagId} PUT /user_tags/{userTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response(f'User tag {userTagId} updated')
        response.status_code = 200
        return response

    elif request.method == 'DELETE': # Delete a user tag
        query = f'''
        DELETE
        FROM userTagParent
        WHERE userTagId = {userTagId}
        '''
    
        current_app.logger.info(f'Deleted user tag {userTagId} DELETE /user_tags/{userTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(f'User tag {userTagId} deleted')
        response.status_code = 200
        return response