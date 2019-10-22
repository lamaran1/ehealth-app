# Generated by Django 2.2.6 on 2019-10-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnosed_with_Malaria', models.CharField(max_length=255, null=True)),
                ('Diagnosed_with_Typhoid', models.CharField(max_length=255, null=True)),
                ('Deep_Cuts', models.CharField(max_length=255, null=True)),
                ('Tuberculosis', models.CharField(max_length=255, null=True)),
                ('Sickel_cell', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
