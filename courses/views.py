from django.shortcuts import render
from django.http import HttpResponse

def courses_home(request):
    return HttpResponse("Welcome to Courses App")
