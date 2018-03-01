import os
from flask import Flask, render_template

flask_app = Flask(__name__)
flask_app.config.from_pyfile('config/settings.cfg')

import app.views, app.endpoints

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host='0.0.0.0', port=port, debug=True)