from app import flask_app
import app.helpers.google_sign_on_helper as sign_on
from flask import jsonify, request
import jwt
from functools import wraps

def token_required(f):
  def decorated(*args, **kwargs):
    token = request.get_json().get('token')

    if not token:
      return jsonify({'message' : 'Token is missing!'}), 403

    try:
      data = jwt.decode(token, app.config.get('SECRET_KEY'))
    except:
        return jsonify({'message' : 'Token is invalid'}), 403

    return f(*args, **kwargs)
  return decorated

@flask_app.route('/authenticate', methods=['POST'])
def authenticate():
  try:
    authenticated_token = sign_on.authenticate_user(request.get_json().get('token'))
    return jsonify({'token' : authenticated_token})
  except ValueError as e:
    return jsonify({'message' : str(e)}), 403



