from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# models
class UserManager(models.Manager):
  def validate(self, post_data):
    errors = []
    if len(post_data['fname']) < 2:
      errors.append("User first name should be more than 2 characters")
    if len(post_data['lname']) < 2:
      errors.append("User last name should be more than 2 characters")
    if not re.match(EMAIL_REGEX, post_data['email']):
      errors.append("invalid email") 
    #  existing email check
    else:
      if len(self.filter(email=post_data['email'])) > 0:
        errors.append("email already in use")
    return errors

class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()
  # def __str__(self):
  #   return "<User object: {} {} {}>".format(self.firstname, self.lastname, self.email)