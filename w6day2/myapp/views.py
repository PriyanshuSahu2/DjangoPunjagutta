from django.shortcuts import render

from myapp.forms import LoginForm


def home(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form})
