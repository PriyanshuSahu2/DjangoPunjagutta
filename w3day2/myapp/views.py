from django.shortcuts import render

# Create your views here.


def home(req):
    data = {
        "data": [
            {
                "id": 1,
                "age": 20,
                "location": "Saudi Arabia",
                "name": "Inez Silva"
            },
            {
                "id": 1,
                "age": 18,
                "location": "San Marino",
                "name": "Blake Curry"
            },
            {
                "id": 1,
                "age": 21,
                "location": "Fiji",
                "name": "Joshua Shaw"
            },
            {
                "id": 1,
                "age": 22,
                "location": "Nigeria",
                "name": "Don Horton"
            },
            {
                "id": 1,
                "age": 22,
                "location": "Anguilla",
                "name": "Aiden Cummings"
            },
        ]
    }
    return render(req, "index.html", data)
