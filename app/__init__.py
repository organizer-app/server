import os, sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db.database import database
import app.models.user, app.models.place

flask_app = Flask(__name__)

if os.environ.get('DEVELOPMENT_ENVIRONMENT') != 'production':
  flask_app.config.from_pyfile('config/settings.cfg')
else:
  flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
  flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

database.init_app(flask_app)
migrate = Migrate(flask_app, database)

import app.views, app.controllers.google_sign_on_controller
