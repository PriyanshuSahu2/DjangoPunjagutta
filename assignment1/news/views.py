from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def news(request):
    return render(request, 'news.html')


def news_sports(request):
    return render(request, 'news-sports.html')


def news_politics(request):
    return render(request, 'news-politics.html')


def news_movies(request):
    return render(request, 'news-movies.html')
