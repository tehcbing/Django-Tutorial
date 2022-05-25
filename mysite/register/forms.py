from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	# allows us to change some of the parent properties
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"] # specify the order in which you want your fields to show up
