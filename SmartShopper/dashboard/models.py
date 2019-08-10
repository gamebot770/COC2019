from django.db import models

# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=900)
    address = models.CharField(max_length=900)
    numOfCustomers = models.IntegerField()
