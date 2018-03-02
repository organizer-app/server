from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'Users'
  id = db.Column(db.Integer, primary_key=True)
  google_id = db.Column(db.Integer)
  first_name = db.Column(db.String(128))
  full_name = db.Column(db.String(128))
  email = db.Column(db.String(128))
  photo_url = db.Column(db.String(256))

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return '<id {}>'.format(self.id)