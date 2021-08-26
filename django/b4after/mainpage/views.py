from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
# from .models import Coffee

import json 
# Create your views here.
def index(request):
    args = {
        "name" : "arg"
    }
    return render(request, "index.html", args)

def index2(request):
    return HttpResponse("Hello, world. You're at the polls now.")

def index3(request):
    template = loader.get_template("index.html")
    args = {
        "a": 'b'
    }
    return HttpResponse(template.render(args, request))

def generic(request):
	return render(request, "generic.html")