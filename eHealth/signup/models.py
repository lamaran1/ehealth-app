
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class user_details(models.Model):
    choices = (("Yes", 'Yes'), ("No", 'No'))
    Name = models.CharField(max_length = 300)
    Email = models.EmailField(max_length = 300, default='none@gmail.com')
    #password = models.CharField(max_length=250)
    Title = models.CharField(max_length = 20)
    Address = models.CharField (max_length = 500)
    Email = models.EmailField(default='none@email.com')
    Diagnosed_with_Malaria = models.CharField(max_length=255, choices=choices, null=True)
    Diagnosed_with_Typhoid = models.CharField(max_length=255, choices=choices, null=True)
    Deep_Cuts = models.CharField(max_length=255, choices=choices, null=True)
    Tuberculosis = models.CharField(max_length=255, choices=choices, null=True)
    Sickel_cell = models.CharField(max_length=255, choices=choices, null=True)
    # def __str__(self):


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_details.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


def __str__(self):
    return self.Name
