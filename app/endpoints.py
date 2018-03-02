from app import flask_app
from app.api.controllers.search_controller import get_recommendations

@flask_app.route('/search')
def search():
    return get_recommendations()
