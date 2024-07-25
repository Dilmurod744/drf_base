from django.contrib.auth.models import AbstractUser
from django.db.models import Model,  CharField,DecimalField, ForeignKey, CASCADE


# Create your models here.


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
