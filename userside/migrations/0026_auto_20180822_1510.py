# Generated by Django 2.0.5 on 2018-08-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0025_auto_20180822_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
