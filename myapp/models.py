from django.db import models
# Create your models here.
class REG(models.Model):
    usermob=models.IntegerField()
    Fname=models.CharField(max_length=10)
    Lname=models.CharField(max_length=10)
    pwd=models.CharField(primary_key=True,max_length=20)