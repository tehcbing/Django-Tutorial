#define paths to different pages (views)

from django.urls import path
from . import views #import views from current dir

urlpatterns= [
path("<int:id>", views.index, name="index"), # this serves as the index of the webpage
path("", views.home, name="home"),
path("create/", views.create, name="create"),
]
