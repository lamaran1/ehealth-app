from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userdetails', null=True)
    choices = (("Yes", 'Yes'), ("No", 'No'))
    Name = models.CharField(max_length = 300)
    Email = models.EmailField(max_length = 300, default='none@gmail.com')
    #password = models.CharField(max_length=40)
    Title = models.CharField(max_length = 20)
    Address = models.CharField (max_length = 500)
    Email = models.EmailField(default='none@email.com')
    Diagnosed_with_Malaria = models.CharField(max_length=255, choices=choices, null=True)
    Diagnosed_with_Typhoid = models.CharField(max_length=255, choices=choices, null=True)
    Deep_Cuts = models.CharField(max_length=255, choices=choices, null=True)
    Tuberculosis = models.CharField(max_length=255, choices=choices, null=True)
    Sickel_cell = models.CharField(max_length=255, choices=choices, null=True)

    def __str__(self):
        return self.Name

class item(models.Model):
    userdetails=models.ForeignKey(user_details, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

#user = User.objects.create_user('myusername', 'myemail@gmail.com', 'mypassword')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to= 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'