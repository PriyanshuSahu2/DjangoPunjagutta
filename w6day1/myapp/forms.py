from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    age = forms.CharField()
    password = forms.CharField()

    name.widget.attrs['class'] ="NameInput"
    
    
    