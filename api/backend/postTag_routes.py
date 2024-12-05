from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db


post_tags = Blueprint('post_tags', __name__)

# Return a list of all post tags
@post_tags.route('/user_tags', methods=['GET'])
def get_user_tags():
    query = f'''
        SELECT *
        FROM postTagParent
    '''
    
    current_app.logger.info(f'GET /post_tags query = {query}')
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
@post_tags.route('/post_tags/<int:userTagId>', methods=['GET', 'PUT', 'DELETE'])
def get_post_tag(postTagId):
    if request.method == 'GET': # Get a user_tag
        query = f'''
            SELECT *
            FROM postTagParent
            WHERE postTagId = {postTagId}
        '''
        
        # Log the query
        current_app.logger.info(f'GET /user_tags/{postTagId} query = {query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    elif request.method == 'PUT': # Update a post_tag
        theData = request.json
        current_app.logger.info(theData)
        
        tagName = theData['tagName']
        category = theData['category'] 
    
        query = f'''
            UPDATE postTagParent`
            SET tagName = '{tagName}', category = '{category}'
            WHERE postTagId = {postTagId}
        '''
        
        current_app.logger.info(f'Updated post_tag {postTagId} PUT /post_tags/{postTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        
        response = make_response(f'User_tag {postTagId} updated')
        response.status_code = 200
        return response
    elif request.method == 'DELETE': # Delete a user
        query = f'''
        DELETE
        FROM postTagParent
        WHERE postTagId = {postTagId}
        '''
    
        current_app.logger.info(f'Deleted user_tag {postTagId} DELETE /post_tags/{postTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(f'post_tag {postTagId} deleted')
        response.status_code = 200
        return response