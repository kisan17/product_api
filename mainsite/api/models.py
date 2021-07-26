from django.db import models
from django.db.models.fields import IntegerField

class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.IntegerField()
    star=models.IntegerField()


    def __str__(self):
        return self.name
        
