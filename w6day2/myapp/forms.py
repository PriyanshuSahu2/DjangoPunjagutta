from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'name'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':'password'}))
    list2 = [('Male','MALE'),('Female','FEMALE')]
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=list2)
    color_list = [('Red',"RED"),('Green',"GREEN"),('Yellow','YELLOW')]
    color = forms.MultipleChoiceField(choices=color_list)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=[2019,2018]))
    file = forms.FileField()
    image_field = forms.ImageField()
    