# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_auto_20160528_2351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicetype',
            options={'verbose_name': '\u0412\u0438\u0434 \u0440\u0430\u0431\u043e\u0442\u044b', 'verbose_name_plural': '\u0412\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442'},
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='users',
            field=models.ManyToManyField(blank=True, to='works.Employee', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b'),
        ),
    ]
