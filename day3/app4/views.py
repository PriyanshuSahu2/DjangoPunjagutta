from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return HttpResponse('<h1>App 4 Home </h1>')

def profile(req):
    return HttpResponse('<h1>App 4 Home </h1>')


def contact(req):
    return HttpResponse('<h1>App 4 Contact </h1>')


def about(req):
    return HttpResponse('<h1>App 4 About </h1>')


def blog(req):
    return HttpResponse('<h1>App 4 Blog </h1>')
