from django.http import HttpResponse, HttpResponseNotFound
import app.helpers.google_sign_on_helper as sign_on
import jwt

def google_sign_on_controller(request):
  if (request.method == 'POST'):
    print(request)
    try:
      authenticated_token = sign_on.authenticate_user(request.get_json().get('token'))
      return jsonify({'token' : authenticated_token})
    except ValueError as e:
      return jsonify({'message' : str(e)}), 403
  return HttpResponse(status=201)