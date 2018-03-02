from db.database import database as db
from datetime import datetime
from sqlalchemy.orm import relationship

class Group(db.Model):
  __tablename__ = 'Groups'
  id = db.Column(db.Integer, primary_key=True)
  group_name = db.Column(db.String(128))
  group_type = db.Column(db.String(128))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())
  updated_at = db.Column(db.DateTime, default=datetime.utcnow())
  users = relationship('User', secondary='UsersToGroups')
  backref = db.backref('Groups')

  def __repr__(self):
    return '<id {}>'.format(self.id)