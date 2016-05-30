# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime
from django.db import models


class Messages(models.Model):
    from_user = models.ForeignKey('core.User', verbose_name=u'От кого', related_name='from_user')
    to_user = models.ForeignKey('core.User', verbose_name=u'Кому', related_name='to_user')
    theme = models.CharField(max_length=250, verbose_name=u'Тема')
    text = models.TextField(max_length=1000, verbose_name=u'Текс')
    unread = models.BooleanField(default=True, verbose_name=u'Не прочитано?')
    created_date = models.DateTimeField(default=datetime.now, verbose_name=u'Дата отправки')

# Create your models here.
