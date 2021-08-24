from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Coffee

import json 
# Create your views here.
def index2(request):
    return render(request, "index.html", args)