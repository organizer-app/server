import os, sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db.database import database, db_session
import app.models.user, app.models.place, app.models.group, app.models.userstogroups

flask_app = Flask(__name__)

if os.environ.get('DEVELOPMENT_ENVIRONMENT') != 'production':
  flask_app.config.from_pyfile('config/settings.cfg')
else:
  flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
  flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

database.init_app(flask_app)
migrate = Migrate(flask_app, database)

from app.models.user import User

new_user = User('123', 'Jeffrey', 'Jeffrey Goldsmith', 'jeff.goldsmith@shopify.com', '123')
# user = User()
# user.first_name = 'Jeffrey'
# user.full_name = 'Jeffrey Goldsmith'
# user.email = 'jeff.goldsmith@shopify.com'
# db_session.add(user)
# db_session.commit()

import app.views, app.controllers.google_sign_on_controller
