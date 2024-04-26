from django.urls import path
from .views import *
urlpatterns = [

    path('', news),
    path('sports/', news_sports),
    path('movies/', news_movies),
    path('politics/', news_politics),
]
