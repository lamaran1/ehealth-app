from django.shortcuts import render
#from .table import ProfileTable
#from .filter import UserFilter
#from signup.models import user_details
#from rest_framework import viewsets, serializers
#from .models import User

 #Create your views here.
def homepage(request, *args, **kwargs):
    #print (args, kwargs)
    #print (request.user)
    return render(request, 'homepage.html', {})

def about(request, *args, **kwargs):
    #print (args, kwargs)
    #print (request.user)
    return render(request, 'about.html', {})


#def value_count():
 #   '''This function counts the number of user that selected Yes to a Category and returns a dictionary'''
 #   users= User.objects.all()
 #   Malaria_number, Typhoid_number, Cuts_number, Tuberculosis_number, SickelCell_number = 0,0,0,0,0
 #   for i in users:
 #       if i.profile.Diagnosed_with_Malaria=='Yes':
 #           Malaria_number += 1
 #       if i.profile.Diagnosed_with_Typhoid=='Yes':
 #           Typhoid_number += 1
 #       if i.profile.Deep_Cuts=='Yes':
 #           Cuts_number += 1
 #       if i.profile.Tuberculosis=='Yes':
 #           Tuberculosis_number += 1
 #       if i.profile.Sickel_cell=='Yes':
 #           SickelCell_number += 1
 #   value = {
 #       'Diagnosed_with_Malaria': Malaria_number,
 #       'Diagnosed_with_Typhoid': Typhoid_number,
 #       'Deep_Cuts': Cuts_number,
  #      'Tuberculosis': Tuberculosis_number,
  #      'Sickel_cell': SickelCell_number
  #  }
 #   return value

#value = value_count()


#def ehealth_tables(request):
 #   user_list = user_details.objects.all()
 #   user_filter = UserFilter(request.GET, queryset=user_list)

#    return render(request, 'tables.html',  {
#    'filter': user_filter,
#    'value': value} )