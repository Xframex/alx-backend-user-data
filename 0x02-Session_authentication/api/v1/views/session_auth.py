#!/usr/bin/env python3
'''Session authentication module for the API.'''

from flask import abort, request, jsonify
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    '''auth login routr'''
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    SESSION_NAME = 'session_id'
    response = jsonify(user[0].to_json())
    cookie = os.getenv('SESSION_NAME') 
    response.set_cookie(SESSION_NAME, session_id)
    return response

@app_views.route(
    '/auth_session/logout' , methods=['DELETE'], strict_slashes=False)
def logout():
    '''Delete or logout session '''
    from api.v1.app import auth
    destroy_session = auth.destroy_session(request)
    if not destroy_session:
        abort(404)
    return jsonify({})
