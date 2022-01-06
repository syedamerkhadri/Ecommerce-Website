# Create your models here.
from django.db import models
from apps.items.models import Item
from apps.users.models import User

class Cart(models.Model):
    class Meta(object):
        db_table = 'cart'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, db_index=True
    )
    quantity = models.IntegerField(
        'Quantity', blank=False, null=False, db_index=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
