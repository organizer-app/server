from app.db.database import database as db
from datetime import datetime
from sqlalchemy.orm import relationship, backref

class UserToGroup(BaseModel):
  __tablename__ = 'UsersToGroups'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
  created_at = db.Column(db.DateTime, default=datetime.utcnow())
  updated_at = db.Column(db.DateTime, default=datetime.utcnow())


  user = relationship(User, backref=backref("UsersToGroups"))
  product = relationship(Product, backref=backref("UsersToGroups"))