from django.http import HttpResponse
from django.shortcuts import render 

def power(request):
    number = int(request.GET['number'])
    number = number*number
    return HttpResponse(f'<h1>{number}</h1>')

def tomjerry(request):
    return HttpResponse('<h1>tom&jerry</h1>') 

def heyriya(request):
    return HttpResponse('<h1>heyriya</h1>')       
