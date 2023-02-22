from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class User_profile(models.Model):
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length = 10 ,default='0')
    
    city  = models.CharField(max_length=16, default="")
    state  = models.CharField(max_length=16, default="")
    zipcode =models.CharField(max_length=6, default="")  

    def __str__(self):
        return self.first_name + self.last_name
    

