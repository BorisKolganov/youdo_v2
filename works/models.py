# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField('core.User', verbose_name=u'Профиль')
    about = models.TextField(verbose_name=u'О себе')
    skills = models.TextField(verbose_name=u'Умения')
    experience = models.TextField(verbose_name=u'Опыт')


class ServiceType(models.Model):
    name = models.CharField(max_length=250, verbose_name=u'Название')
    users = models.ManyToManyField('core.User', verbose_name=u'Специалисты', blank=True)


class Service(models.Model):
    user = models.ForeignKey('core.User', verbose_name=u'Пользователь')
    employee = models.ForeignKey('works.Employee', verbose_name=u'Исполнитель')
    name = models.CharField(max_length=250, verbose_name=u'Название')
    price = models.IntegerField(verbose_name=u'Оплата')
    avatar = models.ImageField(verbose_name=u'Аватар', null=True)
    type = models.ForeignKey('works.ServiceType', verbose_name=u'Тип услуги')


class Comment(models.Model):
    user = models.ForeignKey('core.User', verbose_name=u'Пользователь')
    service = models.ForeignKey('works.Service', verbose_name=u'услуга')
    text = models.TextField(verbose_name=u'Текст комментария')
    rating = models.SmallIntegerField(verbose_name=u'Оценка')