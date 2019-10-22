from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import user_details
from rest_framework import viewsets, serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('http://127.0.0.1:8000/')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def do_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name','')
        user_password = request.POST.get('user_password','')

        user = auth.authenticate(request, username = user_name, password = user_password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect ('/')
        else:
            return render(request, 'login.html')



def do_register(request):
    if request.method == 'POST':
        user_name = user_name = request.POST.get('user_name','')
        user_password = request.POST.get('user_password', '')
        user_email = request.POST.get('user_email', '')

        if len(user_name) > 0 and len(user_password) > 0 and len(user_email)> 0:
            user = auth.authenticate(request, username = user_name, password = user_password)

            if user is None:
                user = get_user_model().objects.create_user(username = user_name, password = user_password, email = user_email)

                if user is not None:
                    user.is_staff =True
                    user.save()

                response = HttpResponseRedirect('/')

            else:
                return render(request, 'signup.html')


#def signup_view(request):
#    form = signupForm(request.POST)
#    if request.method == "POST":
#       if form.is_valid():
#           print(form.cleaned_data)
#           form.save()
#           user_details.objects.create(**form.cleaned_data)
#           return HttpResponseRedirect ('/')

 #   else:
 #       print(form.errors)

    #return render(request, 'signup.html', {"form":form})


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    # noinspection PyUnreachableCode
    class Meta:
        model = user_details
        fields = ['id', 'username']

# ViewSets define the view behavior.
class SignupViewSet(viewsets.ModelViewSet):
    queryset = user_details.objects.all()
    serializer_class = SignupSerializer

@login_required
def user_profile(request):
    obj = user_details.objects.all()
    obj2 = user_details.objects.all()
    context = {'object': obj, 'object2': obj2
                   # 'name': obj2.Name,
                   # 'name2': obj.Name,
                   # 'summary': obj.Summary

                   }


    return render(request, 'profile.html', context)

#form = signupForm(request.POST or None)