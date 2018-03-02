import os, sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db.user import db

flask_app = Flask(__name__)

if os.environ.get('ENVIRONMENT') is None:
  flask_app.config.from_pyfile('config/settings.cfg')

db.init_app(flask_app)
migrate = Migrate(flask_app, db)

import app.views, app.api_controller

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  flask_app.run(host='0.0.0.0', port=port, debug=True)
