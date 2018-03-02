from google.oauth2 import id_token
from google.auth.transport import requests
import datetime

def authenticate_user(token):
  user_info = get_authenticated_info(request.args.get('token'))
  # query user id 

  # if user id is new
    # create a new user
  return generate_user_token(user_info['sub'])

def get_authenticated_info(token):
  try:
    id_info = id_token.verify_oauth2_token(token, requests.Request(), config['GOOGLE_CLIENT_ID'])

    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')

    return id_info

  except ValueError:
    raise ValueError('Invalid Token.')
  
def generate_user_token(user_id):
  token = jwt.encode({'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
  return token.decode('UTF-8')