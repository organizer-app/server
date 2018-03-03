from django.db import models

class User(models.Model):
  google_id = models.IntegerField()
  first_name = models.CharField(max_length=100)
  full_name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  photo_url = models.CharField(max_length=256)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    app_label='app'
    db_table='Users'