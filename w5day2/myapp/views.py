from django.shortcuts import render

from myapp.models import Student

# Create your views here.


def home(request):
    data = Student.objects.all()
    return render(request, 'index.html', {'data': data})
