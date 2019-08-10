from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from dashboard.models import *

import json
# Create your views here.
def dashboard(request):
    return render(request,'index.html',{})

def itemView(request):
    itemList = Item.objects.all()
    print(itemList)
