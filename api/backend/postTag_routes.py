from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

post_tags = Blueprint('post_tags', __name__)

#------------------------------------------------------------
# Post tag routes
#------------------------------------------------------------
# Return a list of all post tags
@post_tags.route('/post_tags', methods=['GET', 'POST'])
def get_user_tags():
    if (request.method == 'GET'):
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

    elif (request.method == 'POST'): #Create a new post tag
        theData = request.json
        current_app.logger.info(theData)
        
        tagName = theData['tagName']
        category = theData['category']
        
        query = f'''
            INSERT INTO postTagParent (tagName, category)
            VALUES ('{tagName}', '{category}')
        '''
        
        current_app.logger.info(f'Added new post tag {tagName} POST /post_tags query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response('Added new post tag')
        response.status_code = 200
        return response

#------------------------------------------------------------
# Return a post tag by their ID
@post_tags.route('/post_tags/<int:postTagId>', methods=['GET', 'PUT', 'DELETE'])
def get_post_tag(postTagId):
    if request.method == 'GET': # Get a post tag
        query = f'''
            SELECT *
            FROM postTagParent
            WHERE postTagId = {postTagId}
        '''
        
        current_app.logger.info(f'GET /post_tags/{postTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    elif request.method == 'PUT': # Update a post tag
        theData = request.json
        current_app.logger.info(theData)
        
        tagName = theData['tagName']
        category = theData['category'] 
    
        query = f'''
            UPDATE postTagParent`
            SET tagName = '{tagName}', category = '{category}'
            WHERE postTagId = {postTagId}
        '''
        
        current_app.logger.info(f'Updated post tag {postTagId} PUT /post_tags/{postTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response(f'Post tag {postTagId} updated')
        response.status_code = 200
        return response

    elif request.method == 'DELETE': # Delete a post tag
        query = f'''
        DELETE
        FROM postTagParent
        WHERE postTagId = {postTagId}
        '''
    
        current_app.logger.info(f'Deleted post tag {postTagId} DELETE /post_tags/{postTagId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response(f'Post tag {postTagId} deleted')
        response.status_code = 200
        return response