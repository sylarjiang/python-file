# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title_img',
            field=models.ImageField(default=0, upload_to='', verbose_name='文章配图'),
            preserve_default=False,
        ),
    ]
