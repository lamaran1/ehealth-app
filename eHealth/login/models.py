from django.db import models

from django.utils import timezone

class user_info(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.name}'

