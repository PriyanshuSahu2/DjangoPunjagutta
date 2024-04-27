from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name="Home"),
    path('contact/',contact,name="Contact")
]
