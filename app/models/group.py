from django.db import models
from app.models.user import User

class Group(models.Model):
  group_name = models.CharField(max_length=100)
  group_type = models.CharField(max_length=100)
  users = models.ManyToManyField(User)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    app_label='app'
    db_table='Groups'