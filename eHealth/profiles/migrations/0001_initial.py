# Generated by Django 2.2.6 on 2019-10-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(default='none@email.com', max_length=254)),
                ('Malaria', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Diarrheal_Diseases', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Road_Injuries', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Tuberculosis', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Cough', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
            ],
        ),
    ]
