from db.database import database as db
from datetime import datetime

class Place(db.Model):
  __tablename__ = 'Places'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  address = db.Column(db.String(128))
  price = db.Column(db.String(4))
  website = db.Column(db.String(128))
  phone = db.Column(db.String(128))
  categories = db.Column(db.String)
  photos = db.Column(db.String)
  longitude = db.Column(db.Float)
  latitutde = db.Column(db.Float)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return '<id {}>'.format(self.id)