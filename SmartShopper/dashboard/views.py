from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from dashboard.models import *
import copy
import json
# Create your views here.
def dashboard(request):
    i = Invoice.objects.all()
    print(len(i))
    for j in i:
        i.delete()
    print(Invoice.objects.all())
    return render(request,'inv.html',{})

def itemView(request):
    pk = 0
    item = Item.objects.get(pk)
    return render(request, '',{'item':item})

def invoiceView(request):
    pk = 0
    invoice = Invoice.objects.all()
    return render(request, 'invoice.html', {'invoices':invoice})

def inven(request):
    inventory = Item.objects.all()
    return render(request, 'inv.html', {'items':inventory})

def invoiceDetails(request, pk):
    invoice = Invoice.objects.get(pk=pk)

    return render(request, 'invoicedetails.html', {'invoice': invoice})

def addInvoice(request):
    items = Item.objects.all()
    return render(request,"invoiceAdd.html",{"items":items})

def getQuantity(request):
    pk = request.POST["pk"]
    item = Item.objects.get(pk=pk)
    return JsonResponse({"quantity":item.stock})

def createInvoice(request):
    if request.method == "POST":
        invoice = Invoice()
        invoice.customerNum = "99"
        invoice.customerfName = request.POST["customerFirstName"]
        invoice.customerlName = request.POST["customerLastName"]
        invoice.total = request.POST["total"]
        invoice.discount = request.POST["discount"]
        try:
            invoice.sendInvoice = request.POST["sendInvoice"]
        except:
            invoice.sendInvoice = False
        invoice.finalSale = request.POST["finalSale"]
        invoice.save()

        items = []
        keys = request.POST.keys()
        seenKeys = []
        for key in request.POST.keys():
            if ("invoicePK" in key or "invoiceQuantity" in key) and not key in seenKeys:
                if "invoicePK" in key:
                    items.append(tuple([request.POST[key],request.POST["invoiceQuantity" + key[-1]]]))
                else:
                    items.append(tuple([request.POST["invoicePK" + key[-1]],request.POST[key]]))
                seenKeys.append(key)
                seenKeys.append("invoiceQuantity" + key[-1])

        for item in items:
            invoiceItem = InvoiceItem()
            invoiceItem.item = Item.objects.get(pk=item[0])
            invoiceItem.quantity = item[1]
            invoiceItem.invoice = invoice
            invoiceItem.save()

        return HttpResponseRedirect(reverse("invoiceView"))

def addInventoryManual(request,addAnother=None):
    if request.method=="GET":
        items = Item.objects.all()
        return render(request,"addManualStock.html",{"items":items})
    else:
        pk = request.POST["item"]
        item = Item.objects.get(pk=pk)
        item.stock += int(request.POST["count"])
        item.save()

        update = stockUpdate()
        update.item = item
        update.count = request.POST["count"]
        update.save()

        if addAnother:
            return HttpResponseRedirect(reverse("addIneventoryManual"))
        else:
            return HttpResponseRedirect(reverse("inventoryView"))
