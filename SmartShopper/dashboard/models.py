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
    costPrice = models.FloatField(null=True, blank=True, default=None)
    salesPrice = models.FloatField(null=True, blank=True, default=None)
    stock = models.IntegerField()
    def __str__(self):
        return self.name

class Invoice(models.Model):
    customerNum = models.IntegerField()
    customerfName = models.CharField(max_length = 25)
    customerlName = models.CharField(max_length = 25)
    finalSale = models.FloatField()
    discount = models.FloatField()
    sendInvoice = models.CharField(max_length = 200)
    total = models.FloatField()




