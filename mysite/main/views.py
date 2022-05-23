from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here (a view is kind of like a webpage)

def index(response, id):
	# get todolist based on id
	ls = ToDoList.objects.get(id=id)

	#get items in todolist
	item = ls.item_set.get(id=1)

	return HttpResponse("<h1>%s</h1> %s" %(ls.name, item.text)) 
