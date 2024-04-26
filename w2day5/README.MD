How to add CSS/Images[Static FIles]  to project:
----------------------------------

step 1) create a static folder with in the project directory

step 2) create a static files inside the static folder.

step 3) Register the path of static folder so go to settings.py

step 4) create a path for static folder

	STATIC_DIR=os.path.join(BASE_DIR,'static')

step 5) Register the Path Inside the STATICFILES_DIRS list

	STATICFILES_DIRS=[STATIC_DIR]

step 6) to use css open HTML file and first line pf HTML File should be load static

	{% load static %}


step 7) set the path of css file by using link tag so we need to use static wrto django

	{% static 'fileName' %}

<link rel='' href="{% static 'fileName' %}" > 

step 8): start the server