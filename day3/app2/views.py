from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return HttpResponse('<h1>App 2 Home </h1>')

def profile(req):
    return HttpResponse('<h1>App 2 Home </h1>')


def contact(req):
    return HttpResponse('<h1>App 2 Contact </h1>')


def about(req):
    return HttpResponse('<h1>App 2 About </h1>')


def blog(req):
    return HttpResponse('<h1>App 2 Blog </h1>')
