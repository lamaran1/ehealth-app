from django.shortcuts import render

#from rest_framework import viewsets, serializers

# Create your views here.
def homepage(request, *args, **kwargs):
    #print (args, kwargs)
    #print (request.user)
    return render(request, 'homepage.html', {})