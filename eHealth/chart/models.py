from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class data_collect(models.Model):
    Diagnosed_with_Malaria = models.CharField(max_length=255, null=True)
    Diagnosed_with_Typhoid = models.CharField(max_length=255, null=True)
    Deep_Cuts = models.CharField(max_length=255, null=True)
    Tuberculosis = models.CharField(max_length=255, null=True)
    Sickel_cell = models.CharField(max_length=255, null=True)


