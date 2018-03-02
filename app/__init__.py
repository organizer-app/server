import os, sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db.database import database
import app.models.user, app.models.place

flask_app = Flask(__name__)

if os.environ.get('ENVIRONMENT') is None:
  flask_app.config.from_pyfile('config/settings.cfg')

database.init_app(flask_app)
migrate = Migrate(flask_app, database)

import app.views, app.api.controllers.google_sign_on_controller
