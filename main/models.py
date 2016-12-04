from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stage(models.Model):
	name = models.CharField(max_length=255) 
	
	def __unicode__(self):
		return self.name

class Grade(models.Model):
	name = models.CharField(max_length=255)
	stage = models.ForeignKey(Stage)
	def __unicode__(self):
		return self.name


class Subfield(models.Model):
	grade = models.ForeignKey(Grade)
	name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.name
class Papersheet(models.Model):
	name = models.CharField(max_length=255)
	subfield = models.ForeignKey(Subfield)
	file = models.FileField(upload_to='papersheet')
	date =models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)

class Teacher(models.Model):
	name = models.CharField(max_length=255) 

class Counter(models.Model):
	number = models.IntegerField()