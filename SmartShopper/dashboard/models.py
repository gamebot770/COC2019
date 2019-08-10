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
    cost = models.FloatField()
    salePrice = models.FloatField()
    bulkThreshold = models.IntegerField()

    def __str__(self):
        return self.name

class SupplierItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    frequency = models.IntegerField()
    price = models.FloatField()
    amountDue = models.FloatField()

class Supplier(models.Model):
    name = models.CharField(max_length=100)






