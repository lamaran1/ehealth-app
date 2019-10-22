from django import forms
from .models import user_details
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



#class signupForm(ModelForm):
#    class Meta:
#        model = user_details
#        widget = {'password': forms.PasswordInput()}
#        exclude = ['user']




#-- using a django form--!

#class RawLoginForm(forms.Form):
 #   username = forms.CharField()
  #  password = forms.CharField(widget=forms.PasswordInput)


#Title = forms.CharField(max_length=20)
#Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname first'}))
#Email = forms.EmailField(max_length=300)
#Password = forms.CharField(widget=forms.PasswordInput)
#Confirm_Password = forms.CharField(widget=forms.PasswordInput)
#Address = forms.CharField(max_length=500)
#Age = forms.IntegerField()
#Diagnosed_with_Malaria = forms.TypedChoiceField(coerce=lambda x: x == 'True',
#                                               choices=((False, 'No'), (True, 'Yes')))
#Diagnosed_with_Typhoid = forms.TypedChoiceField(coerce=lambda x: x == 'True',
#                                                choices=((False, 'No'), (True, 'Yes')))
#Deep_Cuts = forms.TypedChoiceField(coerce=lambda x: x == 'True',
#                                   choices=((False, 'No'), (True, 'Yes')))
#Tuberculosis = forms.TypedChoiceField(coerce=lambda x: x == 'True',
#                                      choices=((False, 'No'), (True, 'Yes')))
#Sickel_cell = forms.TypedChoiceField(coerce=lambda x: x == 'True',
#                                     choices=((False, 'No'), (True, 'Yes')))
