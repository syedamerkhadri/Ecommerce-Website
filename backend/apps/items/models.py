# Create your models here.
from django.db import models
from config.constants import *
from cloudinary.models import CloudinaryField


class Item(models.Model):
    class Meta(object):
        db_table = 'item'
    
    STATUS= models.CharField(
        'Status', blank=False, default='inactive' ,null=False, max_length=50, db_index=True,choices= STATUS 
    )
    name = models.CharField(
        'Name', blank=False, null=False, max_length=120, db_index=True, default='Anonymous'
    )
    price = models.IntegerField(
        'Price', blank=False, null=False, db_index=True
    )
    description = models.CharField(
        'Description', blank=False, null=False, max_length=200, db_index=True, default=0
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
