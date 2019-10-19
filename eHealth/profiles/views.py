from __future__ import unicode_literals

from django.shortcuts import render
from .forms import MyForm
from .models import Profile
from rest_framework import viewsets, serializers

def profile_view(request):

    form = UpdateMyForm(request.POST or None)
    if form.is_valid():
       form.save()
       form = profileForm()

    context = {'form': form
               # 'name': obj2.Name,
                #'name2': obj.Name,
                #'summary': obj.Summary

               }
    return render(request, 'profile.html', context)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username']

# ViewSets define the view behavior.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer