from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from dashboard.models import *

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
    return render(request, 'inv.html', {'inventory':inventory})

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
