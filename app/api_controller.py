from app import flask_app
import app.api.endpoints.yelp_search as search_api

@flask_app.route('/search')
def search():
    return search_api.get_recommendations()
