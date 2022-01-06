# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField

class User(models.Model):
    class Meta(object):
        db_table = 'user'
        
    user_name= models.CharField(
        'Username', blank=False, null=False, max_length=50, db_index=True,  
    )
    password= models.CharField(
        'Password', blank=False, null=False, max_length=500, db_index=True,
    )
    email= models.EmailField(
        'Email', blank=False, max_length=254, null=False, db_index=True
    )
    token= models.CharField(
        'Token', blank=False, max_length=500, null=False, db_index=True
    )
    token_expires_at= models.DateTimeField(
        'Token_expires_at', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )

