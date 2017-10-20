from django.db import models

# Create your models here.
class Section(models.Model):
	section_name = models.CharField(max_length=200)
	section_room = models.CharField(max_length=200)
	

	def __str__(self):
		return self.section_name + '-' + self.section_room
class Student(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	gender = models.CharField(max_length=200)
	course= models.CharField(max_length=200)
	year = models.CharField(max_length=200)
	section_id = models.ForeignKey(Section)

	def __str__(self):
		return self.name + '-' + self.gender + '-' + self.course+ '-' + self.year

	