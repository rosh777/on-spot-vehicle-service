# Generated by Django 2.0.5 on 2018-07-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('fuel', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel')], default='diesel', max_length=6)),
            ],
        ),
    ]
