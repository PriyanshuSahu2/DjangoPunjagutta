from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('''<body style='padding:0px;margin:0px;'><div style='height:40px; background-color:black;color:white;display:flex;gap:20px;align-items:center;padding:0 20px;'>
                 <a href="/home" style='color:white; font-size:20px'>home</a>
                <a href="/contact" style='color:white; font-size:20px'>contact</a>
                <a href="/about" style='color:white; font-size:20px'>about</a>
                        </div>
                        <h1>This is About Page</h1>
                        </body>''')
