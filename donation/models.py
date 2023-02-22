from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
category=(
    ("food","FOOD"),
    ("clothing","CLOTHING"),
    ("utensils","UTENSILS"),
    ("books","BOOKS"),
    ("Others","OTHERS"),
) 
class Item(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length = 30,choices=category,default="clothing")
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name="created")
    desc = models.TextField(default = "")
    cost = models.IntegerField(null=True)  
    created_on = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to="login/images",default="{% static 'images/NA_img.svg'%}")  
    booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(User, null= True,on_delete = models.CASCADE,related_name="booked")
    def __str__(self):
        return self.name
    
class orders(models.Model):
    item_ordered = models.ForeignKey(Item, on_delete = models.CASCADE)
    ordered_by = models.ForeignKey(User, on_delete = models.CASCADE)
    placed_on = models.DateTimeField( blank=True )
    
    def __str__(self):
        return self.item_ordered.name
    
class Donate(models.Model):
    donated_by = models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.IntegerField(null=False)
    donated_on = models.DateTimeField()
    def __str__(self):
        return self.donated_by.email