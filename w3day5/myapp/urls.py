from operator import index
from django.urls import path

from myapp.views import *


app_name = "myapp"
urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),
]
