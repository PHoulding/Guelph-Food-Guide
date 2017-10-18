# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-14 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuelphFoodGuideSite', '0003_resource_dietaryrestrictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='pricePoint',
            field=models.CharField(choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$')], default='$$', max_length=3),
        ),
    ]