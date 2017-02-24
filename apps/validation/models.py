from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):
	def validate(self, **kwargs):
		status = {}
		submitted_email = kwargs['email'][0] 
		if len(submitted_email) < 1:
			status.update({'vaild': False, 'error_msg': "Email Field Cannot Be Empty"})
		elif not EMAIL_REGEX.match(submitted_email):
			status.update({'valid': False, 'error_msg': "Invalid Email!"})
		else:
			status.update({'valid': True})
		return status

class Email(models.Model):
	email = models.EmailField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	emailManager = EmailManager()