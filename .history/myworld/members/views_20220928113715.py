from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import 

def index(request):
    return HttpResponse('hello world')