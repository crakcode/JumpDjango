from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse("hell owrodl")



def sayHello(request):
    return HttpResponse("hellsss oworlsdadasdsss")