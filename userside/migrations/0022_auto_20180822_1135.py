# Generated by Django 2.0.5 on 2018-08-22 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0021_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
