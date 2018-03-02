import os, sys, yaml
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db.database import database
import app.models.user, app.models.place

flask_app = Flask(__name__)

if os.environ.get('DEVELOPMENT_ENVIRONMENT') != 'production':
  file = open('app/config/settings.yml')
  dataMap = yaml.load(file)
  file.close()
  for key, value in dataMap.items():
    os.environ[key] = value

database.init_app(flask_app)
migrate = Migrate(flask_app, database)

import app.views, app.controllers.google_sign_on_controller
