#define paths to different pages (views)

from django.urls import path
from . import views #import views from current dir

urlpatterns= [
path("", views.index, name="index"), # this serves as the index of the webpage
path("v1/", views.v1, name="view 1"),
]
