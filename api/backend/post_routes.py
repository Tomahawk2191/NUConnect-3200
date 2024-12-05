from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

post = Blueprint('post', __name__)

#------------------------------------------------------------

@post.route('/posts', methods=['GET', 'POST'])
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
    
    elif request.method == 'POST':
        theData = request.json
        current_app.logger.info(theData)
        postAuthor = theData['postAuthor']
        title = theData['title']
        body = theData['body']
        userId = theData['userId']
        programId = theData['programId']

        query = f'''
            INSERT INTO post (postAuthor, title, body, userId, programId)
            VALUES ('{postAuthor}', '{title}', '{body}', '{userId}', '{programId}')
        '''
        current_app.logger.info(f'Added new user {postAuthor}, {title}, {body}, {userId}, {programId} POST /users query = {query}')

        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

