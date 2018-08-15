# Generated by Django 2.0.5 on 2018-08-10 17:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0007_auto_20180809_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326, verbose_name='longitude/latitude'),
        ),
    ]
