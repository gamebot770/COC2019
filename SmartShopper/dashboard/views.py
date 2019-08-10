from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from dashboard.models import *

import json
# Create your views here.
def dashboard(request):
    pk = 0
    user.object.get(username= 'gamebot')
    return HttpResponse("Hi")

def itemView(request):
    pk = 0
    item = Item.objects.get(pk)
    return render(request, '',{"item":item})

def invoiceView(request):
    pk = 0
    invoice = Invoice.objects.get(pk)
    return render(request, '', {"invoice":invoice})
