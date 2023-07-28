from django.db import models

# Create your models here.

class Human(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=100)
    birth_date=models.DateField()
    job=models.CharField(max_length=20)
