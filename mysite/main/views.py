from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here (a view is kind of like a webpage)

def index(response, id):
	ls = ToDoList.objects.get(id=id)
	return render(response, "main/list.html", {"ls":ls})

def home(response):
	return render(response, "main/home.html", {"name":"test"})

def create(response):
	if response.method == "POST":
		# gets information from our form and stores it as a dict.
		form = CreateNewList(response.POST)  

		if form.is_valid():
			# n accesses the previously retrieved data
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()
	return render(response, "main/create.html", {"form":form})