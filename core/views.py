from django.shortcuts import render, HttpResponse
from hello_django import urls

# Create your views here.
def hello(request,nome):
    return HttpResponse(f'<h1>Olá {nome}</h1>')