from django import forms
from .models import user_details
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class signupForm(forms.ModelForm):
#    choices = (("Yes", 'Yes'), ("No", 'No'))
    Title = forms.CharField(max_length=20)
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname first'}))
    Email = forms.EmailField(max_length = 300)
    Password = forms.CharField(widget=forms.PasswordInput)
    Confirm_Password = forms.CharField(widget=forms.PasswordInput)
    Address = forms.CharField(max_length=500)
    Age = forms.IntegerField()
    Diagnosed_with_Malaria = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                    choices=((False, 'No'), (True, 'Yes')))
    Diagnosed_with_Typhoid = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                    choices=((False, 'No'), (True, 'Yes')))
    Deep_Cuts = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                    choices=((False, 'No'), (True, 'Yes')))
    Tuberculosis = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                    choices=((False, 'No'), (True, 'Yes')))
    Sickel_cell = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                    choices=((False, 'No'), (True, 'Yes')))

    class Meta:
        model = user_details
        #widget = {'password': forms.PasswordInput()}
        fields = ['Title', 'Name', 'Email', 'Password', 'Address', 'Age']

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_details.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


#class MyForm(forms.ModelForm):
#    class Meta:
#        model = user_details
#        fields = [

     #       'Malaria',
    #        'Diarrheal_Diseases',
   #         'Road_Injuries',
  #          'Tuberculosis',
 #           'Cough'
#        ]
#class RawLoginForm(forms.Form):
 #   username = forms.CharField(max_length=50)
  #  password = forms.CharField(max_length=50)



#-- using a django form--!

#class RawLoginForm(forms.Form):
 #   username = forms.CharField()
  #  password = forms.CharField(widget=forms.PasswordInput)