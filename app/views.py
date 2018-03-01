from app import flask_app
from flask import render_template

@flask_app.route('/')
def index():
    return render_template('index.html')