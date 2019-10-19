from django import forms
from .models import user_info

class loginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user_info
        #widget = {'password': forms.PasswordInput()}
        fields = ['username', 'password']


#class RawLoginForm(forms.Form):
 #   username = forms.CharField(max_length=50)
  #  password = forms.CharField(max_length=50)



#-- using a django form--!

#class RawLoginForm(forms.Form):
#    username = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)