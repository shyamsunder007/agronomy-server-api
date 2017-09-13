from django.db import models
from datetime import datetime

class village(models.Model):                       
	id= models.AutoField(primary_key=True)
	village_name=models.CharField(max_length=20)	
class Households(models.Model):
	id=models.AutoField(primary_key=True)
	Households_lat=models.CharField(max_length=20)
	Households_lon=models.CharField(max_length=20)
	Households_vilid=models.CharField(max_length=20)

class person(models.Model):
	id=models.AutoField(primary_key=True)

	person=models.CharField(max_length=20)
	gender=models.CharField(max_length=20)
	age=models.CharField(max_length=20)
	person_hid=models.CharField(max_length=20)

class farm(models.Model):
	id=models.AutoField(primary_key=True)
	house_id=models.CharField(max_length=20)
	farm_area=models.CharField(max_length=20)
	season_crop=models.CharField(max_length=20)

class points(models.Model):
	id=models.AutoField(primary_key=True)
	farm_id=models.CharField(max_length=20)
	lat=models.CharField(max_length=20)
	lon=models.CharField(max_length=20)

class well(models.Model):
	id=models.AutoField(primary_key=True)
	farm_id=models.CharField(max_length=20)
	lat=models.CharField(max_length=20)
	lon=models.CharField(max_length=20)

class wateryield(models.Model):
	id=models.AutoField(primary_key=True)
	well_id=models.CharField(max_length=20)
	yieldd=models.CharField(max_length=20)
	DateTimeField=models.DateTimeField(default=datetime.now,blank=True)









# Create your models here.
