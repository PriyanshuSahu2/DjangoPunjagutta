from django.shortcuts import render


def home(request):
    return render(request, 'myapp2/home.html')
