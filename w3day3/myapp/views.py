from django.shortcuts import render


def home(request):
    data = {
        "sublist": [[22, 21, 88, 291, 228, 19], [22, 10, 41, 55, 82, 17,], [68, 76, 23, 44, 30, 8]],
        "list": [22, 21, 88, 291, 228, 19, 22, 10, 41, 55, 82, 17, 68, 76, 23, 44, 30, 8],
        "string": "hello world",
    }

    return render(request, "index.html", data)
