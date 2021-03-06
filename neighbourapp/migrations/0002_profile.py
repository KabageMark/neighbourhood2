# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='profile-pics')),
                ('bio', models.TextField()),
                ('neighbourhood_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
    ]
