# Generated by Django 2.0.5 on 2018-08-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0013_auto_20180815_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]