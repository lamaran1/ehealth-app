# Generated by Django 2.2.6 on 2019-10-20 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0005_auto_20191019_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userdetails', to=settings.AUTH_USER_MODEL),
        ),
    ]