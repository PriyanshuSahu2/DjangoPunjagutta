from django.shortcuts import render

from myapp.forms import RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm()
    return render(request, 'index.html', {'form': form})
