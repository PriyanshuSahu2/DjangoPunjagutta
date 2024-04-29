from django.shortcuts import render


def home(request):
    data = {'details': [
        {'id': 1, 'name': "Priyanshu Sahu", 'age': 21, 'location': "India",
         },
        {'id': 2, 'name': "Lina Hanson", 'age': 23, 'location': "Greenland",
         },
        {'id': 3, 'name': "Jay Perry", 'age': 30, 'location': "Switzerland",
         },
        {'id': 4, 'name': "Julian Ramirez", 'age': 23, 'location': "Solomon Islands",
         },

    ]}
    return render(request, 'index.html', data)
