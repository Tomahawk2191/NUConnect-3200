from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

role = Blueprint('role', __name__)

#------------------------------------------------------------
# Role routes
#------------------------------------------------------------
# Return a list of all roles
@role.route('/role', methods=['GET', 'POST'])
def get_roles():
    if request.method == 'GET':
        query = f'''
            SELECT *
            FROM role
        '''
    
        current_app.logger.info(f'GET /role query = {query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    elif request.method == 'POST': #Creates a new role
        theData = request.json
        current_app.logger.info(theData)
    
        roleName = theData['name']
        canPost = theData['canPost'] 
        canApprove = theData['canApprove'] 
        canAssignProf = theData['canAssignProf'] 
        canApply = theData['canApply'] 
        canRetract = theData['canRetract'] 
        canEditOwn = theData['canEditOwn'] 
        canEditAll = theData['canEditAll'] 
        canDeleteOwn = theData['canDeleteOwn'] 
        canDeleteAll = theData['canDeleteAll'] 
        canUpdateAcceess = theData['canUpdateAcceess'] 
    
        query = f'''
            INSERT INTO role (name, 
                              canPost, 
                              canApprove, 
                              canAssignProf, 
                              canApply, 
                              canRetract, 
                              canEditOwn, 
                              canEditAll, 
                              canDeleteOwn, 
                              canDeleteAll, 
                              canUpdateAcceess)
            VALUES ('{roleName}', '{canPost}', 
                    '{canApprove}', '{canAssignProf}', 
                    '{canApply}', '{canRetract}'),
                    '{canEditOwn}', '{canEditAll}'),
                    '{canDeleteOwn}', '{canDeleteAll}', 
                    {canUpdateAcceess})
        '''
    
        current_app.logger.info(f'Added new role {roleName} POST /role query = {query}')
    
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        response = make_response('Added new role')
        response.status_code = 200
        return response

#------------------------------------------------------------
# Return a role by their ID
@role.route('/role/<int:roleId>', methods=['GET', 'PUT', 'DELETE'])
def get_role(roleId):
    if request.method == 'GET': # Get a role
        query = f'''
            SELECT *
            FROM role
            WHERE roleId = {roleId}
        '''
        
        # Log the query
        current_app.logger.info(f'GET /role/{roleId} query = {query}')
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    elif request.method == 'PUT': # Update a role
        theData = request.json
        current_app.logger.info(theData)
        
        roleName = theData['name']
        canPost = theData['canPost'] 
        canApprove = theData['canApprove'] 
        canAssignProf = theData['canAssignProf'] 
        canApply = theData['canApply'] 
        canRetract = theData['canRetract'] 
        canEditOwn = theData['canEditOwn'] 
        canEditAll = theData['canEditAll'] 
        canDeleteOwn = theData['canDeleteOwn'] 
        canDeleteAll = theData['canDeleteAll'] 
        canUpdateAcceess = theData['canUpdateAcceess'] 
    
        query = f'''
            UPDATE role
            SET name = '{roleName}', 
                canPost = '{canPost}', 
                canApprove = '{canApprove}',
                canAssignProf = '{canAssignProf}', 
                canApply = '{canApply}', 
                canRetract = '{canRetract}', 
                canEditOwn = '{canEditOwn}', 
                canEditAll = '{canEditAll}', 
                canDeleteOwn = '{canDeleteOwn}',
                canDeleteAll = '{canDeleteAll}',
                canUpdateAcceess = '{canUpdateAcceess}',
            WHERE roleId = {roleId}
        '''
        
        current_app.logger.info(f'Updated role {roleId} PUT /role/{roleId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()
        
        response = make_response(f'Role {roleId} updated')
        response.status_code = 200
        return response

    elif request.method == 'DELETE': # Delete a role
        query = f'''
        DELETE
        FROM role
        WHERE roleId = {roleId}
        '''
    
        current_app.logger.info(f'Deleted role {roleId} DELETE /role/{roleId} query = {query}')
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(f'Role {roleId} deleted')
        response.status_code = 200
        return response