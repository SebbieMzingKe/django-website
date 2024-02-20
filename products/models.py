from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length = 255)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    image_url = models.CharField(max_length = 2083)


class Offer(models.Model):
    code = models.CharField(max_length = 10)
    description = models.CharField(max_length  = 255)
    discount = models.FloatField(null = True, blank = True)


class Fruit(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()