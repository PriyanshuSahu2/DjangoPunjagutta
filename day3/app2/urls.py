from django.urls import path

from .views import about, blog, contact, home, profile


urlpatterns = [
    path('home/', home),
    path('contact/', contact),
    path('about/', about),
    path('profile/', profile),
    path('blog/', blog),
]
