from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.template import loader
from django.views import View
# from .models import Coffee

import json 
# Create your views here.
class IndexView(View):
    def get(self, request):
        dummy_data = {
            'name': '죠르디',
            'type': '공룡',
            'job': '편의점알바생',
            'age': 5
        }
        return JsonResponse(dummy_data)

    def post(self, request):
        return HttpResponse("Post 요청을 잘받았다")

    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")

    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")


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