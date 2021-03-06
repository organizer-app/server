import os
from app import flask_app
from google.oauth2 import id_token
from google.auth.transport import requests
import datetime
from flask import request
import jwt

def authenticate_user(token):
  user_info = get_authenticated_info(request.get_json().get('token'))
  # query user id 

  # if user id is new
    # create a new user
  return generate_user_token(user_info['sub'])

def get_authenticated_info(token):
  try:
    id_info = id_token.verify_oauth2_token(token, requests.Request(), '153497318804-fv3cc14468utuqri4g6upju4mvodr0a0.apps.googleusercontent.com')
   
    if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
      raise ValueError('Wrong issuer.')

    return id_info

  except ValueError as e:
    raise ValueError('Invalid Token.' + str(e))
  
def generate_user_token(user_id):
  token = jwt.encode({'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, os.environ.get('SECRET_KEY'))
  return token.decode('UTF-8')
