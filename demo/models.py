from django.db import models

# Create your models here.

class repair(models.Model):
	Name=models.CharField(max_length=30)
	Device=models.CharField(max_length=10)
	Company=models.CharField(max_length=20)
	Type=models.CharField(max_length=20)
	Problem=models.CharField(max_length=100)
	Phone=models.IntegerField()
	Address=models.CharField(max_length=100)
	class Meta:
		db_table="demo_repairs"
		

def __str__(self):
	return self.Name		

class suggestion(models.Model):
	Name=models.CharField(max_length=30)
	Contact=models.CharField(max_length=10)
	Email=models.CharField(max_length=20)
	Message=models.CharField(max_length=100)
	class Meta:
		db_table="demo_suggestions"

def __str__(self):
	return self.Name


