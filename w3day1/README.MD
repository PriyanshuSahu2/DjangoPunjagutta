How to send python Backend data to HTML file:
-----------------------------------------


Step 1) create a view inside views.py

step 2) take python data and store in the form of dict . as key value 
pairs

        data={'name':'azhar','age':22,'gender':'Male','marks':[100,200]}

step 3) dictionary should have to pass as arguemnt to render function
either assign to context parameter or pass directly.

		render(request,'info.html',data)

		render(request,'info.html',context=data)

step 4)  now pythonn data is avaiable to html file  that can be accessed by using template variable.

step 5) always remember to use key names as variables inside the html file (key names should be used without single quotes)

		{{ keyName }}

