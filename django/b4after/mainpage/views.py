from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.template import loader
from django.views import View

import json 
# Create your views here.


def index(request):
    args = {
        "name" : "arg"
    }
    return render(request, "index.html", args)

def generic(request):
	return render(request, "generic.html")