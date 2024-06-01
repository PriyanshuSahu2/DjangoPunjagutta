from django.shortcuts import render

from myapp.forms import StudentForm
from myapp.models import Student


def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    img = Student.objects.get(id=1)
    form = StudentForm()

    return render(request, 'index.html', {'form': form, 'img': img.photo})
