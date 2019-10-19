from __future__ import unicode_literals

from django.shortcuts import render
from .forms import signupForm
from .models import user_details
from rest_framework import viewsets, serializers


# Create your views here.

#def login_view(request):
 #   form = RawLoginForm()
  #  if request.method == 'POST':
   #     form = RawLoginForm(request.POST)
    #    if form.is_valid():
     #       print(form.cleaned_data)
      #      logindetails.objects.create(**form.cleaned_data)
       # else:
        #    print(form.errors)
    #context = {
     #   'form': form
    #}

    #return render(request, 'login/login.html', context=context)

def signup_view(request):

    form = signupForm(request.POST or None)
    if form.is_valid():
       form.save()
       form = signupForm()

    context = {'form': form
               # 'name': obj2.Name,
                #'name2': obj.Name,
                #'summary': obj.Summary

               }
    return render(request, 'signup.html', context)

class SignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_details
        fields = ['id', 'username']

# ViewSets define the view behavior.
class SignupViewSet(viewsets.ModelViewSet):
    queryset = user_details.objects.all()
    serializer_class = SignupSerializer