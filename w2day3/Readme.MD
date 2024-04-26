connecting HTML file with each view:
-----------------------------------

1)  create a template folder with respect to project level

2) create html files inside the template folder

3) open settings.py to register/build path of template folder with respect to project

	step 1) import os

	step 2) create a varibale TEMPLATE_DIR
	
		TEMPLATE_DIR=os.path.join(BASE_DIR,'template')
	
	step 3) search TEMPLATES list which contains dictionary
		and in DIRS key store TEMPLATE_DIR

4) create a view but view need to return render object,so we need to use render function for each view
			
		render(request,'htmlfilename')

from django.shortcuts import render
def home(request):
    return render(request,'home.html')


5) create app level url and register with view and ridirect app level url with project level url.



