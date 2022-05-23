from django.shortcuts import render

#step 1
from django.http import HttpResponse

# Create your views here (a view is kind of like a webpage)

#step 2: create a function
def index(response):
	return HttpResponse("Hello World!") # html code goes in here

def v1(response):
	return HttpResponse("View 1")