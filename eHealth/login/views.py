from .models import user_info
from django.shortcuts import render
from .forms import loginForm
from django.contrib.auth import authenticate, login
from rest_framework import viewsets, serializers
from django.contrib.auth.models import User


# Create your views here.

#def login_view(request):
 #   uservalue = ''
 #   passwordvalue = ''

    #form = loginForm(request.POST or None)
    #if form.is_valid():
    #    uservalue = form.cleaned_data.get("username")
    #    passwordvalue = form.cleaned_data.get("password")

        #user = authenticate(username=uservalue, password=passwordvalue)
        #if user is not None:
         #   login(request, user)
         #   context = {'form': form,
         #              'error': 'The login has been successful'}

            #return render(request, 'homepage.html', context)
        #else:
        #    context = {'form': form,
         #              'error': 'The username and password combination is incorrect'}

          #  #return render(request, 'login.html', context)

    #else:
     #   context = {'form': form}
      #  return render(request, 'login.html', context)

    #form.save()
    #form = loginForm()

    #context = {'form': form
               # 'name': obj2.Name,
                #'name2': obj.Name,
                #'summary': obj.Summary

     #          }
    #return render(request, 'login.html', context)

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_info
        fields = ['id', 'username']

# ViewSets define the view behavior.
#class LoginViewSet(viewsets.ModelViewSet):
#    queryset = user_info.objects.all()
#    serializer_class = LoginSerializer

