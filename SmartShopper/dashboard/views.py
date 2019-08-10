from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from dashboard.models import *

import json
# Create your views here.
def dashboard(request):
    return render(request,'invoice.html',{})

def itemView(request):
    pk = 0
    item = Item.objects.get(pk)
    return render(request, '',{"item":item})

def invoiceView(request):
    pk = 0
    invoice = Invoice.objects.get(pk)
    return render(request, '', {"invoice":invoice})
