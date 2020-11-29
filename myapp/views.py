from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)
def index(request):
   text = """<h1>welcome to index page !</h1>"""
   return HttpResponse(text)
def home(request):
   text = """<h1>welcome to home </h1>"""
   return HttpResponse(text)