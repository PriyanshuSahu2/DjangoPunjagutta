from django.urls import path

from myapp.views import home, login


urlpatterns = [
    path('', home, name='Home'),
    path('login/', login, name='Login')
]
