from django.http import HttpResponse


def home(request):
    data = '<div style="font-size:30px;color:red;">This is Home Page</div>'
    return HttpResponse(data)


def contact(request):
    data = '<div style="font-size:30px;color:red;">This is contact page</div>'
    return HttpResponse(data)


def blog(request):
    data = '<div style="font-size:30px;color:red;">This is Blog page</div>'
    return HttpResponse(data)


def about(request):
    data = '<div style="font-size:30px;color:red;">This is About page</div>'
    return HttpResponse(data)

def profile(request):
    data = '<div style="font-size:30px;color:red;">This is Profile Page</div>'
    return HttpResponse(data)
