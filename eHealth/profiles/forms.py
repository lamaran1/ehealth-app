from django import forms
from .models import Profile


question1 = ['Have you ever being diagnosed with an STD ?', 'Have you been diagnosed with sickle cell',
             'Are you a recreational drug user']
choices = ((" ", " "), ("Yes", 'Yes'), ("Yes", 'No'))



class MyForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [

            'Malaria',
            'Diarrheal_Diseases',
            'Road_Injuries',
            'Tuberculosis',
            'Cough'
        ]
