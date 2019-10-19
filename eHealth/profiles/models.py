from django.db import models

# Create your models here.
class Profile(models.Model):
    choices = (("Yes", 'Yes'), ("No", 'No'))
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
   # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Email = models.EmailField(default='none@email.com')
    Malaria = models.CharField(max_length=255, choices=choices )
    Diarrheal_Diseases = models.CharField(max_length=255,choices=choices)
    Road_Injuries = models.CharField(max_length=255, choices=choices)
    Tuberculosis = models.CharField(max_length=255, choices=choices)
    Cough = models.CharField(max_length=255, choices=choices)
    #def __str__(self):
    #    return f'{self.user.username} Profile'

