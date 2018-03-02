from db.database import database as db
from app.models.user import User
from app.models.group import Group
from datetime import datetime
from sqlalchemy.orm import relationship, backref

class UsersToGroups(db.Model):
  __tablename__ = 'UsersToGroups'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
  group_id = db.Column(db.Integer, db.ForeignKey('Group.id'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())
  updated_at = db.Column(db.DateTime, default=datetime.utcnow())


  user = relationship(User, backref=db.backref("UsersToGroups"))
  group = relationship(Group, backref=db.backref("UsersToGroups"))