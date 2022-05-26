from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ToDoList(models.Model): #create a db object called ToDoList
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=200) # attribute

	def __str__(self):
		return self.name

class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # if we delete this record in ToDoList, it will delete everything.
	text = models.CharField(max_length=300)
	complete = models.BooleanField() 

	def __str__(self):
		return self.text