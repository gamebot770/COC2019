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
    dateCreated = models.DateField(auto_now_add=True,blank=True,null=True)

class Supplier(models.Model):
    name = models.CharField(max_length=100)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField()

class stockUpdate(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return "Restock of " + str(self.count) + " orders of " + self.item.name
