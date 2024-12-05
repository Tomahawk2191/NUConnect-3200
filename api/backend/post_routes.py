from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

post = Blueprint('post', __name__)

#------------------------------------------------------------

@post.route('/posts', methods=['GET'])
def get_posts():
    if request.method == 'GET':
        query = f'''
            SELECT * 
            FROM post
        '''
        current_app.logger.info(f'GET /posts query = {query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    

#------------------------------------------------------------

@post.route('/users/<int:userId>/posts/<int:postId>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def get_post_info(userId, postId):
    if request.method == 'GET':

        query = f'''
            SELECT * 
            FROM post
            WHERE postId = {postId}
        '''

        
        current_app.logger.info(f'GET /posts/{userId}/posts/{postId} query = {query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    
    elif request.method == 'POST':
        theData = request.json
        current_app.logger.info(theData)
        postAuthor = theData['postAuthor']
        title = theData['title']
        body = theData['body']
     #   userId = {userId}
        programId = theData['programId']

        query = f'''
            INSERT INTO post (postAuthor, title, body, userId, programId)
            VALUES ('{postAuthor}', '{title}', '{body}', '{userId}', '{programId}')
        '''
        current_app.logger.info(f'Added new user {postAuthor}, {title}, {body}, {userId}, {programId} POST /users/{userId}/posts/{postId} 
                                query = {query}')

        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    
    elif request.method == 'PUT':
        theData = request.json
        current_app.logger.info(theData)
        postAuthor = theData['postAuthor']
        title = theData['title']
        body = theData['body']
        
        query = f'''
            UPDATE post
            SET postAuthor = '{postAuthor}', title = '{title}', body = '{body}'
            WHERE postId = {postId}
        '''
    
        current_app.logger.info(f'Updated user {userId} PUT /users/{userId}/posts/{postId} query = {query}')
    
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    
    elif request.method == 'DELETE': 
        query = f'''
        DELETE
        FROM post
        WHERE postId = {postId}
        '''
    
        current_app.logger.info(f'Deleted user {userId} DELETE /users/{userId}/posts/{postId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

