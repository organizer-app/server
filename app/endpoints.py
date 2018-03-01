from app import flask_app

import sys
sys.path.insert(0, './app/api')
import api

@flask_app.route('/test')
def test():
    return api.reply('Hello World')
