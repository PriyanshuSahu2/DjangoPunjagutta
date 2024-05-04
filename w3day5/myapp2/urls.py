from django.urls import path

from myapp2.views import home


app_name = "myapp2"
urlpatterns = [
    path('', home, name="home"),
]
