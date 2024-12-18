from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

post = Blueprint('post', __name__)

#------------------------------------------------------------
# Post routes
#------------------------------------------------------------
# Returns all posts on platform 
@post.route('/posts', methods=['GET', 'POST', 'DELETE'])
def get_posts():
    if request.method == 'GET':
        query = f'''
            SELECT *
                FROM post AS p
        '''
        current_app.logger.info(f'GET /posts query = {query}')

        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    elif request.method == 'POST': # Create a post
        theData = request.json
        
        postAuthor = theData['postAuthor']
        title = theData['title']
        body = theData['body']
        userId = theData['userId']
        programId = theData['programId']
        
        query = f'''
            INSERT INTO post (postAuthor, title, body, programId, userId)
            VALUES ('{postAuthor}', '{title}', '{body}', '{userId}', '{programId}')
        '''
        current_app.logger.info(f'Added new post POST /posts query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        response = make_response('Added new post')
        response.status_code = 200
        return response

    elif request.method == 'DELETE': # Delete a post
        theData = request.json

        postId = theData['postId']
        
        query = f'''
            DELETE
            FROM post
            WHERE postId = {postId}
        '''
        
        current_app.logger.info(f'Deleted post {postId} DELETE /posts query = {query}')

        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response(f'Post {postId} deleted')
        response.status_code = 200
        return response
        
#------------------------------------------------------------

#------------------------------------------------------------
# Returns a specific post made by a user
@post.route('/users/<int:userId>/posts/<int:postId>', methods = ['GET', 'POST', 'PUT'])
def get_post_info(userId, postId):
    if request.method == 'GET': # Return a post's information
        query = f'''
            SELECT * 
            FROM post
            WHERE postId = {postId} and userId = {userId}
        '''
        current_app.logger.info(f'GET /posts/{userId}/posts/{postId} query = {query}')

        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    
    elif request.method == 'POST': # Create a post
        theData = request.json
        current_app.logger.info(theData)

        postAuthor = theData['postAuthor']
        title = theData['title']
        body = theData['body']
        programId = theData['programId']

        query = f'''
            INSERT INTO post (postAuthor, title, body, userId, programId)
            VALUES ('{postAuthor}', '{title}', '{body}', '{userId}', '{programId}')
        '''
        current_app.logger.info(f'Created new post {postAuthor}, {title}, {body}, {userId}, {programId} POST /users/{userId}/posts/{postId} query = {query}')

        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response('Created new post')
        response.status_code = 200
        return response
    
    elif request.method == 'PUT': # Update a post's information
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
    
        current_app.logger.info(f'Updated post {postId} PUT /users/{userId}/posts/{postId} query = {query}')
    
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response(f'Post {postId} updated')
        response.status_code = 200
        return response

# Returns all posts made by a specific professor
@post.route('/posts/<int:professorId>', methods = ['GET', 'DELETE'])
def get_posts_author(professorId):
    if request.method == 'GET':
        query = f'''
        SELECT *
        FROM post
        WHERE userId = {professorId}
        '''

        current_app.logger.info(f'GET /posts/{professorId} query = {query}')

        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    elif request.method == 'DELETE': # Delete a post associated with a professor
        query = f'''
        DELETE
        FROM post
        WHERE postId = {professorId}
        '''
    
        current_app.logger.info(f'Deleted post {professorId} DELETE /posts/{professorId}/ query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response(f'Post {professorId} deleted')
        response.status_code = 200
        return response