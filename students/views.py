from django.shortcuts import render
from django.http import HttpResponse

def students_home(request):
    return HttpResponse("Welcome to Students App")