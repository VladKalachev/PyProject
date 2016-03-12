from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    return HttpResponse("Hove a you?")



def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>Сейчас %s.</body></html>' % now
    return HttpResponse(html)