from app import flask_app
import app.api.helpers.google_sign_on_helper as sign_on
from flask import jsonify, request
import jwt
from functools import wraps
 
def token_required(f):
  def decorated(*args, **kwargs):
    token = request.args.get('token')

    if not token:
      return jsonify({'message' : 'Token is missing!'}), 403

    try:
      data = jwt.decode(token, app.config.get('SECRET_KEY'))
    except:
        return jsonify({'message' : 'Token is invalid'}), 403

    return f(*args, **kwargs)
  return decorated

@flask_app.route('/authenticate', methods=['POST'])
@token_required
def authenticate():
  try:
    authenticated_token = sign_on.authenticate_user(request.args.get('token'))
    return jsonify({'token' : authenticate_msg})
  except ValueError as e:
    return jsonify({'message' : str(e)})



