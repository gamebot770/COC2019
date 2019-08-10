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

class Invoice(models.Model):
    customerNum = models.IntegerField()
    customerfName = CharField(max_length = 25)
    customerlName = CharField(max_length = 25)
    finalSale = FloatField()
    discount = FloatField()
    sendInvoice = CharField(max_length = 200)
    total = FloatField()

class



