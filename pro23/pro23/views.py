from django.http import HttpResponse


def home(request):
    data = '<h1 style="color:green; text-align:center"> Hello This is My First Response</h1>'
    return HttpResponse(data)
