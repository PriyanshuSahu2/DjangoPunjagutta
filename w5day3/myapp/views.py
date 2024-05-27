from django.shortcuts import render

from myapp.models import Student


def home(request):
    data = Student.objects.filter(age__gte=18)

    return render(request, 'index.html', {'data': data})
