from django.db import models

# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=900)
    address = models.CharField(max_length=900)
    numOfCustomers = models.IntegerField()

class Item(models.Model):
    name = models.CharField(max_length=100)
    soldMonth = models.IntegerField()
    soldYear = models.IntegerField()
    soldDaily = models.IntegerField()
    soldWeekly = models.IntegerField()
    stock = models.IntegerField()
    def __str__(self):
        return self.name



