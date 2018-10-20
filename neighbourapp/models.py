from django.db import models

# Create your models here.

class NeighbourHood(models.Model):
    image_name = models.CharField(max_length =30)
    image_location = models.CharField(max_length =30)
    Occupants Count = models.PositiveIntegerField()
    Admin Foreign key = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)

# class Business(models.Model):
#     name = models.CharField(max_length=30)
#     id=models.PositiveIntegerField()
