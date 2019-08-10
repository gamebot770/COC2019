from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse

import json
# Create your views here.
def dashboard(request):
    return HttpResponse("Hi")